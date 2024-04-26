from statistics import mean
from math import ceil
def process_swim_data(filename):
    centiseconds = []
    FN = filename
    FOLDER ="swimdata/"
    #Unpack user details from the text file name
    swimmer_name,age,distance,stroke = FN.strip(".txt").split("-")
    with open(FOLDER + FN) as file:
        lines = file.readlines()
    #Split the various times to a times list
    times = lines[0].strip().split(",")
    
    #Convert time to centiseconds
    for time in times:
        
    
    
    