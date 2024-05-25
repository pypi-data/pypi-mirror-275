from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
import asyncio
import json
import os
import websockets
from websockets.sync.client import connect
from websockets.server import serve
import time
import sys
import numpy as np

try:
    progress = SharedMemory(name="progress", create=True, size=1*8)
except FileExistsError:
    progress = SharedMemory(name="progress", create=False, size=1*8)

try:
    curClient = SharedMemory(name="curClient", create=True, size=1*8)
except FileExistsError:
    curClient = SharedMemory(name="curClient", create=False, size=1*8)

progressfloat = np.ndarray((1,), dtype=np.float64, buffer=progress.buf)
curClientint = np.ndarray((1,), dtype=np.int64, buffer=curClient.buf)

class ConsoleCapture:
    def write(self, text):
        # Capture the printed text
        if text == '\n':
            return
        if text[1:5]=="XING" :
            progressfloat[0]=float(text[15:])

        sys.stdout= sys.__stdout__
        print(text)
        sys.stdout = self

    def flush(self):
        pass
    
# Redirect sys.stdout to the custom stream
capture_stream = ConsoleCapture()
sys.stdout = capture_stream

class XClient:
    def __init__(self,funcs,mode: str, ip=None, port=None):
        '''
        init a ComClient with AI functions
        funcs: a list of AI functions
        '''
        self.server = None

        self.clients = {}
        self.clientsCFG = {}
        self.blockbuffers = {}

        if not os.path.exists("tasks"):
            os.mkdir("tasks")
        tasks = os.listdir("tasks")
        for task in tasks:
            os.remove(f"tasks/{task}")

        if not os.path.exists("results"):
            os.mkdir("results")
        results = os.listdir("results")
        for result in results:
            os.remove(f"results/{result}")

        for func in funcs:
            Process(target=add_listener, args=(func,)).start()
        #sending
        asyncio.get_event_loop().create_task(self.global_send())

        #listening
        if(mode == "server"):
            print("\033[93m Server started on "+ip+":"+str(port)+" \033[0m")
            asyncio.get_event_loop().run_until_complete(serve(self.asServer_onRecv, ip, port))

        elif(mode == "client"):
            print("\033[93m Client started \033[0m")
            asyncio.get_event_loop().create_task(self.connect_cloud(ip))
        
        asyncio.get_event_loop().run_forever()




    async def connect_cloud(self,ip):
        async with websockets.connect(ip) as websocket:
            print("\033[93m===========         Connected to the server         ============\033[0m")
            print("\033[93m===========         Connected to the server         ============\033[0m")
            print("\033[93m===========         Connected to the server         ============\033[0m")
            self.server_websocket = websocket
            try:
                while True:
                    message = await websocket.recv()
                    ###### -1 should be client id, change it later
                    await self.global_onRecv(-1, message)
            except websockets.ConnectionClosedError:
                print("Connection closed by the server")


    async def asServer_onRecv(self, websocket):

        client_id = id(websocket)
        print(f"Client {client_id} connected")
        try:
            async for message in websocket:
                self.clients[client_id] = websocket

                await self.global_onRecv(client_id, message)

        except Exception as e:
            print(f"Error in websocket communication: {e}")

    async def global_onRecv(self, client_id, message):
        '''
        WebSocket Object should NOT go inside here, only client_id and message
        
        '''
        print(
            "\033[93mheader:"+
            message[:10].replace(b"\x00", b"").decode()+
            "   id:"+
            message[10:20].decode()+
            "   length:"+
            str(len(message[20:]))+
            "\033[0m"
        )
        # connect client and save client id

        header = message[:10].replace(b"\x00", b"").decode()
        task_id = message[10:20]

        if client_id not in self.blockbuffers:
            self.blockbuffers[client_id] = []
        if client_id not in self.clientsCFG:
            self.clientsCFG[client_id] = {}

        content = message[20:]
        
        try:
            if header == "block":
                # if block, save it to buffer
                self.blockbuffers[client_id].append(content)
                return

            if client_id in self.blockbuffers:
                # if there is a block buffer, concat it
                self.blockbuffers[client_id].append(content)
                content = b"".join(self.blockbuffers[client_id])
                with open(f"tasks/{client_id}.{task_id.decode()}.{header}", "wb") as f:
                    f.write(content)
                del self.blockbuffers[client_id] # clean buffer

        except Exception as e:
            print(f"Error in websocket communication: {e}")
            return

    async def global_send(self):
        while True:
            if len(os.listdir("results")) > 0:
                for file in os.listdir("results"):
                    try:
                        with open(f"results/{file}", "rb") as f:
                            result_data = f.read()
                        os.remove(f"results/{file}")
                        content = result_data
                        client_id, task_id, header = file.split(".")
                        client_id = int(client_id)
                
                        header = (header + "0" * (10 - len(header))).encode("utf-8")
                        if isinstance(task_id, str):
                            task_id = task_id.encode("utf-8")
                        if isinstance(header, str):
                            header = header.encode("utf-8")
                        if isinstance(content, str):
                            content = content.encode("utf-8")
                        if client_id == -1:
                            await self.server_websocket.send(header + task_id + content)
                        else:
                            await self.asServer_send(client_id, header, task_id, content)

                        break # only send one result at a time
                    except Exception as e:
                        print(f"Error in sending message to websocket: {e}")
            else:
                await asyncio.sleep(0.1)

    async def asServer_send(self, client_id, header, task_id, content):
        websocket = self.clients.get(client_id)
        while len(content) > 0:
            if len(content) > 100000:
                await websocket.send(b"block00000" + task_id + content[0:100000])
                content = content[100000:]
            else:
                await websocket.send(header + task_id + content)
                content = b""
            await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)



def add_listener(callback, interval=0.1):
    while True:
        taskfiles = os.listdir("tasks")
        found = False
        try:
            for file in taskfiles:
                client_id, task_id, header = file.split(".")
                if header == callback.__name__:
                    found = True
                    res=callback("tasks/"+file)
                    os.remove("tasks/"+file)
                    assert type(res) == bytes, "Return type must be bytes"
                    if res is not None:
                        with open("results/"+file,"wb") as f:
                            f.write(res)
        except Exception as e:
            print(f"Error in interpreting task of {callback.__name__}: {e}")

        if found is None:
            time.sleep(interval)
            continue