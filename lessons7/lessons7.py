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
'''

import random

WORDS = [ 'developer', 'macos', 'github']

MAX_LIVES = 10

def game_world():
	word = random.choice(WORDS)
	return word

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
	
	statuses = [False,False,False,False,False,False,False]
	for index, l in enumerate(word):
		if l == letter:
			statuses[index] = True
	print(statuses)

	return statuses


def main():
	word = game_world()
	statuses = initial_statuses_word(word)
	letter = user_letter()
	user_letter_veretification(word,statuses, letter)



main()
'''

#7
'''
name = input('Input Name : ')
x = len(name) + 6
print(('{0:*^'+ str(x) +'}').format(name))
'''

#8

X = 'X'
O = 'O'
EMPLY_PLACE = None
field = list(range(1,10))

def player_side():
	while True:
		try:
			side = int(input('Choise your side and input \n 1 for X :  \n 2 for O : '))
						
			if int(side) == 1:
				player_side = X
				
				return player_side
			elif int(side) == 2:
				player_side = O
				
				return player_side
		except ValueError:
			print('Input 1 or 2')



def print_field (field):
	




    for i in range(0, 10, 3) :
        print(field[i:i + 3])
    print('\n')

def field_moves(move,player_side,field):
	field[move] = player_side
	print(field)
	return field




def player_move():
	while True:
		try:
			move = (int(input('INput where move : ')) - 1)
			if 0 <= move < 9:
				return move
		except ValueError:
			print('Error input move : ')

def main():
	field = list(range(1,10))

	player = player_side()
	print_field(field)
	move = player_move()
	field = field_moves(move,player,field)
	print_field(field)


main()


