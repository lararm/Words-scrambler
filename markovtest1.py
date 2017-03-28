import markovgen
file_1 = open('jeeves.txt')
file_2 = open('try.txt')
markov = markovgen.Markov(file_1,file_2)

print markov.generate_markov_text()

'''import markovgen
file_1 = open('jeeves.txt')
file_2 = open('try.txt')
markov = markovgen.Markov(file_)

print markov.generate_markov_text()'''
