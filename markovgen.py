import random

class Markov(object):
	
	def __init__(self, open_file, open_file2):
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()
		
		self.cache2 = {}
		self.open_file2 = open_file2
		self.words2 = self.file_to_words2()
		self.word_size2 = len(self.words2)
		
			
	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words
		
	def file_to_words2(self):
		self.open_file2.seek(0)
		data2 = self.open_file2.read()
		words2 = data2.split()
		return words2
	
	def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		
		if len(self.words) < 3:
			return
		
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			
	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
				
	def generate_markov_text(self, size=11):
		lista = ['robots','has','origins','its','the','on','antient','The','world','history','of']
		#print "self:", self.cache[]
		#for word in self.words2:
		seed =0
		for x in range(1,10):
			#print self.words2[x]
			if self.words2[x].istitle():
			 seed = x
			 print self.words2[x]
			 #print "found an uppercase letter",seed
			 if seed is 0:
			  seed = random.randint(0, self.word_size2-3)
		
		#print self.word_size2
		##seed = random.randint(0, self.word_size2-3)
		seed_word, next_word = self.words2[seed], self.words2[seed+1]
		w1, w2 = seed_word, next_word
		print "initial words:", w1,w2
		w2 = random.choice(self.cache[(w1, w2)])	
		gen_words = []
		for i in xrange(size):
			gen_words.append(w1)
			try:
				temp = w1
				w1 = w2
				#print "temp, w2:", temp,w2
				print "self.cache:",2, self.cache[w1,w2]
				w1,w2 = random.choice(self.cache[(temp, w2)])		
				#w2 = random.choice([1, 2, 3, 5, 9])		
				print "W2:",w2
			except KeyError:
				#print "just jumpped to error"
				#seed = random.randint(0, self.word_size2-3)
				print "the seed is:",seed
				#import pdb; pdb.set_trace()
				w2= self.words2[seed+2]
			#import pdb; pdb.set_trace()
			#w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words)
			
			
		
		