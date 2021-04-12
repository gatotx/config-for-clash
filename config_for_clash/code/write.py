from log import log
import os

class SelectError(Exception):
    "this is user's Exception for check the length of name "

def write_header(fyaml):
    header_Str = "#http 和socks5 端口\nport: 7890\nsocks-port: 7891\n\nmode: Rule\nlog-level: debug\nexternal-controller: 127.0.0.1:9090\n\n"
    fyaml.write(header_Str)
    log(" [config_file] header successed to write!")

def dns_model(fyaml):
    dns_Str = "dns:\n  enable: true\n  listen: 127.0.0.1:5450\n  enhanced-mode: redir-host\n  default-nameserver:\n    - 119.29.29.29\n    - 119.28.28.28\n    - 1.0.0.1\n    - 208.67.222.222\n    - 1.2.4.8\n  nameserver:\n    - https://dns.alidns.com/dns-query\n    - https://1.1.1.1/dns-query\n    - tls://dns.adguard.com:853\n"
    fyaml.write(dns_Str)
    log(" [config_file] dns successed to write!")

def tun_model(fyaml):
    tun_Str = "  interface-name: WLAN # 出口网卡名称，或者使用下方的自动检测\n  \ntun:\n  enable: true\n  stack: gvisor\n  dns-hijack:\n    - 198.18.0.2:53\n  macOS-auto-route: true\n  macOS-auto-detect-interface: true # 自动检测出口网卡\n"
    fyaml.write(tun_Str)
    log(" [config_file] tun successed to write!")

def write_proxies(fyaml, nodes):
    nodes = '\n'.join(nodes)
    header_Str = "#在此导入所有节点\nproxies:\n"
    print("%s%s"%(header_Str, nodes), file = fyaml)
    log(" [config_file] nodes successed to write!")

def write_proxies_group(fyaml, nodes_names):
    nodes_names = '\n'.join(nodes_names)
    header_Str = "\nproxy-groups:\n\n# > 🌲main_proxy\n- name: 🌲main_proxy\n  type: select\n  proxies:\n    - DIRECT\n    - REJECT\n    - 🖱️select\n    - 💻auto_select\n"
    select = "\n# > 🖱️select\n- name: 🖱️select\n  type: select\n  proxies:\n"
    auto_select = "\n# > 💻auto_select\n- name: 💻auto_select\n  type: url-test\n  proxies:\n"
    url_tail = "\n  url: 'http://www.gstatic.com/generate_204'\n  interval: 600"
    groups = "\n# > 📺BiliBili\n- name: 📺BiliBili\n  type: select\n  proxies:\n    - DIRECT\n    - REJECT\n    - 💻auto_select\n    - 🖱️select\n\n# > 🛢️Youtube\n- name: 🛢️Youtube\n  type: select\n  proxies:\n    - DIRECT\n    - REJECT\n    - 💻auto_select\n    - 🖱️select\n\n# > 🕹️Steam\n- name: 🕹️Steam\n  type: select\n  proxies:\n    - DIRECT\n    - REJECT\n    - 💻auto_select\n    - 🖱️select\n"
    print("%s%s%s%s%s%s%s"%(header_Str,select,nodes_names,auto_select,nodes_names,url_tail,groups), file=fyaml)
    log(" [config_file] proxies_group successed to write!")
    
