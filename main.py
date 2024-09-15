import sfsutils
import os
path = open("path.txt", "r").readline()
savelist = os.listdir(path)
for i in savelist:
    print("["+str(savelist.index(i))+"]"+i)
save = int(input("Enter the number of the save you want to edit. >>>"))
data = sfsutils.parse_savefile(path+savelist[save]+"/persistent.sfs")

def rename(data, oldname, newname):
    names = [guy['name'] for guy in data['GAME']['ROSTER']['KERBAL']]
    try:
        idx = names.index(oldname)
    except ValueError:
        print("Kerbal '%s' does not exist" % oldname)
        return
    data['GAME']['ROSTER']['KERBAL'][idx]['name'] = newname

old = input("Enter the curent name of the kerbal >>>")
new = input("Enter the new name of the kerbal >>>")
rename(data,old,new)
sfsutils.writeout_savefile(data, destination_file=path+savelist[save]+"/persistent.sfs")

input("Done! Press enter to close.")
exit()