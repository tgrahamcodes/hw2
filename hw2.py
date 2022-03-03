#/opt/homebrew/bin/python3

import random
import hashlib
import math

# Calculate hash for given x
def calculate_hash(x):
	x_to_hash = hex(x).encode()
	hash = hashlib.sha256(x_to_hash).hexdigest()[0:k]
	return hash

# Calculate f fk(x) = SHA(x) mod 2k
def calculate_f(x, k):
	x = int(x, 16)
	f = x % math.pow(2, k)
	return f

def precompute_table(k):

	# Setting variables
	i = 1

	# selecting the random points
	SP = random.randint(0, 256)
	EP = random.randint(0, 256)

	# Key: SP, Value: EP
	dict = {
		SP: EP
	}

	print("\nDict:\t\t", dict)
	print("Before Sort:\t", dict.keys())
	print("Values:\t\t", dict.values())

	# # computing the chains
	# for i in range(SP):
	o = 2
	hash = calculate_hash(o)
	print("hash\t\t", hash)
	f = int(calculate_f(hash, k))
	print ("f:\t\t", f)
	print ()

	# 	# if key in table.keys():
	# 	if EP in dict.values():
	# 		print("\nTrue\n")
	# 	else:
	# 		print("\nFalse\n")

	# 	# sort table with respect to EP
	# 	# table = sorted(table)
	# #return i
		
def online_attack(hash):
	# find pre-image by using table
	# if (hash in table):
	# use distingued point technique
	# pre_image = 
	return

if __name__ == "__main__":

	# Case A
	# 16 bits
	k = 16
	precompute_table(k)
	
	# Case B
	# 20 bits
	k = 20
	# precompute_table(k)

	# Case C
	# 24 bits
	k = 24
	# precompute_table(k)

