import requests, base64
import parse as p
from log import*

def get_data(url):
    log(" [Info] start to download data!")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    response = requests.get(url, headers = headers)
    if(response.status_code == 200):
        data = base64.b64decode(response.text).decode().splitlines()
        length = len(data)
        log(" [Info] Success to get "+str(length)+" nodes!")
    else:
        log(" [Info] Get data failed!")
    return data

def decode_data(data):
    nodes = []
    nodes_names = []
    serial = 0
    for i in data:
        serial += 1
        if("vmess:" in i):
            node, node_name = p.vmess_parse(i,serial)
            nodes.append(node),nodes_names.append(node_name)
        elif("ss:" in i and "vless:" not in i):
            node, node_name = p.ss_parse(i,serial)
            nodes.append(node),nodes_names.append(node_name)
        elif("trojan:" in i):
            node, node_name = p.trojan_parse(i,serial)
            nodes.append(node),nodes_names.append(node_name)
    log(" [Info] Parse has completed!")
    return nodes, nodes_names

def get_nodes(url):
    data = get_data(url)
    nodes, nodes_names = decode_data(data)
    return nodes, nodes_names

def get_url():
    url = input("input your url:\n")
    airpot_name = input("create a name for this url:\n")
    log(" [Info] successed to get url")
    return url, airpot_name
