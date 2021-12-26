import multiprocessing as mp
import socket
import json
import sys
import os
import math
import cmath

SERVER = "192.168.56.101"
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)


def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num
    
def sendResult(conn,addr,result):
    result = formatNumber(result)
    result = str(result)
    conn.send(result.encode(FORMAT))
    print(f"[RESULT] THE RESULT HAS BEEN SENT TO THE CLIENT {addr}")

def sendQuadratic(conn,addr,result1,result2):
    result1 = str(result1)
    result2 = str(result2)
    quadraticList = [result1, result2]
    quadraticList = json.dumps(quadraticList)
    conn.sendall(bytes(quadraticList,encoding="utf-8"))
    print(f"[RESULT] THE RESULT HAS BEEN SENT TO THE CLIENT {addr}")


def addition(conn,addr,receive_msg):
    result = float(receive_msg[1]) + float(receive_msg[2])
    sendResult(conn,addr,result)

def substraction(conn,addr,receive_msg):
    result = float(receive_msg[1]) - float(receive_msg[2])
    sendResult(conn,addr,result)

def log(conn,addr,receive_msg):
    result = math.log(float(receive_msg[1]), float(receive_msg[2]))
    sendResult(conn,addr,result)

def squareRoot(conn,addr,receive_msg):
    result = math.sqrt(float(receive_msg[1]))
    sendResult(conn,addr,result)

def exponent(conn,addr,receive_msg):
    result = pow(float(receive_msg[1]), float(receive_msg[2]))
    sendResult(conn,addr,result)

def quadratic(conn,addr,receive_msg):
    d = (float(receive_msg[2])**2) - (4*float(receive_msg[1])*float(receive_msg[3]))
    result1 = (-float(receive_msg[2])-cmath.sqrt(d))/(2*float(receive_msg[1]))
    result2 = (-float(receive_msg[2])+cmath.sqrt(d))/(2*float(receive_msg[1]))
    sendQuadratic(conn,addr,result1,result2)

def cuboidVol(conn,addr,receive_msg):
    result = float(receive_msg[1])*float(receive_msg[2])*float(receive_msg[3])
    sendResult(conn,addr,result)

def sphereVol(conn,addr,receive_msg):
    pi=22/7
    result = (4/3) * (pi * float(receive_msg[1]) ** 3)
    sendResult(conn,addr,result)

def cylinderVol(conn,addr,receive_msg):
    pi=22/7
    result =  pi * float(receive_msg[1]) * float(receive_msg[1]) * float(receive_msg[2])
    sendResult(conn,addr,result)

def coneVol(conn,addr,receive_msg):
    pi=22/7
    result =  (1.0/3) * pi * float(receive_msg[1]) * float(receive_msg[1]) * float(receive_msg[2])
    sendResult(conn,addr,result)


def handle_client(conn,addr):
    try:
        try:
            print(f"[NEW CONNECTION] {addr} CONNECTED")
            connected = True
            while connected:
                receive_msg = conn.recv(2048).decode(FORMAT)
                if receive_msg:
                    receive_msg = json.loads(receive_msg)
                    if receive_msg == DISCONNECT_MESSAGE:
                        connected = False
                        print(f"[DISCONNECT] CLIENT {addr} HAS BEEN DISCONNECTED")
                        
                    if receive_msg[0] == "1":
                        addition(conn,addr,receive_msg)
                    elif receive_msg[0] == "2":
                        substraction(conn,addr,receive_msg)
                    elif receive_msg[0] == "3":
                        log(conn,addr,receive_msg)
                    elif receive_msg[0] == "4":
                        squareRoot(conn,addr,receive_msg)
                    elif receive_msg[0] == "5":
                        exponent(conn,addr,receive_msg)
                    elif receive_msg[0] == "6":
                        quadratic(conn,addr,receive_msg)
                    elif receive_msg[0] == "7":
                        cuboidVol(conn,addr,receive_msg)
                    elif receive_msg[0] == "8":
                        sphereVol(conn,addr,receive_msg)
                    elif receive_msg[0] == "9":
                        cylinderVol(conn,addr,receive_msg)
                    elif receive_msg[0] == "10":
                        coneVol(conn,addr,receive_msg)
            conn.close()
        except OverflowError:
            print("Overflow Error")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Server Has Been Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)    


def start():
    try:
        try:
            server.listen()
            try:
                while True:
                    try:
                        conn, addr = server.accept()
                        process = mp.Process(target=handle_client, args=(conn,addr))
                        process.start()
                    except socket.error:
                        print("Socket Error")
            except Exception as e:
                print("An Exception Has Occured:")
                print(e)
                sys.exit(1)
        except OverflowError:
            print("Overflow Error")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Server Has Been Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    print("[STARTING] SERVER IS STARTING")
    start()