def write_rules(fyaml):
    rule_providers = 'rule-providers:\n  reject:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt"\n    path: ./ruleset/reject.yaml\n    interval: 86400\n\n  icloud:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/icloud.txt"\n    path: ./ruleset/icloud.yaml\n    interval: 86400\n\n  apple:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/apple.txt"\n    path: ./ruleset/apple.yaml\n    interval: 86400\n\n  google:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/google.txt"\n    path: ./ruleset/google.yaml\n    interval: 86400\n\n  proxy:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt"\n    path: ./ruleset/proxy.yaml\n    interval: 86400\n\n  direct:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt"\n    path: ./ruleset/direct.yaml\n    interval: 86400\n\n  private:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/private.txt"\n    path: ./ruleset/private.yaml\n    interval: 86400\n\n  gfw:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/gfw.txt"\n    path: ./ruleset/gfw.yaml\n    interval: 86400\n\n  greatfire:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/greatfire.txt"\n    path: ./ruleset/greatfire.yaml\n    interval: 86400\n\n  tld-not-cn:\n    type: http\n    behavior: domain\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/tld-not-cn.txt"\n    path: ./ruleset/tld-not-cn.yaml\n    interval: 86400\n\n  telegramcidr:\n    type: http\n    behavior: ipcidr\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/telegramcidr.txt"\n    path: ./ruleset/telegramcidr.yaml\n    interval: 86400\n\n  cncidr:\n    type: http\n    behavior: ipcidr\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt"\n    path: ./ruleset/cncidr.yaml\n    interval: 86400\n\n  lancidr:\n    type: http\n    behavior: ipcidr\n    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt"\n    path: ./ruleset/lancidr.yaml\n    interval: 86400\n'   
    rules = "\nrules:\n\n#📺BiliBili\n  - DOMAIN,upos-hz-mirrorakam.akamaized.net,📺BiliBili\n  - DOMAIN-SUFFIX,acg.tv,📺BiliBili\n  - DOMAIN-SUFFIX,acgvideo.com,📺BiliBili\n  - DOMAIN-SUFFIX,b23.tv,📺BiliBili\n  - DOMAIN-SUFFIX,bigfun.cn,📺BiliBili\n  - DOMAIN-SUFFIX,bigfunapp.cn,📺BiliBili\n  - DOMAIN-SUFFIX,biliapi.com,📺BiliBili\n  - DOMAIN-SUFFIX,biliapi.net,📺BiliBili\n  - DOMAIN-SUFFIX,BiliBili.com,📺BiliBili\n  - DOMAIN-SUFFIX,BiliBili.tv,📺BiliBili\n  - DOMAIN-SUFFIX,biligame.com,📺BiliBili\n  - DOMAIN-SUFFIX,biligame.net,📺BiliBili\n  - DOMAIN-SUFFIX,bilivideo.com,📺BiliBili\n  - DOMAIN-SUFFIX,hdslb.com,📺BiliBili\n  - DOMAIN-SUFFIX,im9.com,📺BiliBili\n  - DOMAIN-SUFFIX,smtcdns.net,📺BiliBili\n\n #🛢️Youtube\n  - DOMAIN-KEYWORD,Youtube,🛢️Youtube\n  - DOMAIN,Youtubei.googleapis.com,🛢️Youtube\n  - DOMAIN,yt3.ggpht.com,🛢️Youtube\n  - DOMAIN-SUFFIX,googlevideo.com,🛢️Youtube\n  - DOMAIN-SUFFIX,gvt2.com,🛢️Youtube\n  - DOMAIN-SUFFIX,youtu.be,🛢️Youtube\n  - DOMAIN-SUFFIX,Youtube.com,🛢️Youtube\n  - DOMAIN-SUFFIX,ytimg.com,🛢️Youtube\n\n  # > 🕹️Steam\n  - DOMAIN-SUFFIX,fanatical.com,🕹️Steam\n  - DOMAIN-SUFFIX,humblebundle.com,🕹️Steam\n  - DOMAIN-SUFFIX,Steamcommunity.com,🕹️Steam\n  - DOMAIN-SUFFIX,Steampowered.com,🕹️Steam\n  - DOMAIN-SUFFIX,Steamstatic.com,🕹️Steam\n  - DOMAIN-SUFFIX,Steambroadcast.akamaized.net,🕹️Steam\n  - DOMAIN-SUFFIX,Steamcdn-a.akamaihd.net,🕹️Steam\n  - DOMAIN-SUFFIX,Steamcommunity-a.akamaihd.net,🕹️Steam\n  - DOMAIN-SUFFIX,Steamstore-a.akamaihd.net,🕹️Steam\n  - DOMAIN-SUFFIX,Steamusercontent-a.akamaihd.net,🕹️Steam\n  - DOMAIN-SUFFIX,Steamuserimages-a.akamaihd.net,🕹️Steam\n\n\n #🌲main_proxy\n  - DOMAIN-KEYWORD,dualstack.apiproxy-device-prod-nlb-,🌲main_proxy\n  - DOMAIN-KEYWORD,dualstack.ichnaea-web-,🌲main_proxy\n  - DOMAIN,Netflix.com.edgesuite.net,🌲main_proxy\n  - DOMAIN-SUFFIX,fast.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflix.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflix.net,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest0.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest1.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest2.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest3.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest4.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest5.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest6.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest7.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest8.com,🌲main_proxy\n  - DOMAIN-SUFFIX,Netflixdnstest9.com,🌲main_proxy\n  - DOMAIN-SUFFIX,nflxext.com,🌲main_proxy\n  - DOMAIN-SUFFIX,nflximg.com,🌲main_proxy\n  - DOMAIN-SUFFIX,nflximg.net,🌲main_proxy\n  - DOMAIN-SUFFIX,nflxso.net,🌲main_proxy\n  - DOMAIN-SUFFIX,nflxvideo.net,🌲main_proxy\n  - IP-CIDR,8.41.4.0/24,🌲main_proxy,no-resolve\n  - IP-CIDR,23.246.0.0/18,🌲main_proxy,no-resolve\n  - IP-CIDR,34.210.42.111/32,🌲main_proxy,no-resolve\n  - IP-CIDR,37.77.184.0/21,🌲main_proxy,no-resolve\n  - IP-CIDR,38.72.126.0/24,🌲main_proxy,no-resolve\n  - IP-CIDR,45.57.0.0/17,🌲main_proxy,no-resolve\n  - IP-CIDR,52.89.124.203/32,🌲main_proxy,no-resolve\n  - IP-CIDR,54.148.37.5/32,🌲main_proxy,no-resolve\n  - IP-CIDR,64.120.128.0/17,🌲main_proxy,no-resolve\n  - IP-CIDR,66.197.128.0/17,🌲main_proxy,no-resolve\n  - IP-CIDR,69.53.224.0/19,🌲main_proxy,no-resolve\n  - IP-CIDR,103.87.204.0/22,🌲main_proxy,no-resolve\n  - IP-CIDR,108.175.32.0/20,🌲main_proxy,no-resolve\n  - IP-CIDR,185.2.220.0/22,🌲main_proxy,no-resolve\n  - IP-CIDR,185.9.188.0/22,🌲main_proxy,no-resolve\n  - IP-CIDR,192.173.64.0/18,🌲main_proxy,no-resolve\n  - IP-CIDR,198.38.96.0/19,🌲main_proxy,no-resolve\n  - IP-CIDR,198.45.48.0/20,🌲main_proxy,no-resolve\n  - IP-CIDR,207.45.72.0/22,🌲main_proxy,no-resolve\n  - IP-CIDR,208.75.76.0/22,🌲main_proxy,no-resolve\n\n# > Microsoft\n#  -  USER-AGENT,OneDrive,🌲main_proxy\n  -  DOMAIN-KEYWORD,onedrive,🌲main_proxy\n  -  DOMAIN-SUFFIX,azure.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,fabric.io,🌲main_proxy\n  -  DOMAIN-SUFFIX,files.1drv.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,hotmail.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,live.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,live.net,🌲main_proxy\n  -  DOMAIN-SUFFIX,livefilestore.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,mesh.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,microsoft.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,microsoftonline.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,microsoft-tst.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,msn.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,office.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,office.net,🌲main_proxy\n  -  DOMAIN-SUFFIX,onedrive.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,outlook.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,p.sfx.ms,🌲main_proxy\n  -  DOMAIN-SUFFIX,s-microsoft.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,sharepoint.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,skype.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,spoprod-a.akamaihd.net,🌲main_proxy\n  -  DOMAIN-SUFFIX,storage.msn.com,🌲main_proxy\n\n# > Telegram\n  -  DOMAIN-SUFFIX,t.me,🌲main_proxy\n  -  DOMAIN-SUFFIX,tdesktop.com,🌲main_proxy\n  -  DOMAIN-SUFFIX,telegra.ph,🌲main_proxy\n  -  DOMAIN-SUFFIX,PROXY.me,🌲main_proxy\n  -  DOMAIN-SUFFIX,PROXY.org,🌲main_proxy\n  -  IP-CIDR,91.108.0.0/16,🌲main_proxy,no-resolve\n  -  IP-CIDR,109.239.140.0/24,🌲main_proxy,no-resolve\n  -  IP-CIDR,149.154.160.0/20,🌲main_proxy,no-resolve\n  -  IP-CIDR6,2001:67c:4e8::/48,🌲main_proxy,no-resolve\n  -  IP-CIDR6,2001:b28:f23d::/48,🌲main_proxy,no-resolve\n  -  IP-CIDR6,2001:b28:f23f::/48,🌲main_proxy,no-resolve\n\n\n# > Speed Test by Cloudflare\n  -  DOMAIN-SUFFIX,speed.cloudflare.com,🌲main_proxy\n\n# > YiYo\n  #- IP-CIDR,239.255.255.250,🌲main_proxy\n  - DOMAIN-SUFFIX, yiyo.io, 🌲main_proxy\n\n# > Duyao\n  - DOMAIN-SUFFIX,duyaoss.com, 🌲main_proxy\n  \n# > shuchong\n  - DOMAIN-SUFFIX, shuchong.info, DIRECT\n\n# > oj\n  - DOMAIN-SUFFIX, vjudge.net, 🌲main_proxy\n  - DOMAIN-SUFFIX, onlinejudge.org,🌲main_proxy\n\n# > qidian international\n  - DOMAIN-SUFFIX,webnovel.com,🌲main_proxy\n\n# > rules-provider\n  - RULE-SET,private,DIRECT\n  - RULE-SET,reject,REJECT\n  - RULE-SET,icloud,DIRECT\n  - RULE-SET,apple,DIRECT\n  - RULE-SET,google,DIRECT\n  - RULE-SET,proxy,🌲main_proxy\n  - RULE-SET,direct,DIRECT\n  - RULE-SET,telegramcidr,🌲main_proxy\n  - GEOIP,,DIRECT\n  - GEOIP,CN,DIRECT\n\n\n\n# > match\n  - MATCH,🌲main_proxy\n"
    print(rule_providers, rules,file=fyaml)
    log(" [config_file] rules successed to write!")

