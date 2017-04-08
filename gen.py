from parse import Parser
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import random

class Generator:
	def __init__(self, name, db, rnd):
		self.name = name
		print name
		self.db   = db
		self.rnd  = rnd

		self.words_input = self.file_to_words()
		self.input = self.get_input_word()

	def _get_next_word(self, word_list):
		print "*****************************_get_next_word*********************"
		print "Word list:",word_list
		print "My input list::",self.words_input
		
		if not self.words_input:
			print "List Empty!!"
			return '$'
			
		#Remove the word from word_list
		if word_list[0] in self.words_input:  #position [1] if trigrams
			self.words_input.remove(word_list[0])
			print "NEW input list:",self.words_input
		if not self.words_input:
			print "List Empty!!"
			return '$'
		
		candidate_words = self.db.get_word_count(word_list)
		#print "candidate_words:::",candidate_words
 		total_next_words = sum(candidate_words.values())
		
		###Stuff added
		countkey=0
		countkey2=0
		
		for i in range(len(self.words_input)):
		  if self.words_input[i] in candidate_words:
			#print "candidate,value", self.words_input[i],candidate_words[self.words_input[i]]
			countkey = candidate_words[self.words_input[i]]
			if (countkey > countkey2):
				countkey2 = countkey
				nextw = self.words_input[i]
		if countkey2 >0:
			print "candidate, value:", nextw, countkey2
			#word_list.remove('world')
			#print word_list
			
			#candidate_words = self.db.get_word_count([nextw])
	        #print "candidate_words:::",candidate_words
			return nextw	
		else:
			 if len(word_list)>0 and self.words_input: #if there is a next word
				rand = random.choice(self.words_input)
				print "rand:",rand
				self.words_input.remove(rand)
				print "not found"
				return rand
			 else:
				return 
				quit()
		print "total_next_words::",total_next_words
		i = self.rnd.randint(total_next_words)
		print "i::",i
		t=0
		for w in candidate_words.keys():
			t += candidate_words[w]
			#print "t, candidate:", t, candidate_words[w]
			if (i <= t):
				print "Returnnn Print w,candidate::", w,candidate_words[w] 
				return w
		assert False

	def generate(self, word_separator):
		print "generate$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
		#print "word separator::",word_separator
		depth = self.db.get_depth()
		#print "depth", depth
		sentence = [Parser.SENTENCE_START_SYMBOL] * (depth - 1)
		#print "sentence",Parser.SENTENCE_START_SYMBOL*(depth - 1)
		end_symbol = [Parser.SENTENCE_END_SYMBOL] * (depth - 1)
		#print "end_symbol:",end_symbol
		countail=0
		counter=0
		while True:
			tail = sentence[(-depth+1):]
			print "tail",tail
			if (counter==11) or (tail == end_symbol):
				print "Found end symbol!", counter
				break
			if countail ==0:
			   word = self.input
			   countail=1
			else:
				print "else",counter
				word = self._get_next_word(tail)
			sentence.append(word)
		
		return word_separator.join(sentence[depth-1:][:1-depth])

		
	def file_to_words(self):
		file_2 = open('try.txt')
		data = file_2.read()
		print "data:",data
		words_input = data.split()
		print "@@@@@@@@@@@@@@@@@@@@ file_to_words @@@@@@@@@@@@@@@",words_input
		print "############# words input #############",words_input
		
		
		'''text = data
		token=nltk.word_tokenize(text)
		bigrams=list(ngrams(token,2))
		print bigrams #bigrams working!!'''
		
		return words_input	
	
	def get_input_word(self):
	#Find frist word of Sentence (most likely that one with uppercase letter, if none is found, get a random - for now
	  seed =0
	  for x in range(len(self.words_input)):
	  #print self.words2[x]
		if self.words_input[x].istitle():
			seed = x
			print "uppercase",self.words_input[x]
			input_word= self.words_input[x]
			#print "found an uppercase letter",seed
		if seed is 0:
			print "no uppercase found"
	  return input_word
	
	