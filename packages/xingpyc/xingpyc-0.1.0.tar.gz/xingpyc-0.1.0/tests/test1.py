import socket
from multiprocessing import Process
from xingpyc import XClient

def i2i(file):
    print("i2i",file)
    return b"i2i"

def config(file):
    print("config",file)
    return b"hello from com test"

def run_comclient():
    XClient([i2i,config],"client", "ws://localhost:8888/com/","testuser.testuser")
    print("passed")

if __name__ == "__main__":
    
    comclient_process = Process(target=run_comclient, args=())

    comclient_process.start()

    comclient_process.join()
