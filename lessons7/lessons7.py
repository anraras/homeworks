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


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)

    # possible_moves = list(MOVES.keys())
    # applied_moves = 0
    # while applied_moves < 100:
    #     random_move = random.choice(possible_moves)

    #     try:
    #         field = perform_move(field, random_move)
    #         applied_moves += 1
    #     except IndexError:
    #         continue

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


field = shuffle_field()
print_field(field)