import requests
import hashlib
import random

# Official BIP39 wordlist
url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'
wordList = requests.get(url).text.split("\n")[:-1]

# Get user input for entropy
print("Please enter as long of a string as possible to add unique entropy to the algorithm... ")
userInput = input("Enter: ")

# Seed with random number
sha256Hash = hashlib.sha256(userInput.encode()).hexdigest()
base10seed = int(sha256Hash, 16)
random.seed(a=base10seed)

# Generate random seed phrase
print("Executing random seed generator based on your input.")
print("It is advised to reboot your machine after recording your seed phrase to ensure it's not available in memory.\n")

seedList = []
while len(seedList) < 24:
	# Skip a random number of random calls due to the function being deterministic if seed number is known
	randomSkip = random.SystemRandom().randint(0,2047)
	while randomSkip > 0:
		word = random.choice(wordList)
		randomSkip -= 1
	seedList.append(random.choice(wordList))

print(seedList)
print("\nEnd of execution.")
