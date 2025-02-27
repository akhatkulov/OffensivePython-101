import socket 
from termcolor import colored

######CONFIG######
socket.setdefaulttimeout(3)
##################

def port_scan(ip:str,ports):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IP manzil (v4) va TCP da aloqa shakllantirish
    for port in ports:
        if connection.connect_ex((ip,port)):
            print(colored("-{X}- " + str(port) +" port yopiq!","red"))
        else:
            print(colored("-{Y}- " + str(port) + " port ochiq :)","green"))
    
    connection.close()      

