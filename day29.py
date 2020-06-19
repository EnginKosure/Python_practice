
import re
from time import time

start_time = time()


def convert_string(s):
    new_string = ''
    for i in s:
        if i.lower() != i:
            i = i.lower()
            new_string += ' ' + i
        else:
            new_string += i
    print(new_string)
    return new_string


convert_string('helloWorld')  # hello world
convert_string('iLoveMyTeapot')  # i love my teapot
convert_string('stayInStaySafe')  # stay in stay safe
convert_string('iLoveClarusway')  # i love clarusway
print(f'---AAA {time()-start_time} seconds ---')

start_time = time()


def func1(sentence):

    list_version = re.findall('[A-Z][a-z]*', sentence)
    strval = ' '.join(list_version)
    strfinal = strval.replace(' , ', ' ')
    print(strfinal.lower())
    return strfinal.lower()


func1('helloWorld')  # hello world
func1('iLoveMyTeapot')  # i love my teapot
func1('stayInStaySafe')  # stay in stay safe
func1('iLoveClarusway')  # i love clarusway
print(f'---BBB {time()-start_time} seconds ---')

start_time = time()


def func2(data):
    output = ''
    for ch in data:
        if 64 < ord(ch) < 91:
            output += f"{' '}{ch.lower ( )}"
        else:
            output += ch
    print(output)
    return output


func2('helloWorld')  # hello world
func2('iLoveMyTeapot')  # i love my teapot
func2('stayInStaySafe')  # stay in stay safe
func2('iLoveClarusway')  # i love clarusway
print(f'---CCC {time()-start_time} seconds ---')


start_time = time()


def func3(data):
    sentence = ''
    for chrc in data:
        if chrc.islower() == False:
            sentence += ' ' + chrc.lower()
        else:
            sentence += chrc
    print(sentence)
    return sentence


func3('helloWorld')  # hello world
func3('iLoveMyTeapot')  # i love my teapot
func3('stayInStaySafe')  # stay in stay safe
func3('iLoveClarusway')  # i love clarusway
print(f'---DDD {time()-start_time} seconds ---')
