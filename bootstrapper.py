import os
import subprocess as sub

CHANCOIN_BIN="/Users/Chazu/chan/chancoin-cash/build/bin/chancoin"

network_name = input("Network name: ")
node1_ip = input("Node 1 IP: ")
node2_ip = input("Node 2 IP: ")
node3_ip = input("Node 3 IP: ")

for node in (node1_ip, node2_ip, node3_ip):
    sub.run(f"mkdir -p {network_name}/{node}", shell=True)
    sub.run(f"{CHANCOIN_BIN} account new --chancoin-testnet --datadir=temp", shell=True)
    utc_name = os.listdir("./temp/keystore")[0]
    sub.run(f"mv ./temp/keystore/{utc_name} {network_name}/{node}/{utc_name}", shell=True)

# Create foundation address - move it into place
sub.run(f"{CHANCOIN_BIN} account new --chancoin-testnet --datadir=temp", shell=True)
utc_name = os.listdir("./temp/keystore")[0]
sub.run(f"mkdir -p {network_name}/foundation", shell=True)
sub.run(f"mv ./temp/keystore/{utc_name} {network_name}/foundation/{utc_name}", shell=True)

sub.run("rm -rf temp", shell=True)
# Delete temp_datadir
