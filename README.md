# Generate BIP39 seed phrase guaranteed to be randomized based on your input of entropy

This repo is intended to securley generate a BIP39 seed phrase without using the default seed creation process
within hardware wallets. Unless you created it, you cannot guarantee the true randomness or that it was not 
already created by the vendor. The more input you give, the more random it becomes!

Clone the repo with this line:
```bash
git clone https://github.com/anthony-albertina/bip39-entropy.git && cd bip39-entropy
```

Assuming python3 is installed, run the following:
```python
python3 createUserRandomizedSeed.py
```

