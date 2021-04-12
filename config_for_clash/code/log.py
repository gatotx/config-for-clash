import datetime,os

def log(msg):
    time = datetime.datetime.now()
    print('['+time.strftime('%Y.%m.%d-%H:%M:%S')+']:'+msg)

def flog(msg):
    msg = '\n\n'.join(msg)
    dirlog = os.path.dirname(os.path.dirname(__file__))+'\\log'
    if(not os.path.exists(dirlog)):
        os.mkdir(dirlog)
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename ='..\\log\\'+ time+".log"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(msg)

def get_msg(airpot_name,node_nums,url,name):
    return "airpot_name: "+airpot_name+"\nurl: "+url+"\nnode_nums: "+str(node_nums)+"\nconfig_file_name: "+name+"\n\n"