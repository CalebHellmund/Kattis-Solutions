# Problem: Babelfish
# Link: https://open.kattis.com/problems/babelfish
# Difficulty: Medium

dictionary = dict()

word = input()
while word != '':
    english, piglatin  = word.split()
    dictionary[piglatin] = english
    word = input()
while True:
    try:
        spoken = input()
        if spoken in dictionary:
            print(dictionary[spoken])
        else: 
            print('eh')
    except:
        break