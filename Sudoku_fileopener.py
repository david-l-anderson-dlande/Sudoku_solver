import os

def get_file_name(possiblename):
    csvlist = get_file_name_list()
    if possiblename in csvlist:
        usedname = possiblename
    else:
        usedname = get_file_name_dialog(csvlist)
    return usedname

def get_file_name_list():
    listoffilescurrentdirectory=os.listdir()
    csvfiles=[filename for filename in listoffilescurrentdirectory\
              if filename[(len(filename)-4):] == '.csv']
    return csvfiles
    

def get_file_name_dialog(csvfilelist):
    for i in range(len(csvfilelist)):
        print(i, csvfilelist[i])
    namechoice = get_file_name_dialog_request()
    if namechoice in csvfilelist:
        chosenname = namechoice
    elif namechoice + '.csv' in csvfilelist:
        chosenname = namechoice + '.csv'
    else:
        chosenname = get_file_name_dialog_number(namechoice, csvfilelist)
    return chosenname

def get_file_name_dialog_request():
    inputfilename = input('Please enter the number or name of the .csv file'\
                           ' containing the puzzle: ')
    return inputfilename


def get_file_name_dialog_number(numberindex, csvfiles):
    csvdictionary = {repr(i):csvfiles[i] for i in range(len(csvfiles))}
    if numberindex in csvdictionary:
            csvfilename = csvdictionary[numberindex]
    else:
        print('That is not a valid filename.')
    return csvfilename
      
    

