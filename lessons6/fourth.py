'''
r - чтение файла
w - перезапись файла
a - добавление в файл
b - Binary mode
'''

filename = input('ВВедите имя файла')
text = input('какой текст ввести в файл ?')

file = open(filename, 'w')
file.write(text)
file.close()