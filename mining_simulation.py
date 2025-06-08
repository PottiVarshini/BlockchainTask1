#Simulate Proof-of-Work by mining a block that satisfies a difficulty condition.
import hashlib
import time

class Block:
    def __init__(self,index,data,previous_hash):
        self.index=index
        self.timestamp=time.ctime()
        self.data=data
        self.previous_hash=previous_hash
        self.nonce=0
        self.hash=self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index)+self.timestamp+self.data+self.previous_hash+str(self.nonce)).encode()).hexdigest()

    def mine_block(self, difficulty):
        start_time=time.time()
        target='0'*difficulty
        while self.hash[:difficulty]!=target:
            self.nonce+=1
            self.hash=self.calculate_hash()
        end_time=time.time()
        print(f"Mined block with nonce {self.nonce} in {end_time - start_time:.2f} seconds. Hash: {self.hash}")
block = Block(0,"Mining Example","0")
block.mine_block(difficulty=4)