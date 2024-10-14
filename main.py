import sfsutils
import os
import sys
path = open("path.txt", "r").readline()
savelist = os.listdir(path)
options = ["Rename","Edit Stupidity","Edit Courage","Edit Badass","Edit Veteran","Edit Gender","Edit Trait","Delete Kerbal","Exit"]
tf = ["False", "True"]
mf = ["Male","Female"]
ny = ["n","y"]
traits = ["Pilot","Engineer","Scientist"]
for i in savelist:
    print("["+str(savelist.index(i))+"]"+i)
try:
    save = int(input("Enter the number of the save you want to edit. >>>"))
except ValueError:
    print("Error: Value entered is not a number")
    input("Press enter to exit")
    sys.exit()
try:
    data = sfsutils.parse_savefile(path+"/"+savelist[save]+"/persistent.sfs")
except IndexError:
    print("Error: Save entered is out of lists range")
    input("Press enter to exit")
    sys.exit()
#name choicer
print()
names = [guy['name'] for guy in data['GAME']['ROSTER']['KERBAL']]
for i in names:
    print("["+str(names.index(i))+"]"+i)
try:
    kerbNum = int(input("Enter the number of the kerbal you want to edit >>>"))
except ValueError:
    print("Error: Value entered is not a number")
    input("Press enter to exit")
    sys.exit()
try:
    kerb = names[kerbNum]
except IndexError:
    print("Error: Kerbal entered is out of lists range")
    input("Press enter to exit")
    sys.exit()

def rename(data, oldname, newname):
    global names
    names = [guy['name'] for guy in data['GAME']['ROSTER']['KERBAL']]
    try:
        idx = names.index(oldname)
    except ValueError:
        print("Kerbal '%s' does not exist" % oldname)
        input("Press enter to exit")
        sys.exit()
    data['GAME']['ROSTER']['KERBAL'][idx]['name'] = newname

def remove(data):
    data['GAME']['ROSTER']['KERBAL'].pop(kerbNum)

def revalue(data, value, newvalue):
    data['GAME']['ROSTER']['KERBAL'][kerbNum][value] = newvalue

def renameSeq():
    global names
    global kerb
    new = input("Enter the new name of the kerbal >>>")
    rename(data,kerb,new)
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    names = [guy['name'] for guy in data['GAME']['ROSTER']['KERBAL']]
    kerb = names[kerbNum]
    optionSeq()

def stupidSeq():
    revalue(data,"dumb",input("Enter a decimal number from 0 to 1 for the stupidity value >>>"))
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    optionSeq()

def courageSeq():
    revalue(data,"brave",input("Enter a decimal number from 0 to 1 for the courage value >>>"))
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    optionSeq()

def badassSeq():
    revalue(data,"badS",tf[int(input("Enter 0 to set Badass to false enter, 1 to set it to true >>>"))])
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    optionSeq()

def veteranSeq():
    revalue(data,"veteran",tf[int(input("Enter 0 to set veteran to false, enter 1 to set it to true >>>"))])
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    optionSeq()

def genderSeq():
    revalue(data,"gender",mf[int(input("Enter 0 to set gender to male, enter 1 to set it to female >>>"))])
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    optionSeq()

def traitSeq():
    revalue(data,"trait",traits[int(input("Enter 0 to set trait to pilot, enter 1 to set it to engineer, enter 2 to set it to scientist >>>"))])
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    optionSeq()

def removeSeq():
    print("!WARNING! This will delete the kerbal entirely, this change is irreverisble")
    match input("Do you wish to continue? (y/n) >>>"):
        case "n":
            print("Kerbal not deleted")
            optionSeq()
        case "y":
            print("Kerbal has been deleted")
        case _:
            removeSeq()
    remove(data)
    exitSeq()

def exitSeq():
    sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")
    input("Done! Press enter to close.")
    sys.exit()

def optionSeq():
    for i in options:
        print("["+str(options.index(i))+"]"+i)
    optionChoice = int(input("Enter the option you want to edit >>>"))
    match optionChoice:
        case 0:
            renameSeq()
        case 1:
            #edit stupid
            stupidSeq()
        case 2:
            #edit corage
            courageSeq()
        case 3:
            #edit badS
            badassSeq()
        case 4:
            #edit vetran
            veteranSeq()
        case 5:
            #edit gender
            genderSeq()
        case 6:
            #edit trait
            traitSeq()
        case 7:
            removeSeq()
        case 8:
            exitSeq()
        case _:
            optionSeq()
    



optionSeq()