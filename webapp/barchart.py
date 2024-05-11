from swimclub import process_swim_data
from hfpy_utils import convert2range
import json
import os
CHARTS ="charts/"
JSONDATA = "./webapp/world_records.json"
COURSES = ["LC MEN","LC WOMEN","SC MEN","SC WOMEN"]



def event_lookup(filename):
    conversions = {
    "Free":"freestyle",
    "Back":"backstroke",
    "Breast":"breaststroke",
    "Fly":"butterfly",
    "IM":"individual medley"

}
    *_,distance,event = filename.removesuffix(".txt").split("-")

    return f"{distance} {conversions[event]}"


def draw_bar_chart(filename,location=CHARTS):
    swimmer = process_swim_data(filename)
    ranges = []
    name = swimmer["name"] 
    times = swimmer["times"]
    age = swimmer["age"]
    converts = swimmer["converts"]
    distance = swimmer["distance"]
    average = swimmer["average"]
    stroke = swimmer["stroke"]
    times.reverse()
    converts.reverse()
    records = []

    max_range = max(converts)
    with open(JSONDATA) as jf:
        world_records =json.load(jf)
    for course in COURSES:
        records.append(world_records[course][event_lookup(filename)])
    for n in converts:
                ranges.append(convert2range(n,0,max_range,0,350))
                title = f"{name} (Under {age}) {distance} - {stroke}"
                html = f"""
                    <!DOCTYPE html>
                    <head>
                    <title>{title}</title>
                    </head>
                    <body>
                    <h3>{title}</h3>
                    """
                footer = f"""<p>Average time {average}</p>
                    <p> <h4>M: {records[0]}
                            ({records[2]})
                        </h4>
                        <h4> W: {records[1]}
                            ({records[3]})
                        </h4>
                    </p>
                    </body>
                    </html>
                    """
    svgs =""
    
    for count,range in enumerate(ranges):
                        svgs += f"""
                        <svg width="400" height="30">
                        <rect width="{range}" height="30" style="fill:rgb(0,0,255);"/>
                        </svg> {times[count]}<br>
                        """
    page = html + svgs + footer
    save = os.path.join(location, f"{filename.removesuffix('.txt')}.html")

    with open(save, "w") as file_html:
        print(page,file=file_html)
    return os.path.realpath(save)