def del_original():
    l = os.listdir('..\\')
    for i in l:
        if(".yaml" in i):
            os.remove("..\\"+i)    

def edit_manage(name, nodes, nodes_names):
    log(" [Info] start to write config file!")
    del_original()
    while(True):
        try:
            dns = int(input('Turn on dns model? "1" for Yes, "0" for No.\n'))
            tun = int(input('Turn on tun model? "1" for Yes, "0" for No.\n'))
            if(not dns and tun): raise SelectError
            else: break
        except(SelectError):    
            log(" [WARN] if you want turn on tun model, you should turn on dns model first!")
    name = "..\\"+name
    with open(name+'.yaml', "a+", encoding="utf-8") as fyaml:
        write_header(fyaml)
        if(dns): dns_model(fyaml)
        if(tun): tun_model(fyaml)
        write_proxies(fyaml, nodes)
        write_proxies_group(fyaml, nodes_names)
        write_rules(fyaml)
    log(" [Info] config file successed to make!")    
 

""" 
with open("nodes_2.out", "r", encoding="utf-8") as fin:
    nodes = fin.read()
with open("nodes_names_2.out", "r", encoding="utf-8") as fin:
    nodes_names = fin.read()

edit_manage('test', nodes, nodes_names)
"""





''' 

fout = open("tmp.out", "w",encoding='utf-8')

with open("tmp.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        print(line+'\\n', end = '', file=fout)

fout.close()
'''


