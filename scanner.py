import sys
import socket
from datetime import datetime

#our target

def run() -> None:
    if len(sys.argv) != 2:
        print("Invalid no. of arguments.")
        print("SYNTAX: scanner.py <ip>")
        return
    target = socket.gethostbyname(sys.argv[1])

    #Add banner
    print(f"{'-'*50}\nScanning target {target}\nTime started: {str(datetime.now())}")

if __name__ == "__main__":
    run()