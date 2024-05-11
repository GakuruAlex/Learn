from statistics import mean
from math import ceil
FOLDER ="./webapp/swimdata/"


def process_swim_data(filename: str)-> dict:
    """_Return swim data from file_
Given name of swimmers file , process it and return dictionary of swimmer details with average time taken for a given category


    Args:
        filename (str): _the name of file to be processed_

    Returns:
        dict: _Swimmers details_
    """
    centiseconds = []
    user_details ={}
  
    #Unpack user details from the text file name
    swimmer_name,age,distance,stroke = filename.removesuffix(".txt").split("-")
    #Store user details in a dictionary
    user_details["name"] = swimmer_name
    user_details["age"] = age
    user_details["distance"] = distance
    user_details["stroke"] = stroke

#Open the file in given folder
    with open(FOLDER + filename) as file:
        lines = file.readlines()
    #Split the various times to a times list
    times = lines[0].strip().split(",")
    #Add times list to user details
    user_details["times"] = times

#Convert time to centiseconds
    for time in times:
        if ":" in time:
            minutes,seconds_hundredths = time.split(":") #Convert time to minutes and seconds_and_hundredths
            seconds,hundredths = seconds_hundredths.split(".") #Convert seconds_and_hundredths to seconds and hundredths
            centisecond = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths) #convert minutes and seconds to hundredths and add to existing hundredths
        else:
            seconds,hundredths = time.split(".")
            centisecond = (int(seconds) * 100) + int(hundredths)
        centiseconds.append(centisecond) #Add converted hundredths to centiseconds list
#Calculate average
    average = mean(centiseconds)
    user_details["converts"] = centiseconds
#Convert calculated average to time
    minutes_seconds, hundredths = f"{(average / 100) :.2f}".split(".")
    minutes = int(minutes_seconds) // 60
    seconds = int(minutes_seconds) - (minutes * 60)
    
    time = f"{minutes}:{seconds:0>2}.{hundredths}"
    #Add average calculated to user details
    user_details["average"] = time
    
    return user_details



