from swimclub import process_swim_data,FOLDER
from hfpy_utils import convert2range

def draw_bar_chart(filename,templates ="charts/"):
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

    max_range = max(converts)
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
    save = f"charts/{filename.removesuffix('.txt')}.html"
    with open(save,"w") as file_html:
        print(page, file=file_html)
    return save
