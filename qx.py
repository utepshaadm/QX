''' Heka QX Playing Card Hash/MAC'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class QX:
    def __init__(self):
        self.deck = list(range(52))
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def qx_input(self, n):
    	self.deck.append(self.deck.pop(n))
    	
    def heka_core(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         
         self.deck.insert(self.deck[1], self.deck.pop(0))
         
         return chr(((self.deck[self.deck[self.deck[0]]]) % 26) + 65)
         
    def input_letter(self, letter):
        num = ord(letter) - 65
        self.qx_input(num)

    def mac(self, letters):
        m = []
        for x in range(len(letters)):
            self.input_letter(letters[x])
        for x in range(52):
        	m.append(self.heka_core())
        return "".join(m)
        
qx = QX()
#heka.gen_rand_decks()
m = [chr(65)] * 100000
#msg = "".join(m)
msg = "HELLOWORLD"
tag = qx.mac(msg)
print(tag)
