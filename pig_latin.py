'''
This is the code for Pig Latin game. It's a language game where all consonants before the first vowel
are moved to the end of the word and suffix "ay" is appended if the word did start with consonant
Otherwise word is unchanged and suffix "yay" is appended to its end.
'''

'''
First function checks if the first letter is a consonant. If so it concats it to an empty string
that we later use to append to the end of word. Then it moves to the next letter. If it is 
among the vowels it slices the word from that point on till the end, concats the consonants' string
and stops any further iteration
'''
def checker(str):

	clip =""
	vowels = ('a','e','o','u','i')
	for i in str:
		if i not in vowels:
			clip += i
		else:
			str = str[str.index(i):] + clip
			break
	return str

def main():

	vowels = ('a','e','o','u','i')
	msg = input("Please enter a word: ").lower()
	if len(msg) == 0 or not msg.isalpha():
		print("Please enter alphabetic str. Exiting...")
		exit()
	else:
		try:
			if msg[0] in vowels:
				msg += "yay"
			else:
				msg = checker(msg) + "ay"
		except Exception as e:
			print(e)
	print(msg)
main()
