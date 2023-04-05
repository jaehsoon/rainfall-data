FILE_IN_NAME = "5965003 KINASARABAN KUNDASANG-RF-HOURLY-20100101-20201231.txt"
FILE_OUT_NAME = "CleanData - Kinasaraban.txt"

removingValueFlag = False
year = 2009
month = 0
dayCount = 1

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def is_month(word):
    if word in months:
        # print("The word is " + word)
        global month
        month = months.index(word) + 1

        global dayCount
        dayCount = 1
        removingValueFlag = False

        global year
        if word == "January":
            year += 1

with open(FILE_IN_NAME, "r") as in_file, \
    open (FILE_OUT_NAME, "w") as out_file:
    hourCount = 1
    for line in in_file:
        # print(dayCount)
        if line.startswith('~'):
            continue

        if line.__contains__('mm'):
            continue

        if line.__contains__('Day'):
            continue

        if line.__contains__('End'):
            continue

        # if line.__contains__('April'): #Stops printing if month is reached
        #     break
        
        line = line.replace("-", "0")
        line = line.split() #line is now an array

        ### Remove the line containing the month
        if line.__contains__("Hourly"):
            for word in line:
                is_month(word)
            continue

        ### Removing 1st and last value after hour line
        if line.__contains__('Hour'):
            removingValueFlag = True
            continue
        
        if removingValueFlag and len(line) != 0 :
            line.pop(0)
            line.pop(len(line)-1)

        ### End of removing 1st and last value
    
        hourCount = 1
        for word in line:
            print(str(year) + ", " + str(month) + ", " + str(dayCount) + ", " + str(hourCount) + ", "  + word)
            out_file.write(str(year) + ", " + str(month) + ", " + str(dayCount) + ", " + str(hourCount) + ", "  + word + "\n")
            hourCount += 1
        
        if len(line) > 0:
            dayCount += 1

            

        