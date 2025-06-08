#Simulate and compare PoW, PoS, and DPoS logic in code.
import random
from collections import Counter

# Proof of Work: miners with random computational power
miners = [
    {"name": "MinerA", "power": random.randint(1, 100)},
    {"name": "MinerB", "power": random.randint(1, 100)},
    {"name": "MinerC", "power": random.randint(1, 100)},
]
# Proof of Stake: stakers with random token holdings
stakers = [
    {"name": "StakerA", "stake": random.randint(1, 100)},
    {"name": "StakerB", "stake": random.randint(1, 100)},
    {"name": "StakerC", "stake": random.randint(1, 100)},
]
# Delegated Proof of Stake: voters choosing delegates
delegates = ["DelegateA", "DelegateB", "DelegateC"]
voters = [
    {"voter": "User1", "vote": random.choice(delegates)},
    {"voter": "User2", "vote": random.choice(delegates)},
    {"voter": "User3", "vote": random.choice(delegates)},
]

# PoW: highest computational power wins
winner_pow =max(miners, key=lambda x: x["power"])
print("Proof of Work")
print("-Each miner has a 'power' value representing computational ability")
print("-The miner with the highest power is selected to validate the block.\n")
for miner in miners:
    print(f"-{miner['name']} power: {miner['power']}")
print(f"Selected:{winner_pow['name']}(Highest Power)\n")

# PoS: highest stake wins
winner_pos=max(stakers, key=lambda x: x["stake"])
print("Proof of Stake")
print("-Each staker has a 'stake' value representing the number of tokens they hold")
print("-The validator with the highest stake is selected to validate the block.\n")
for staker in stakers:
    print(f"-{staker['name']} stake: {staker['stake']}")
print(f"Selected: {winner_pos['name']} (Highest Stake)\n")

# DPoS: most votes wins
votes = [voter["vote"] for voter in voters]
vote_counts=Counter(votes)
winner_dpos=vote_counts.most_common(1)[0][0]
print("Delegated Proof of Stake")
print("-Users vote for delegates")
print("-The delegate with the most votes is selected to validate the block.\n")
for voter in voters:
    print(f"-{voter['voter']} voted for: {voter['vote']}")
print(f"Selected: {winner_dpos}(Most Votes)\n")