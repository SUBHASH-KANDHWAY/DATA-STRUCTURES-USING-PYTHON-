from blockchain1 import block
import datetime

block_chain= [block.create_genesis_block()]

print(' THE GENESIS BLOCK HAS BEEN CREATED\n')
print("HASH:%s " %  block_chain[-1].hash)
no_ofblocks_add=10

for i in range(1,no_ofblocks_add + 1):
    block_chain.append(block(block_chain[-1].hash,'DATA!',
    datetime.datetime.now()))
    print()
    print("BLOCK %d HAS BEEN CREATED:" %i)
    print()
    
    print("BLOCKCHAIN::%d HASH:: %s" %(i,block_chain[1].hash))


print('all good till now')