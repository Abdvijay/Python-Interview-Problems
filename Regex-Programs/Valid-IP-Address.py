# Check if string is a valid IP address (IPv4)

# Input: "192.168.0.1" → Valid
# Input: "999.10.0.1" → Invalid

import re
Ip = input("Enter the IP Address : ")
pattern = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.|$)){4}$'
if re.match(pattern,Ip):
    print(f'IP - > {Ip} is Valid')
else:
    print(f'IP - > {Ip} is not Valid')