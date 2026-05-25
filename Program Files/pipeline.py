"""
Key Notes:
1) The pipeline.py contains the code which acts as the engine of the entire network pipeline.

"""

import asyncio
import socket 
import threading 


worker_1 = 1
worker_2 = 1
class Engine():
    def message():
        global worker_1,worker_2
        result = worker_1 + worker_2
        print("THE PIPELINE HAS STARTED SUCCESSFULLY")
        print("Thread Workers Initialized")
        print(f"{result} both workers are initialized")