#/opt/homebrew/bin/python3
# Tom Graham
# Advanced Crypto
# Project 2

import hashlib
import hmac
import secrets

# Calculate hash for given input
def calculate_hash(plain_text, key):
	cipher_text = hmac.new(key.encode(), msg=plain_text, digestmod=hashlib.sha256).digest()[0:2]
	key = cipher_text
	return key.hex()

# Precompute each chain
def compute_chain(plain_text, SP, found):
	if (found):
		chain_length = chain_length - 1
	j = 0
	InitalSP = SP
	chain_length = 2**8
	while (j < chain_length):
		# Generate EP from last key
		SP = calculate_hash(plain_text, SP)
		j = j + 1
	dict[SP] = InitalSP

# Precompute the table and return it as a dictionary
def compute_table(plain_text, chain_length, k, bytes):
	i = 0
	keyspace = 2**k
	num_of_chains = keyspace/chain_length

	while (i < num_of_chains):
		SP = secrets.token_hex(nbytes=bytes)
		compute_chain(plain_text, SP, False)
		i = i + 1
	return dict

# Given cipher text(y) find key that encrypted plain text
def online_attack(dict, y):
	# check y value against EP
	# if it matches an EP that means the key is the previous entry in the chain
    if y in dict.keys():
        print("Y =", dict[y])
		# feed y as input to hash and stop one spot before the end of the chain
		# compute_chain(plain_text, y, True)
	# else:
	# 	Rehash y into yprime then check
	# 	loop this


if __name__ == "__main__":

	dict = {}

	# Case A
	# 16 bits
	k = 16
	bytes = int(k/8)
	i = 1
	chain_length = 2**8
	plain_text = "Testing".encode()
	dict = compute_table(plain_text, chain_length, k, bytes)
	online_attack(dict, '4')
	# print (dict)

	# Case B
	# 20 bits
	k = 20
	# precompute_table(k)

	# Case C
	# 24 bits
	k = 24
	# precompute_table(k)

