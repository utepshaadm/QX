''' QX Playing Card Hash/MAC'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class QX:
    def __init__(self):
        self.deck = list(range(52))
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def transpose(self):
    	c = 0
    	i = 0
    	for x in range(13):
    		for y in range(c):
                 self.deck[c + 0], self.deck[c + 1] = self.deck[c + 1], self.deck[c + 0]
                 self.deck[c + 2], self.deck[c + 1] = self.deck[c + 1], self.deck[c + 2]
                 self.deck[c + 2], self.deck[c + 3] = self.deck[c + 3], self.deck[c + 2]
                 self.deck[c + 0], self.deck[c + 3] = self.deck[c + 3], self.deck[c + 0]
                 c += 4
    
    	for x in range(4):
    	    self.deck.append(self.deck.pop(0))
    
    def interleave(self):
    	d = []
    	c = 0
    	for x in range(26):
    		d.append(self.deck.pop(1 + c))
    		c += 1
    	self.deck.extend(d)
    	
    def qx_input(self, n):
    	self.deck.append(self.deck.pop(n))
    	
    def heka(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         
         self.deck.insert(self.deck[1], self.deck.pop(0))
         return chr((self.deck[self.deck[self.deck[0]]] % 26) + 65)
    	
    def heka_core(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         
         self.deck.insert(self.deck[1], self.deck.pop(0))
         
         for x in range(self.deck[self.deck[self.deck[0]]]):
         	self.deck.append(self.deck.pop(0))
         
    def input_letter(self, letter):
        num = ord(letter) - 65
        self.qx_input(num)

    def mac(self, letters):
        for x in range(len(letters)):
            self.input_letter(letters[x])
        self.transpose()
        self.interleave()
        self.heka_core()
        m = []
        for x in range(len(self.deck)):
        	self.qx_input(self.deck[x])
        for x in range(len(self.deck)):
        	m.append(chr((self.deck[x] % 26) + 65))
   
        return "".join(m)
        
qx = QX()
#heka.gen_rand_decks()
m = [chr(65)] * 100000
#msg = "".join(m)
msg = "A "
tag = qx.mac(msg)
print(tag)
