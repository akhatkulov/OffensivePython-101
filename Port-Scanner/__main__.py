#!usr/bin/python
from helper import port_scan 

target_ip = input("-{?}- IP4 manzilni bering: ")
mode = input("-{?}- Portlarni avto-generatsiya qilaymi? (y/n): ")

if mode == "y":
    port_scan(ip=target_ip,ports=list(range(1,65535+1)))
else:
    ports = list(map(int,input("-{?}- Portlarni kiriting: ").split()))
    port_scan(ip=target_ip,ports=ports)
