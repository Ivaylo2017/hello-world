'''
The program encrypts messages using Ceasar cypher with key length specified by the user
When the same key with opposite sign is used it can decrypt messages as well. Ceaser cypher is 
the simplest and oldest known transpositional cypher. It adds the key to the numerical representation
of each character in the original text and returns the new charater 
'''
def ceasarcypher(string,n):                                  #Function takes two args - message to be encrypted as str and key as int
	cypheredString = ""
	for character in string:
		if ord(character) in range(97,123):                  #perform conversion for small letters ASCII char 97-123
			charNum = ord(character) + n
			if charNum > 122:
				newChar = chr(charNum - 26)
			elif charNum < 97:
				newChar = chr(charNum + 26)
			else:                                             
				newChar = chr(charNum)                       #translate punctuation as is           
			cypheredString += newChar
		elif ord(character) in range(65,91):                 #perform same actions for capital letters - ASCII char 65-91
			charNum = ord(character) + n
			if charNum > 90:
				newChar = chr(charNum - 26)
			elif charNum < 65:
				newChar = chr(charNum + 26)
			else:
				newChar = chr(charNum)
			cypheredString += newChar
		else:
			cypheredString += character

	return cypheredString                                      #return the cyphertext


def main():
	string = input("Please provide your message:\n")               #Take string input for message from the user and verify
	if type(string) != str:
		print("{} is not  string.".format(string))
	else:
		n = input("Please enter the encryption/decryption key as integer: ")
		try:
			int(n)
			print("\n{} when encrypted is equal to {}.\n".format(string,ceasarcypher(string,n)))        #Print the result using format and calling ceasarcypher function on the user input                                                                          #Take int input fromm user and verify
		except ValueError:
			print("{} is not an integer. Exiting...".format(n))
		

if __name__ == "__main__":                                                                          #Make sure output is only printed if function called from this file
	main()