'''
This is the code for Pig Latin game. It's a language game where all consonants before the first vowel
are moved to the end of the word and suffix "ay" is appended if the word did start with consonant
Otherwise word is unchanged and suffix "yay" is appended to its end

Another version of the pig latin program. This one is more reusable as the is_vowel function 
can be more universely reused. It takes a character as its only argument and returns true or flase
depending on whether it's found in a pre-defined tuple of vowels or not.
'''
def is_vowel(char):
	vowels = ('a','o','e','u','i')
	if char in vowels:
		return True
	else: 
		return False

def main():
	word = input("Please enter a word :")
	clip = ""
	'''
	Next check if there's any input provided and if that input is 
	alphabetic char then proceed, else exit with descriptive message (see bottom)
	'''
	if len(word) > 0 and word.isalpha():                     
		word = word.lower()                      #make word all lower case          
		if is_vowel(word[0]):                    #if it starts with vowel append yay and print out the result 
			word += "yay"
			print(word)
		else:                           #Otherwise for each character in the word check to see if it's vowel or consonant                    
			for i in word:              #if the letter is consonant concat it to the 'clip' string. If it's a vowel slice the word from that point
				if is_vowel(i):         #to the end and add the accumulated 'clip' string at the back of it. Then add 'ay'. Print it and stop any                         
					word = word[word.index(i):] + clip + "ay"   #further iterations.
					print(word)
					break
				else:
					clip += i
					if word == clip:              #If after the last iteration word and 'clip' are equal it means there were no vowels
						print("Your string must contain at least one vowel")
						exit()
	else:
		print("{} is not a valid word.Exiting...".format(word))
		exit()
main()                                             #Invoke the main() function to execute
				
