def user_letter_veretification(word, statuses, letter):
	statuses = [False,False,False,False,False,False,False]
	for index, l in enumerate(word):
		if l == letter:
			statuses[index] = True
	print(statuses)

	return statuses

def main():

	user_letter_veretification(word,statuses, letter)
	user_letter_veretification(word,statuses, letter)
	user_letter_veretification(word,statuses, letter)
	user_letter_veretification(word,statuses, letter)
main()
