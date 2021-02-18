import time
from bitcoinlib.services.bitcoind import BitcoindClient

base_url = 'http://rpcuser:lcjxjwzbvnkqwtcm@bitcoin-full-node-service:8332'
bdc = BitcoindClient(base_url=base_url)
txid = '63522845d294ee9b0188ae5cac91bf389a0c3723f084ca1025e7d9cdfe481ce1'
rt = bdc.getrawtransaction(txid)
print("Raw: %s" % rt)

while(True):
    print("looping...")
    time.sleep(2)
