from cgitb import reset
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
    print(f"{'-'*50}\nScanning target {target}\nTime started: {str(datetime.now())}\n{'-'*50}")

    try:
        for port in range(50, 85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
    except KeyboardInterrupt:
        print("\nExiting")
        sys.exit()
    except socket.gaierror:
        print("Failed to resolve hostname.")
        sys.exit()
    except socket.error:
        print("failed to connect to server.")
        sys.exit()
    finally:
        s.close()


if __name__ == "__main__":
    run()