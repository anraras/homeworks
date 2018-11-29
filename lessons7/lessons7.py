
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
'''
import random
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

'''
'''
import random
X = True
O = False


def board():
	board = [None for i in range(1,10)]
	print(board)
	return board

def print_board(board):
	for index, i in enumerate(board):
	    if i is None :
	        board[index] = index+1
	    if i is True :
	        board[index] = 'X'
	    if i is False :
	        board[index] = 'O'
	for i in range(0, 10, 3) :
		print(board[i:i + 3])        
    

    


def choice_x_or_o():
	while True:
		try:
		
			player = int(input('Choise your  side \n 1 - X \n 2 - O \n  '))
			if player == 1:
				player = X
				computer = O
			elif player == 2:
				player = O
				computer = X
			return (player, computer)
		except (ValueError, UnboundLocalError):
			print('You mistake !!! Input 1 or 2 plz')


def player_step(board,player):
	while True:
		try:
			step = int(input('Input number 1-9 for your  step : '))
			if step in legal_move(board):
				board[step - 1] = player
				return board
			else:
				print('Its move  is alredy has been ')
		except (ValueError, IndexError, UnboundLocalError):
			print('You must input number 1 - 9 ')


def legal_move(board):
	move_list = []
	print(board)
	for i in range(0,9):
		if board[i] is None:
			print(board[i])
			move_list.append(i)
	return move_list


def computer_choise(board,player,computer):
	for move in legal_move(board):
		board[move] = computer
		if winner_combination(board) == computer:
			return move
		board[move] = None

	for move in legal_move(board):
		board[move] = computer
		if winner_combination(board) == player:
			return move
		board[move] = None
	move = random.choice(legal_move(board))
	return move

def computer_move(board, move):
	board[move] = computer
	return board


	




def winner_combination(board):
	win_comb = (

		(0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)

        )
	for i in win_comb:
		if boardp[i[0]] == board[i[1]] == board[i[2]] != None:
			result = board[i[0]]
			return result
	if None not in board:
		print("It's Draw")

def winner(result):
	if result == player:
		print('Exelent You Win !!!')
	elif result == computer:
		print('Sorry but you loser !')





	



board = board()
print(board)

print_board(board)

player, computer = choice_x_or_o()
print(board)
legal_move(board)
print(legal_move(board))
board = player_step(board,player)
print_board(board)
legal_move(board)
move =computer_choise(board,player,computer)
board = computer_move(board,move)
print_board(board)

'''
'''
class Printer():
	def log(self, *values):
		self.values = values
		print(self.values)

class FormattedPrinter(Printer):
	def formated_log(self, *values):
		print('***********************************************')
		self.log(*values)
		print('************************************************')


a = FormattedPrinter()
a.log(1, 2, 3, 4, 5, 6, 7, 8, 9)

b = FormattedPrinter()
b.formated_log(1, 2, 3, 4, 5, 6, 7, 8, 9)
'''

