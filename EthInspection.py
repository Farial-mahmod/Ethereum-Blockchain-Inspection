# Importing Web3 library
from web3 import Web3

# Place your infura API key
Infura_Connection = "https://mainnet.infura.io/v3/INFURA_KEY"

# Producing the connection to the blockchain
web3 = Web3(Web3.HTTPProvider(Infura_Connection))

# Checking protocol version
print(web3.eth.protocolVersion)

# Fetching the latest block
print(web3.eth.getBlock('latest'))

# Displaying coinbase
print(web3.eth.coinbase)

# Prints the current hashrate that is to be mined to add a block
print(web3.eth.hashrate)

# Checking if nodes are sycing properly or dead
print(web3.eth.syncing)

# fetching ChainID
print(web3.eth.chainId)

# Displaying block number
print(web3.eth.blockNumber)

# Input account key to get balance in Wei unit
myBalance = web3.eth.getBalance("YOUR_ACCOUNT")
print(myBalance)

# Current gas price in Wei unit
print(web3.eth.gasPrice)
