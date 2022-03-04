#/opt/homebrew/bin/python3
# Tom Graham
# Advanced Crypto
# Project 2

import random
import hashlib
import hmac
import secrets

# Calculate hash for given x
def calculate_hash(plain_text, key):
	cipher_text = hmac.new(key.encode(), msg=plain_text, digestmod=hashlib.sha256).digest()[0:2]
	key = cipher_text
	return key.hex()

# Precompute each chain
def compute_chain(plain_text, SP):
	j = 0
	InitalSP = SP
	chain_length = 2**8
	while (j < chain_length):
		# Generate EP from last key
		SP = calculate_hash(plain_text, SP)
		j = j + 1
	dict[SP] = InitalSP

# Precompute the table
def compute_table(plain_text, chain_length, k, bytes):
	i = 0
	keyspace = 2**k
	num_of_chains = keyspace/chain_length

	while (i < num_of_chains):
		SP = secrets.token_hex(nbytes=bytes)
		compute_chain(plain_text, SP)
		i = i + 1
	return dict
	#online_attack(dict, SP, InitalSP)

# The online stage find preimage, given y find x
def online_attack(dict, SP):
	print('seraching')
	# find pre-image by using table
	# while SP not in dict:
	# 	compute_table(plain_text, chain_length, k, bytes)
	# 	print ('collision found')
	# return True

	# if dictionary has SP for given EP
	# use distingued point technique
	# pre_image = 


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
	print (dict)

	# Case B
	# 20 bits
	k = 20
	# precompute_table(k)

	# Case C
	# 24 bits
	k = 24
	# precompute_table(k)

