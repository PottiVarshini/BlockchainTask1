# Theoretical Part:
## 1.Blockchain Basics
  ### -Define blockchain:
    A blockchain is a decentralized and digital ledger used to record transactions in a secure,transparent,and permanent way.It consists of a chain of      blocks,where each block contains a group of transactions,a timestamp,a reference(hash) to the previous block,and a unique cryptographic hash of its     own.All These blocks are linked together in chronological order,making it nearly impossible to alter past records without changing all subsequent       blocks.It operates on a peer-to-peer network without central control.
  ### -List 2 real-life use cases:
     1.Supply Chain Management-
          In real time Blockchain enables companies to track the journey of products from origin to destination.For example,in the food industry,it                  helps monitor freshness,prevent fraud,and ensure product authenticity by recording every step on a tamper-proof ledger.
     2.Digital Identity Verification
          Blockchain can store and verify personal identities securely.Instead of relying on centralized databases prone to hacking,individuals can                  control and share their identity data(like Aadhaar,passport info,or academic certificates)via blockchain, reducing the risk of identity                    theft and simplifying KYC (Know Your Customer) processes.
## 2.Block Anatomy
  ### -Draw a block showing:data,previous hash,timestamp,nonce,and Merkle root
     BLOCK
     Timestamp     : 2025-06-08 12:35:10
     Nonce         : 54790
     Previous Hash : 322689654
     Merkle Root   : 88967741&42
     Data          : Alice wants to send 1 Bitcoin to Bob
  ### -Briefly explain with an example how the Merkle root helps verify data integrity
     A Merkle root is a single hash that summarizes all the transactions in a block.It's created by hashing pairs of transactions repeatedly until one       final hash(the Merkle root)is produced.  
     Let's Imagine a block has 4 transactions(Tx1,tx2,Tx3,Tx4)
     -First,Each transaction is hashd indpendently as:
            H1=hash(Tx1)
            H2=hash(Tx2)
            H3=hash(Tx3)
            H4=hash(Tx4)
     -Now These hashes are paired and hashed together as:
            H12=hash(H1+H2)
            H34=hash(H3+H4)
     -Now the resulting hashes are again paired and hashed.This Final Hash is the Merkle Root.   
            Merkle Root=hash(H12+H34)    
     If even one transaction is changed(e.g.,Tx3 is tampered),its hash changes,which changes H34,and that changes the Merkle root.This makes the             system quickly detect that the block's data has been altered—without checking every transaction one by one.  
     Therefore,the Merkle root ensures that the entire set of transactions remains unchanged,helping verify data integrity efficiently.
## 3.Consensus Conceptualization
  ### -What is Proof of Work and why does it require energy?
    Proof of Work (PoW) is a consensus mechanism used in blockchain(like Bitcoin)to verify and add new blocks to the chain.In PoW,miners compete to         solve a complex mathematical puzzle—usually by finding a number(called a nonce)that produces a hash starting with a certain number of zeros.
    It Requires energy because,These computers perform high-speed calculations non-stop,consuming large amounts of electricity.
  ### -What is Proof of Stake and how does it differ?
    Proof of Stake (PoS) is a blockchain consensus mechanism where validators are chosen to create new blocks based on how much cryptocurrency they         "stake" or lock up in the network.The more coins a user stakes,the higher their chance of being selected to validate the next block and earn            rewards.
    The key differences between PoS and PoW lie in their approach to security,energy consumption,and participation.
  ### -What is Delegated Proof of Stake and how are validators selected?
    Delegated Proof of Stake (DPoS) is an advanced version of Proof of Stake where network participants vote for a small number of trusted delegates        (also called validators or witnesses) who are responsible for validating transactions and producing new blocks.
    Validators are selected by:
      -First,Token holders vote by using their coins to elect delegates.
      -The top N delegates with the most votes become active validators.
      -These selected delegates take turns producing blocks in a rotating schedule.
