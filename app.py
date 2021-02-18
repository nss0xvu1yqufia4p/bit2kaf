import time
import json
from bitcoinlib.services.bitcoind import BitcoindClient

base_url = 'http://rpcuser:lcjxjwzbvnkqwtcm@bitcoin-full-node-service:8332'
bdc = BitcoindClient(base_url=base_url)
txid = '63522845d294ee9b0188ae5cac91bf389a0c3723f084ca1025e7d9cdfe481ce1'
rt = bdc.getrawtransaction(txid)
print("Raw: %s" % rt)

lastblockread = 0

while(True):
    blockheight = bdc.blockcount()
    if lastblockread < blockheight:
        block = bdc.getblock(lastblockread, parse_transactions=False)
        print(json.dumps(block))
        lastblockread = lastblockread + 1
    print("looping...")
    time.sleep(2)
