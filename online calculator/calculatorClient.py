import socket
import json
import sys
import os


SERVER = "192.168.56.101"
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def disconnect():
    msg = "!DISCONNECT"
    msg = json.dumps(msg)
    client.sendall(bytes(msg,encoding="utf-8"))

def send_recv(lists):
    lists = json.dumps(lists)
    client.sendall(bytes(lists,encoding="utf-8"))
    receive_msg = client.recv(2048).decode(FORMAT)
    if receive_msg:
        print(f"[SERVER] RESULT: {receive_msg}")
    else:
        print("[SERVER]: SERVER DOWN")

def send_recv_quadratic(lists):
    lists = json.dumps(lists)
    client.sendall(bytes(lists,encoding="utf-8"))
    receive_msg = client.recv(2048).decode(FORMAT)
    if receive_msg:
        receive_msg = json.loads(receive_msg)
        print(f"[SERVER] RESULT: Solution 1: {receive_msg[0]}\nSolution 2: {receive_msg[1]}")
    else:
        print("[SERVER]: SERVER DOWN")

def checkNumber(num):
    try:
        int(num)
        check = "correct"
        return check
    except ValueError:
        try:
            float(num)
            check = "correct"
            return check
        except ValueError:
            check = "incorrect"
            return check

def checkLog(num):
    if float(num) <= 0:
        log = "incorrect"
        return log
    else:
        log = "correct"
        return log

def checkRoot(num):
    if float(num) < 0:
        root = "incorrect"
        return root
    else:
        root = "correct"
        return root

def checkExponent(x,y):
    if float(x) == 0:
        if float(y) <= 0:
            expo = "incorrect"
            return expo
        else:
            expo = "correct"
            return expo
    elif float(x) < 0:
        if float(y).is_integer():
            expo = "correct"
            return expo
        else:
            expo = "incorrect"
            return expo

def checkVol(num):
    if float(num) < 0:
        vol = "incorrect"
        return vol
    else:
        vol = "correct"
        return vol

def addition(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect":
                x = input("Enter First Number: ")
                check1 = checkNumber(x)
                
            check2 = "incorrect"    
            while check2 == "incorrect":
                y = input("Enter Second Number: ")
                check2 = checkNumber(y) 
                
            lists = [operation,x,y]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0) 

def log(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect" or log1 == "incorrect":
                x = input("Enter Number: ")
                check1 = checkNumber(x)
                if check1 == "correct":
                    log1 = checkLog(x)
                
            check2 = "incorrect"    
            while check2 == "incorrect" or log2 == "incorrect":
                y = input("Enter Log Base: ")
                check2 = checkNumber(y) 
                if check2 == "correct":
                    log2 = checkLog(y)
                
            lists = [operation,x,y]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0) 

def squareRoot(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect" or root1 == "incorrect":
                x = input("Enter Number: ")
                check1 = checkNumber(x)
                if check1 == "correct":
                    root1 = checkRoot(x)

            lists = [operation,x]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def exponent(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect":
                x = input("Enter Number: ")
                check1 = checkNumber(x)
            
            check2 = "incorrect"
            while check2 == "incorrect" or expo == "incorrect": 
                y = input("Enter Exponent: ")
                check2 = checkNumber(y)
                if check2 == "correct":
                    expo = checkExponent(x,y)

            lists = [operation,x,y]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def quadratic(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect":
                a = input("Enter a: ")
                check1 = checkNumber(a)
                
            check2 = "incorrect"    
            while check2 == "incorrect":
                b = input("Enter b: ")
                check2 = checkNumber(b) 
            
            check3 = "incorrect"    
            while check3 == "incorrect":
                c = input("Enter c: ")
                check3 = checkNumber(c) 
                
            lists = [operation,a,b,c]
            send_recv_quadratic(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0) 

def cuboidVol(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect" or vol1 == "incorrect":
                length = input("Enter Length: ")
                check1 = checkNumber(length)
                if check1 == "correct":
                    vol1 = checkVol(length)
                
            check2 = "incorrect"    
            while check2 == "incorrect" or vol2 == "incorrect":
                width = input("Enter Width: ")
                check2 = checkNumber(width) 
                if check2 == "correct":
                    vol2 = checkVol(width)
            
            check3 = "incorrect"    
            while check3 == "incorrect" or vol3 == "incorrect":
                height = input("Enter Height: ")
                check3 = checkNumber(height) 
                if check3 == "correct":
                    vol3 = checkVol(height)
                
            lists = [operation,length,width,height]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def sphereVol(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect" or vol1 == "incorrect":
                x = input("Enter Radius: ")
                check1 = checkNumber(x)
                if check1 == "correct":
                    vol1 = checkVol(x)

            lists = [operation,x]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)  

def cylinderVol(operation):
    try:
        try:
            check1 = "incorrect"
            while check1 == "incorrect" or vol1 == "incorrect":
                x = input("Enter Radius: ")
                check1 = checkNumber(x)
                if check1 == "correct":
                    vol1 = checkVol(x)
            
            check2 = "incorrect"
            while check2 == "incorrect" or vol2 == "incorrect":
                y = input("Enter Height: ")
                check2 = checkNumber(y)
                if check2 == "correct":
                    vol2 = checkVol(y)

            lists = [operation,x,y]
            send_recv(lists)
        
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0) 

if __name__ == "__main__":
    try:
        try:
            operation = "hai"
            while operation != "11":
                print("1. Addition of 2 numbers\n2. Substraction of 2 numbers\n3. Logarithmic\n4. Square Root\n5. Exponential\n6. Quadratic Equation\n7. Cuboid Volume\n8. Sphere Volume\n9. Cylinder Volume\n10. Cone Volume\n11. Exit")
                operation = input("Please Select Math Operation: ")
                if operation == "1":
                    addition(operation)
                elif operation == "2":
                    addition(operation)
                elif operation == "3":
                    log(operation)
                elif operation == "4":
                    squareRoot(operation)
                elif operation == "5":
                    exponent(operation) 
                elif operation == "6":
                    quadratic(operation)
                elif operation == "7":
                    cuboidVol(operation)
                elif operation == "8":
                    sphereVol(operation) 
                elif operation == "9":
                    cylinderVol(operation)
                elif operation == "10":
                    cylinderVol(operation)              
                elif operation == "11":
                    disconnect()
        except BrokenPipeError:
            print("Server down")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)    
    

                
           
            
        
        
            

       
        