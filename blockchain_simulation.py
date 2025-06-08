# Build a basic blockchain with 3 linked blocks.
import hashlib
import time
class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index= index
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash
        self.nonce=0
        self.hash=self.calculate_hash()
    def calculate_hash(self):
        value = str(self.index)+self.timestamp+self.data+self.previous_hash+str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()
    def __str__(self):
        return f"Block #{self.index}\n Hash:{self.hash}\n Previous:{self.previous_hash}\n Data:{self.data}\n"
#Create Blockchain
block0 = Block(0,time.ctime(),"First Block","0")
block1 = Block(1,time.ctime(),"Second Block",block0.hash)
block2 = Block(2,time.ctime(),"Third Block",block1.hash)
blockchain = [block0, block1, block2]
#Display Blocks
for block in blockchain:
    print(block)
#Challenge-1
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()
#Challenge-2
print("\nAfter tampering:")
for block in blockchain:
    print(block)