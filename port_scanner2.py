
#port scanner
import socket
import subprocess
import sys
from datetime import datetime
from anonymous_tool import anonymousBrowser
subprocess.call('clear', shell=True) # clear the screen

def port_scanner():
    remoteServer = input('Enter the host name you wish to scan: ')
    remoteServerIP = socket.gethostbyname(remoteServer) #binding remoteServer to remoteServerIP

    print('#' * 15)
    print(f"Scanning of remoteServer {remoteServer}  has started ")
    t1 = datetime.now() 
    print('#' * 15)

    try:
        for port in range(1, 500):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = socket.connect(remoteServerIP, port)
            if result == 0:
                print('port {}: on IP address {}: is open'.format(port, remoteServerIP))
            else:
                print("port {}: on IP Address {}: is closed".format(port, remoteServerIP))
    except KeyboardInterrupt:
        print("You chose to quit the program ")
        print("quitting... ")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved ")
        print('exiting...')
        sys.exit()
    except socket.error:
        print("couldn't connect to server ")
        print("exiting...")
        sys.exit()

    t2 = datetime.now()
    timeTaken = t2 - t1

    print(f"Time taken to scan is {timeTaken} seconds ")


#checking if the useragents attribute exist
if hasattr(anonymousBrowser, 'user_agents'):
    print("The 'user_agents' attribute exists.")
else:
    print("The 'user_agents' attribute does not exist.")

ab = anonymousBrowser(proxies=[].\
    user_agents==[(user_agents + 'superSecretBrowser')]).\
    ab.anonymize()
if ab.anonymize():
    if True:
        print("*" * 5) 
        print('port scanning anonymized successfully' )
        print( 'running the port scanner')
        print("*" * 5)
        port_scanner()
        response = ab.open(remoteServer)
  

else:
    print("port scanner couldn't be established anonymously")
    print("You can still scan your host")
    user_input = input('press Y to continue or N to quit').lower()
    if user_input == 'y':
        port_scanner()

    elif user_input == 'n':
        print('exiting program ...')
        exit(2)
    else:
        KeyboardInterrupt = True
        while KeyboardInterrupt:
            print('keyboard interrupt detected')
            print('exiting program...')
            exit(2)


        








