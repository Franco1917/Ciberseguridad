from datetime import datetime
import json
import requests
import sys
import socket 

print("-" * 60)  
print("Comienza el escaneo:" + str(datetime.now())) 
print("-" * 60)

data = []
ipRange = "192.168.0."
ports = [21, 22, 25, 53, 79, 80, 110, 443, 8080, 9050]

try:
    for host in range(1, 254):
        for port in ports: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            s.settimeout(1)
            target = ipRange + str(host)
            result = s.connect_ex((target,port))
            print(target,":",port)
            if result == 0: 
                banner = s.recv(1024)
                banner = banner.decode("utf-8")
                data.append({'ip': target, 'port': port, 'banner':banner})
            s.close()
    print(data)

    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)

    payload = json.dumps(data)
    
    try:
        response = requests.post('http://127.0.0.1/example/fake_url.php', json=payload)
    except:
        print("No se pudo acceder al servidor.")

except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
except socket.gaierror: 
    print("\nHostname Could Not Be Resolved") 
    sys.exit() 
except socket.error: 
    print("\nServer not responding") 
    sys.exit() 