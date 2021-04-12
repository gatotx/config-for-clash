import urllib.parse, json, base64,datetime
from log import*

def get_file_name():
    flag = int(input("if you want to name the config file type 1 else type 2:\n"))
    if(flag == 1):
        name = input("type your file name!(not included \".yaml\")\n")
    else:
        time = datetime.datetime.now().strftime('%m%d%H%M')
        name = time
    log(" [Info] successed to get file name!")
    return name

def pretmt(string,):
    string = urllib.parse.unquote(string)
    flag = 0
    if('#' in string):
        name = string[string.find('#')+1:]
        string = string[:string.find('#')]
        flag = 0
    string = string[string.find("//")+2:]
    string = base64.b64decode(string).decode()
    if(flag):
        return string,name,flag
    else:
        name = ""
        return string,name,flag

def retmt(node):
    node_name = '    - "'+node["name"]+'"'
    node = '  - '+str(node)
    return node,node_name

def vmess_parse(string, serial):
    vmessStr, name, flag = pretmt(string)
    vmessStr = json.loads(vmessStr)
    node = {
        "name":vmessStr["add"]+str(serial),
        "type":"vmess",
        "server":vmessStr["add"],
        "port":vmessStr["port"],
        "uuid":vmessStr["id"],
        "alterId":vmessStr["aid"],
        "cipher":vmessStr["type"],
        "network":vmessStr["net"] if vmessStr["net"] and vmessStr["net"] != "tcp" else None,
        "tls":True if vmessStr["tls"] == "tls" else None,
        "ws-path":vmessStr["path"] if vmessStr["path"] else None
    }
    #if(flag): node["name"] = name
    if(node["name"] == '' or node["name"] == None):
        node["name"] = node["server"]
    for key in list(node.keys()):
        if(node[key]) == None: del node[key]
    node, node_name = retmt(node)
    return node, node_name

def ss_parse(string,serial):
    ssStr, name, flag = pretmt(string)
    cipher = ssStr[:ssStr.find(':')]
    ssStr = ssStr[ssStr.find(':')+1:]
    password = ssStr[:ssStr.find('@')]
    ssStr = ssStr[ssStr.find('@')+1:]
    server = ssStr[:ssStr.find(':')]
    port = ssStr[ssStr.find(':')+1:]
    node ={
        "name": server+str(serial),  #name if(flag)else server,
        "server":server,
        "port":port,
        "type":"ss",
        "cipher":cipher,
        "password": password
    }    
    node, node_name = retmt(node)
    return node,node_name

def trojan_parse(string,serial):
    string = urllib.parse.unquote(string)
    trStr = string[string.find("//")+2:]
    password = trStr[:trStr.find('@')]
    trStr = trStr[trStr.find('@')+1:]
    sni = trStr[:trStr.find(':')]
    trStr = trStr[trStr.find(':')+1:]
    port = trStr[:trStr.find('#')]
    name = trStr[trStr.find('#')+1:]
    node = {
        "name":name+str(serial),
        "server":sni,
        "port":port,
        "type":"trojan",
        "password":password,
        "sni":sni
    }
    node,node_name = retmt(node)
    return node,node_name

def vless_parse(string):
    string = urllib.parse.unquote(string)
    vlStr = string[string.find('//')+2:]
    print(vlStr)

#string = "vless://2cfe82ea-8888-11eb-b2af-560003419c5e@xibun.gq:443?encryption=none&security=tls&type=tcp&headerType=none#%e4%ba%8c%e7%88%b7%e7%bf%bb%e5%a2%99%e7%bd%91+https%3a%2f%2f1808.ga"

#vless_parse(string)
""" 
node, node_name = trojan_parse(string)

print(node)
print(node_name)
"""
