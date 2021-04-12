import json,os
from log import log

def prerun():
    if(os.path.exists("archives.json")):
        archives = get_archives()
        if(archives == {}): print("Your archive file are empty")
        else: print("You do have some archives, do you want to modify them?")
        judge = int(input("type 1 to add or change, 2 to del, 0 for no action:\n"))
        if(judge == 1):
            archives = ac_archives(archives)
            save_to_file(archives)
        elif(judge == 2):
            archives = del_archives(archives)
            save_to_file(archives)
    else:
        print("It seems that you don't have any archives.")
        flag = int(input("Do you want to create a archive file? type 1 for yes 0 for no:\n"))
        if(flag == 1):
            with open("archives.json", "w", encoding="utf-8") as f:
                archives = {}
                archives = ac_archives(archives)
                save_to_file(archives)
        else: archives = None
    return archives
            
def ac_archives(archives):
    log(" [Info] start to modify archives file!")
    num = int(input("How many airpots do you want to modify\n"))
    ac_dict ={}
    for i in range(0, num):
        key = input("input your airpot name:\n")
        url = input("input the corresponding url:\n")
        if(key in archives.keys()):
            print("This action will change the url of airpot \"%s\", would you like to continue?"%key)
            con = intput("type 1 for continue, 2 for not:\n")
            if(con != '1'): continue
        ac_dict[key] = url
    for key in ac_dict:
        archives[key] = ac_dict[key]
    log(" [Info] modification has done!")
    return archives

def del_archives(archives):
    log(" [Info] start to delete archives file!")
    num = int(input("How many airpots do you want to delete?\n"))
    del_list = []
    key_list = list(archives.keys())
    printInfo(archives)
    for i in range(0, num):
        n = int(input("Type the serial number of the airport you want to delete:\n"))
        del_list.append(key_list[n-1])
    for key in del_list:
        del archives[key]
    log(" [Info] delete task has done!")
    return archives

def get_archives():
    with open("archives.json", "r", encoding="utf-8") as f:
        archives = json.load(f)
    return archives

def save_to_file(archives):
    with open("archives.json", "w+", encoding="utf-8") as f:
        json.dump(archives, f)
    log(" [Info] archive file has been saved")

def printInfo(archives):
    print("\nYou have %d airports in total and their names are below."%len(archives))
    i = 1
    for key in archives.keys():
        print("%d. %s"%(i, key))
        i += 1
    print()

def setup():
    archives = prerun()
    if(archives == None):
        return 0
    printInfo(archives)
    print("Would you like to use the airports above?")
    flag = int(input("type 1 for Yes, 0 for NO:\n"))
    if(flag):
        pos = int(input("Type the serial number of the airport you want to choose:\n"))
        key = list(archives.keys())[pos-1]
        return str(archives[key])+","+str(key)