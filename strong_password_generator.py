# Python code to suggest strong password

import random

# Function to insert character in a string
# Because string is immutable in python
def insert(s, pos, ch):
		return(s[:pos] + ch + s[pos:])
		
# adding more characters to 
# suggest strong password
def add_more_char(s, need):
		pos = 0

		# add 26 letters
		low_case = "abcdefghijklmnopqrstuvwxyz"

		for i in range(need):
				pos = random.randint(0, len(s)-1)
				s = insert(s, pos, low_case[random.randint(0,25)])

		return(s)

# Make powerful string
def suggester(l, u, d, s, st):

		# all digits
		num = '0123456789'

		# all lower case, upper case and special characters
		low_case = "abcdefghijklmnopqrstuvwxyz"
		up_case = low_case.upper()
		spl_char = '@#$_()!'

		# Position at which place a character
		pos = 0

		# If there is no lowercase char
		# in input string, add it
		if( l == 0 ):
		
				# Generate random integer under string length
				pos = random.randint(0,len(st)-1)

				# Generate random integer under 26 for indexing of a to z
				st = insert(st, pos, low_case[random.randint(0,25)])

		# If there is no upper case char in input string, add it
		if( u == 0 ):
		
				# Generate random integer under string length
				pos = random.randint(0,len(st)-1)

				# Generate random integer under 26 for indexing of A to Z
				st = insert(st, pos, up_case[random.randint(0,25)])

		# If there is no digit in input string, add it
		if( d == 0 ):
		
				# Generate random integer under string length
				pos = random.randint(0,len(st)-1)

				# Generate random integer under 10 for indexing of 0 to 9
				st = insert(st, pos, num[random.randint(0,9)])

		# If there is no special character
		# in input string, add it
		if( s == 0 ):
		
				# Generate random integer under string length
				pos = random.randint(0,len(st)-1)

				# Generate random integer under 7 for
				# indexing of special characters
				st = insert(st, pos, low_case[random.randint(0,6)])

		return st

# generate_password function : This function is used to check
# strength and if input string is not strong, It will suggest
def generate_password(n, p):

		# flag for lower case, upper case, special
		# characters and need of more characters
		l = 0; u = 0; d = 0; s = 0; need = 0

		# Password suggestions
		suggest = ''

		for i in range(n):
		
				# Password suggestion
				if( p[i].islower() ):
						l = 1
				elif( p[i].isupper() ):
						u = 1
				elif( p[i].isdigit() ):
						d = 1
				else:
						s = 1

		# Check if input string is strong that
		# means all flags are active
		if( (l + u + d + s) == 4):
				print("Your Password is Strong")
				return
		else:
				print("Suggested Passwords")

		# Suggest 10 strong strings
		for i in range(10):
				suggest = suggester(l, u, d, s, p)
				need = 8 - len(suggest)

				if(need > 0):
						suggest = add_more_char(suggest, need)
				print(suggest)


# Driver Code
input_string = 'geek@2018'

generate_password( len(input_string), input_string)


# This code is contributed by Arjun Saini