'''
class Animal(object):
	def __init__(self, name, agression):
		self.name = name
		self.agression = agression

	def attack_human(self, human):
		if self.agression > human.agression : 
			print('{} attack {} and win!!!'.format(self.name, human.name))
			human.dungerous_list.append(self.name)
			print(human.dungerous_list)
		else :
			print('{} Attack {} and fall'.format(self.name, human.name))

class Human(Animal):
	def __init__(self,name,agression):
		self.dungerous_list = []
		super().__init__(name, agression)

	def is_dangerous (self, target):
		
		if target.name in self.dungerous_list:
			print('{} is  dangerous for {}'.format(target.name, self.name))
		else :
			print('{} is not  dangerous for {}'.format(target.name, self.name))


hercules = Human('Геракл', 50)
prometeus = Human('Прометей', 30)

hydra = Animal('Гидра', 70)
hawk = Animal('Ястреб', 50)
lamb = Animal('Овца', 30)
print('\nПолучение людьми опыта общения с животными:\n ')
hydra.attack_human(hercules)
hawk.attack_human(hercules)
lamb.attack_human(hercules)

hydra.attack_human(prometeus)
hawk.attack_human(prometeus)
lamb.attack_human(prometeus)

print('\nПолучение людьми опыта общения с другими людьми:\n ')
hercules.attack_human(prometeus)

print('\nПроверка накопленного людьми опыта общения с животными:\n ')
hercules.is_dangerous(hydra)
hercules.is_dangerous(hawk)
hercules.is_dangerous(lamb)

prometeus.is_dangerous(hydra)
prometeus.is_dangerous(hawk)
prometeus.is_dangerous(lamb)

print('\nПроверка накопленного людьми опыта общения с другими людьми:\n ')
prometeus.is_dangerous(hercules)
hercules.is_dangerous(prometeus)
'''
'''
m =map(lambda x: x % 5, [1, 4, 5, 30, 99])
list(m)

m2 =map(lambda x: str(x), [3, 4, 90, -2])
list(m2)

f = filter(lambda x: type(x) != str, ['some', 1, 'v', 40, '3a', str] )
list(f)

from functools import reduce
l=[]
r = reduce(lambda x, y : x + y, list(map(lambda x: len(x), ['some', 'other', 'value'])))
'''
'''
def decorator(functions):
	def new_function(flag, *numbers):
		print(functions.__name__ , ' is canceled')

	return new_function


@decorator
def jopa (flag, *numbers):
	print(numbers)
	
	if flag == True:
		list = [i for i in numbers if int(i) % 2 !=0 ]
		print(list)
	elif flag == False:
		list = [i for i in numbers if int(i) % 2 ==0 ]
		print(list)

jopa(True, 5, 7, 89, -2, -3, 4)
'''
'''
def way_better(filename):
	print('reading file with way better')
	with open(filename) as f:
		return f.read()

print(way_better('line 1.txt'))
  

def read_file(file):
	print('reading file')
	try:
		f = open(file)
		content = f.read()
		f.close()
	finally:
		print('Final')
		f.close()
	return content


print(read_file('line 1.txt'))
'''
'''

def write_to_file(name, content, mode='w'):
	with open(name, mode=mode) as f:
		f.write(content)


write_to_file('my new file.txt', '\nperfect \ntext \nend final', mode='a')
'''

'''
import re

def car_number(number):
	mutch = re.fullmatch(r'\b[АВЕКМНОРСТУХ]\d\d\d[АВЕКМНОРСТУХ]{2}\d{2,3}', number)
	mutch2 = re.fullmatch(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', number)
	
	if mutch:
		print('Private')
	elif mutch2:
		print('Taxi')
	else:
		print('Fail')

car_number('С227НА777')
car_number('КУ22777')
car_number('Т22В7477')
car_number('М227К19У9')
car_number(' С227НА777')
'''
'''
def write_to_file(name,content, mode='a'):
	with open(name, mode=mode) as f:
		f.write(content)

def read_to_file(name):
	with open(name) as f:
		return print(f.read())


write_to_file('my new file.txt', '\nhey its new line')
read_to_file('my new file.txt')'''
'''
import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts')
d = {}

for key, value in r.headers.items():
	print(key, ' : ', value)
	d[key] = value
for key, value in d.items():
	with open('heads.json', 'w') as f:
		f.write(key, ' : ', value)
'''
'''
from flask import Flask

app = Flask(__name__)


@app.route('/<str1>,<str2>,<str3>')
def home(str1, str2, str3):
	l = [str1, str2, str3]
	m = max(len(str1), len(str2), len(str3))
	for i in l:
		if len(i) == m:
			return i 


if __name__ == '__main__':
    app.run()
    '''




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
'''
6

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
name = input('Input Name : ')
x = len(name) + 6
print(('{0:*^'+ str(x) +'}').format(name))
'''
'''
from flask import Flask

app = Flask(__name__)


@app.route('/<filename>')
def home(filename):
	try:
		with open(str(filename)) as f:
			
			return 'Yes'
	except FileNotFoundError:
		return 'No'


if __name__ == '__main__':
    app.run()
'''
'''
from flask import Flask, request
import datetime

from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, ValidationError

def jobs(form, field):
	if (field.data != 'IT') and (field.data != 'HR') and (field.data != 'Banks'):
		raise ValidationError('Name must be less than 50 characters')

def dates(form, field):
	now_time = datetime.datetime.now().strftime('%d-%m-%Y')
	if field.data[3:5] != now_time[3:5]:
		raise ValidationError('Name must be less than 50 characters')


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Length(min=1, max=35), jobs
    ])
    date = StringField(label='date', validators = [
    	validators.Length(10), dates
    	])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()

'''
'''

from flask import Flask
import json

app = Flask(__name__)

@app.route('/locales')
def jsondict():
	my_dict = {'ru' : 'russian', 'en':'english', 'it': 'italian'}
	return json.dumps(my_dict)

if __name__ == '__main__':
	app.run()

	
from flask import Flask, request
app = Flask(__name__)

@app.route('/sum/<int:first>/<int:second>')
def my_sum(first, second):
	t = first + second
	return str(t)

if __name__== '__main__':
	app.run()


'''
'''
from flask import Flask, request




app = Flask(__name__)
app.config.update(
	DEBUG=True,
	SECRET_KEY='This key must be secret!',
	WTF_CSRF_ENABLE=False,
	)

@app.route('/<username>')
def hello(username):
	return 'hello {}'.format(username)

if __name__=='__main__':
	app.run()
'''
'''
from flask import Flask, request
import json

from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, ValidationError

def valid_password(form, field):
	if form.data['password'] != form.data['confimpassword']:
		raise ValidationError('пароли не совпадают')

class My_form(FlaskForm):
	email=StringField(label='E-mail', validators=[
		validators.Length(min=6, max = 17),
		validators.Email()])
	password=StringField(label='pass', validators=[
		validators.Length(min=6)])
	confimpassword=StringField(label='conpass', validators=[
		validators.Length(min=6), valid_password])
		


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/form/user', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = My_form(request.form)
        #print(form.validate())
        #print(form.errors)

        if form.validate():
            return json.dumps({'status' : 0}) 
        else:
        	

        	 
            return str(json.dumps(form.errors, ).encode('utf8')) + str(json.dumps({'status' : 0}))

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()
    '''
