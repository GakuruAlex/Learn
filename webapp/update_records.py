from gazpacho import Soup,get
import json


def import_records():
    URL ="https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
    JSON_PATH = "./webapp/"
    COURSES =["LC MEN","LC WOMEN","SC MEN","SC WOMEN"]
    RECORDS = [0,2,4,5]
    html = get(URL)
    tables = Soup(html).find("table",mode="all")
    records = {}
    for record,course in zip(RECORDS,COURSES):
        records[course] ={}
        rows = tables[record].find("tr",mode = "all")[1:]
        for row in rows:
            columns = row.find("td",mode ="all")
            event = columns[0].text
            time = columns[1].text
            if "relay" not in event:
                records[course][event] = time
    
    with open(f"{JSON_PATH}world_records.json","w") as file:
        json.dump(records,file)
   
        