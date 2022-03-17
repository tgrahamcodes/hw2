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
def compute_chain(plain_text, SP, chainlen):
	j = 0
	InitalSP = SP
	#	chain_length = 2**8
	while (j < chainlen):
		# Generate EP from last key
		SP = calculate_hash(plain_text, SP)
		j = j + 1
	return InitalSP, SP

# Precompute the table and return it as a dictionary
def compute_table(plain_text, chainlen, k, bts):
	i = 0
	keyspace = 2**k
	num_of_chains = keyspace/chainlen

	while (i < num_of_chains):
		# TODO
		SP = secrets.token_hex(nbytes=bts)
		SP, EP = compute_chain(plain_text, SP, chainlen)
		i = i + 1
		dict[EP] = SP
	return dict

# Given cipher text(y) find key that encrypted the plain text
def online_attack(dict, y):
	# TODO
	i = 2**8
	while(i > 0):
		if y in dict.keys():
			SP, EP = compute_chain(plain_text, y, i-1)
			return EP
			
		y = calculate_hash(plain_text, y)
		i = i - 1


if __name__ == "__main__":

	# Create empty dictionary
	dict = {}

	# Case A
	# 16 bits
	k = 16
	# bts = int(k/8)
	
	x = '1e'
	chain_length = 2**4
	plain_text = "Testing".encode()
	dict = compute_table(plain_text, chain_length, k, 2)
	y = calculate_hash(plain_text, x)
	x2 = online_attack(dict, y)
	print('y: ', y)
	print ('x2: ', x2)
	y2 = calculate_hash(plain_text, x2)

	print ('y2: ', y2)
	if (y == y2):
		print('True')
	else:
		print('False')

	# Case B
	# 20 bits
	k = 20
	# precompute_table(k)

	# Case C
	# 24 bits
	k = 24
	# precompute_table(k)