'''
from flask import Flask, request

app=Flask(__name__)
app.config.update(
 	DEBUG=True,
 	SECRET_KEY='asdfasda',
 	WTF_CSRF_ENABLED = False,
 	)

@app.route('/serve/<path:filename>')
def read_file(filename):
 	try:
 		with open(filename) as f:
 			return f.read()
 	except:
 		return '404'
if __name__=='__main__':
 	app.run()
'''
'''
from flask import Flask, request



app = Flask(__name__)
app.config.update(
	DEBUG=True,
	SECRET_KEY='some key',
	)


@app.route('/', methods=['GET','POST'])
def home():
	
	return 'hello world!', 200

#print(request, type(request), request.method)

#with app.test_request_context('/?next=http://example.com/'):
    #print(request, type(request), request.method)

if __name__=='__main__':
	app.run()
'''
'''
import config
from flask_wtf import FlaskForm
from flask import Flask, request, url_for
import random
from wtforms import IntegerField, validators

class Riddler(object): #class for riddler  numbers

	number = None

	@classmethod
	def new_number(cls, max):
		cls.number = random.randint(1, max)
		print('Riddler number is ', cls.number)

class GuessForm(FlaskForm):
	number = IntegerField(label='Nuber is ', validators=[validators.Required()])

app = Flask(__name__)

app.config.from_object(config)

@app.route('/', methods=['GET'])
def home():
	Riddler.new_number(100)
	print(Riddler.number)
	return ' Number is  riddler'


@app.route('/guess', methods=['POST'])
def guess():
	if Riddler.number == None:
		return '<a href="/">Вы не загадали число</a>'

	form=GuessForm(request.form)

	if form.validate():
		user_number = form.number.data

		if user_number == Riddler.number:
			Riddler.new_number(100)
			return 'You win!!! another number is  riddler'
		elif user_number < Riddler.number:
			return ' > '
		elif user_number > Riddler.number:
			return '<'

	else:
		return str(form.errors)





if __name__=='__main__':
	app.run()

'''
from contextlib import contextmanager


class Lock(object):
	def __init__(self):
		self.lock = False

@contextmanager
def locker(some_lock):
	print(some_lock.lock)
	some_lock.lock = True
	yield 
	print(some_lock.lock)

with locker(Lock()) as f:
	print(f)

@contextmanager
def loger():
	try:
		yield
	except Exception as e:
		print('logs: ', str(e))

with loger():
	1/0
with loger():
	's'/2

from time import time, sleep
from datetime import datetime

class TimeIt(object):
	def __enter__(self):
		self.start_time = datetime.now()
		print('Start time  is {}'.format(self.start_time))
		return self

	def __exit__(self, *args):
		self.end_time = datetime.now()
		print('End time  is {}'.format(self.end_time))
		self.time = self.end_time - self.start_time

with TimeIt() as t:
	sleep(2)
print('Execution time was :', t.time )