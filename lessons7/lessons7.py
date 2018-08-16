# 1)

'''number = int(input('Input your  number plz : '))
if number % 2 == 0:
	raise ValueError ('You put even number')
elif number < 0 :
	raise TypeError ('You put  number less than 0')
elif number > 10:
	raise IndexError ('You put  number  more than 10')
	'''

#2

'''
l = [i for i in range(1, 10)]
try:
	users_index = int(input('Input index  for  list : '))
	print(l[users_index])
except ValueError:
	print('you put bad index')
except IndexError:
	print('you put wrong index')	
	'''
#3
'''
def function (x, y):
	if x > 0 and y > 0:
		result = x + y
	elif x < 0 and y < 0:
		result = x - y
	else :
		result = 0

	return result

print(function(int(input()),int(input())))'''
#4
'''
def maximum(x, y, z):
	list = [x, y, z]
	list.remove(min(list))
	return(list)

print(maximum(int(input()),int(input()),int(input())))
'''
#5
'''
def function (flag, *numbers):
	print(numbers)
	
	if flag == True:
		list = [i for i in numbers if int(i) % 2 !=0 ]
		print(list)
	elif flag == False:
		list = [i for i in numbers if int(i) % 2 ==0 ]
		print(list)

function(False, 5, 7, 89, -2, -3, 4)
'''
#6

import random

WORDS = [ 'developer', 'macos', 'github']



def game_world():
	return random.choice(WORDS)

def user_letter():
	while True:
		letter = input('Input letter : ')
		if letter.isalpha() == False:
			print('It is not  letter !')
		elif len(letter) != 1:
			print('Input 1 letter !')
		else :
			return letter



def initial_statuses_word(word):
	statuses = []
	for letters in word:
		statuses.append(False)
	return statuses

def user_letter_veretification(word, statuses, letter):
	if letter not in word:
		return False
	
	for index, l in enumerate(word):
		if l == letter:
			statuses[index] = True

	return True

def finish_game(statuses, max_lives):
	if max_lives <= 0:
		print ('Game Over')
		return True
	for status in statuses:
		if not status:
			return False
	print ('You WIN')
	return True

def print_word(word, statuses):
	for index, letter in enumerate(word):
		if statuses[index]:
			print(letter, end=' ')
		else:
			print('_ ', end='')

	print()

	




	


def main():
	word = game_world()
	print(word)
	statuses = initial_statuses_word(word)
	print(statuses)
	max_lives = 10
	
	while not finish_game(statuses, max_lives):
		print('You lives is ', max_lives)
		print_word(word, statuses)
		letter = user_letter()
		result = user_letter_veretification(word,statuses,letter)

		if not result:
			print('No Letters in  word')
			max_lives -=1
	

main()


#7
'''
name = input('Input Name : ')
x = len(name) + 6
print(('{0:*^'+ str(x) +'}').format(name))
'''