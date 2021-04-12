from nodes import*
from write import*
from parse import*
from log import*
from set_up import*


def main():
    count = int(input("How many config file do you want to make:\n"))
    msg = []
    while(count):
        tmp = setup()
        if(tmp == None or tmp == 0):
            url, airpot_name = get_url()
        else:
            tmp = tmp.split(',')
            url = tmp[0]
            airpot_name = tmp[1]
        filename = get_file_name()
        nodes, nodes_names = get_nodes(url)
        node_nums = len(nodes_names)
        edit_manage(filename, nodes, nodes_names)
        msg.append(get_msg(airpot_name,node_nums,url,filename+'.yaml')) 
        log(" [Info] airport: "+airpot_name+" get "+str(node_nums)+" nodes!")
        count -= 1
    flog(msg)
    
main()
        