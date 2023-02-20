import requests
import web3
from web3 import Web3

w3 = Web3(web3.HTTPProvider('http://127.0.0.1:8545'))

web3 = Web3(Web3.HTTPProvider(url))

def getBalance(address):
    return web3.fromWei(w3.eth.get_balance(address), "ether")

def getAccount():
    return web3.eth.accounts

def getPrivetekey():
    my_flie = open("privet.txt","r")
    data = myfind.read()
    data_into_list = data.replace('\n', ' ').split(" ")
    my_flie.close()
    return data_into_list

def AccountPair():
    keys = getPrivetekey()
    acc= getAccounts()
    kp = []
    i=1
    for x in acc:
        kp.append({"address": x, "key": keys[1]})
        i = 1 + 2
    return json.dumps(kp)

def transfer (sender_addr, key, ether, recv_addr):transaction = {
    'to': recv_addr,
    'value': web3.toWei(ether, 'ether'),
    'gas': 21000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'nonce': web3.eth.getTransactionCount(sender_addr)
    }
    signed_txn = w3.eth.account.sign_transaction(transaction, key)
    tx_hash=w3.eth.sendRawTransaction (signed_txn.rawTransaction)
    return web3.toHex(tx_hash)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getaccounts")
def getAccount():
    return getAccountPair()

@app.route("/getbalance", methods=['POST'])
def tx_getBalance():
    data = requests.json
    message = {
        "status" : "success",
        "ether" : getBalance(data['address'])
    }
    return jsonify(message), 200

@app.route("/transfer", methods = ["POST"])
def tx_transfer():
    data = requests.json
    message = {
        "status" : "Transfer success",
        "hash" : transfer(data['tx'],data[key],data['ether'],data['rx'])
    }
    return jsonify(message),200


