#/opt/homebrew/bin/python3

import random
import hashlib
import math

def precompute_table(plain_text, n):

	# Setting variables
	i = 1

	# Key: EP, Value: SP
	table = {
		"testKey": "testValue",
		"aKey": "aValue"
	}

	print ("\nTable: ", table)
	print("\nKeys:", table.keys())
	print("Values:", table.values(), end="\n\n")

	sorted_table = sorted(table)
	print("Sorted table by keys:", sorted_table, end="\n\n")


	# selecting the random points
	SP = random.randint(0, 256)
	EP = random.randint(0, 256)

	# computing the chains

	# sorting the table
	while (i < n):
		# Generate cipher text for ever plain text under N
		plain_text = plain_text.encode()
		cipher_text = hashlib.sha256(plain_text)
		hex_digest = cipher_text.hexdigest()
		print("Cipher Text", hex_digest)

		# get the first 16 bits of the sha256
		truncated_sha = hex_digest[0:16]
		print("Truncated SHA:", truncated_sha)

		# convert hex to integer to use in f
		converted_to_int = int(truncated_sha, 16)
		print("Integer:", converted_to_int)

		f = math.pow(converted_to_int, -1)
		print ("Inverted:", f)

		# f = converted_to_int % (math.pow(2, k))

		update = {cipher_text, plain_text}
		table.update(update)

		print(update)

		# if key in table.keys():
		if EP in table.keys():
			print("\nTrue\n")
		else:
			print("\nFalse\n")

		# sort table with respect to EP
		# table = sorted(table)
		return i
		
def attack(hash):
	# find pre-image by using table
	# if (hash in table):
	# use distingued point technique
	# pre_image = 
	return

if __name__ == "__main__":

	# Case A
	# 16 bits
	k = 16
	plain_text = "test"
	precompute_table(plain_text, k)
	
	# Case B
	# 20 bits
	k = 20
	# precompute_table(k)

	# Case C
	# 24 bits
	k = 24
	# precompute_table(k)

