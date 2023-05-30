# Method to Get input from the user
# Passing the input message (msg) as parameter
def getInput(msg):
    while True:
        try:
            # Getting the credit as integer
            credit = int(input(msg))

            # Checking whether the credit range is in 0, 20, 40, 60, 80, 100, 120
            if (not ((credit % 20 == 0) and (credit >= 0 and credit <= 120))):
                print("Out of range")
                continue
            break
        except ValueError:
            print("Integer required")

    return credit


# Method to check the total credit =  120
# Passing Pass(p), Defer(d), Fail(f) as parameters
def checkTotal(p, d, f):
    # Checking whether the credits total is equal to 120
    total = p + d + f
    if (total == 120):
        return True
    else:
        print("Total Incorrect")
        return False


# Method is used to find the correct progression
# Passing pass credits (p) and fail credits (f) as parameter to calculate the progression
# Part 1
def findProgressionOutcome(p, f):
    if p == 120:
        return "Progress"
    elif p == 100:
        return "Progress (module trailer)"
    elif p == 80 or p == 60:
        return "Module retriever"
    elif p == 40 and f == 80:
        return "Exclude"
    elif p == 40:
        return "Module retriever"
    elif (p == 20 and f == 80) or (p == 20 and f == 100):
        return "Exclude"
    elif p == 20:
        return "Module retriever"
    elif (p == 0 and f == 80) or (p == 0 and f == 100) or (p == 0 and f == 120):
        return "Exclude"
    elif p == 0:
        return "Module retriever"


# Method is used to generate the horizontal histogram
# Passing the progression list as parameter
# Part 2
def generteHorizontalHistogram(progressionList):
    # Separate string variable initialized for progress, trailer, retriever and excluded
    progress = ''
    trailer = ''
    retriever = ''
    excluded = ''

    for progression in progressionList:
        # Checking the progression and adding * according to the correct variable
        if progression == "Progress":
            progress += '*'
        elif progression == "Progress (module trailer)":
            trailer += '*'
        elif progression == "Module retriever":
            retriever += '*'
        elif progression == "Exclude":
            excluded += '*'

    # Printing the histogram
    print('------------------------------------')
    print('Horizontal Histogram')
    # Used format printing to print the results formatted
    print(f"{'Progress ' : <10}{str(len(progress)): ^1}{' : ': ^1}{progress: >1}")
    print(f"{'Trailer ' : <10}{str(len(trailer)): ^1}{' : ': ^1}{trailer: >1}")
    print(f"{'Retriever ' : <10}{str(len(retriever)): ^1}{' : ': ^1}{retriever: >1}")
    print(f"{'Excluded ' : <10}{str(len(excluded)): ^1}{' : ': ^1}{excluded: >1}")
    print('\n')
    print(str(len(progress) + len(trailer) + len(retriever) + len(excluded)) + ' Outcomes in Total.')
    print('------------------------------------')


# Method is used to generate vertical histogram
# Passing progression list as parameter
# Part 2
def generateVerticalHistogram(progressionList):
    # Initializing separate variables for progress, trailer, retriever and excluded
    progress = 0
    trailer = 0
    retriever = 0
    excluded = 0
    for progression in progressionList:
        # Checking the progression and increasing +1 from the correct variable count
        if progression == "Progress":
            progress += 1
        elif progression == "Progress (module trailer)":
            trailer += 1
        elif progression == "Module retriever":
            retriever += 1
        elif progression == "Exclude":
            excluded += 1

    # Used format printing to print the vertical histogram
    print('------------------------------------')
    print('Vertical Histogram')
    print(f"{'Progress' : ^10}{'Trailer' : ^10}{'Retriever' : ^10}{'Excluded': ^10}")
    # For loop is going to run for maximum variable count
    for x in range(max(progress, trailer, retriever, excluded)):
        print(
            f"{'*' if x < progress else '' : ^10}"
            f"{'*' if x < trailer else '': ^10}"
            f"{'*' if x < retriever else '': ^10}"
            f"{'*' if x < excluded else '': ^10}"
        )
    print('\n')
    print(str(progress + trailer + retriever + excluded) + ' Outcomes in Total.')
    print('------------------------------------')


# to continue the loop
def getOption():
    while True:
        print('\n')
        option = input(
            "Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        if option == "y" or option == "q":
            print('\n')
            break

        else:
            print("Invalid Option")
            continue

    return option

# Used to print the progression from dictionary
# Part 3
def printFromDict(progressionDict):
    keys = ['Progress', 'Progress (module trailer)', 'Module retriever', 'Exclude']
    print('------------------------------------')
    print('Reading from dictionary')
    for key in keys:
        for progression in progressionDict[key]:
            print(progression)
    print('------------------------------------')

# Used to save input progression data to a text file.
def writeToFile(progressionDict, path):
    keys = ['Progress', 'Progress (module trailer)', 'Module retriever', 'Exclude']
    file = open(path, 'w')
    for key in keys:
        for progression in progressionDict[key]:
            file.writelines(progression + '\n')

    file.close()

# Used to read the data from the text file
def readFile(path):
    file = open(path, 'r')
    print('------------------------------------')
    print('Reading from file')
    for progression in file.readlines():
        print(progression)
    print('------------------------------------')


# Main function
def question():
    progressionList = []
    progressionDict = {
        'Progress': [],
        'Progress (module trailer)': [],
        'Module retriever': [],
        'Exclude': []
    }

    while True:
        # p - pass  d - defer   f - fail
        p = getInput("Enter your total PASS credits: ")
        d = getInput("Enter your total DEFER credits: ")
        f = getInput("Enter your total FAIL credits: ")

        if not checkTotal(p, d, f):
            continue
        progression = findProgressionOutcome(p, f)
        progressionList.append(progression)
        print(progression)

        # formatted string
        progressionString = f"{progression : <1}{' - ': ^1}{str(p): ^1}{',': ^1}{str(d): ^1}{',': ^1}{str(f): >1}"

        # Appending the string to the dictionary
        progressionDict.get(progression).append(progressionString)

        # Checking the option
        option = getOption()
        if option == 'y':
            continue
        else:
            break
    print('Select an option to display the summary of results')
    print('''    (1) Generate Horizontal Histogram
    (2) Generate Vertical Histogram
    (3) Store the results to Dictionary and read from Dictionary
    (4) Store the results in a Text file and read from Text file''')
    while True:
        option = input('\nPlease select an option - 1,2,3,4 or 5 to quit? ')
        if option == '1':
            generteHorizontalHistogram(progressionList)
        elif option == '2':
            generateVerticalHistogram(progressionList)
        elif option == '3':
            printFromDict(progressionDict)
        elif option == '4':
            writeToFile(progressionDict, 'progression.txt')
            readFile('progression.txt')
        elif option == '5':
            quit()
        else:
            print('invalid option')
            continue

# Calling the main function
question()
