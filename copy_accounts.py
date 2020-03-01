import ipaddress
import os
import subprocess as sub

network_name = input("Network name: ")

for ip in os.listdir(f"./{network_name}"):
    try:
        ipaddress.ip_address(ip)
        account_file = os.listdir(f"./{network_name}/{ip}")[0]
        command = (f"scp ./{network_name}/{ip}/{account_file} "
                   f"root@{ip}:~/.chancoin/keystore/{account_file}")
        print(command)
        sub.run(command, shell=True)
    except ValueError:
        print(f"Skipping {ip} - not a node IP")
