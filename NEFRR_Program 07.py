#NEHESIA EDMOND
#CS 101 L003
#PROGRAM 07

'''AS STATED IN MY COMMENT, THE PROGRAM INSTRUCTIONS WERE NOT CLEAR, NONE OF MY QUESTIONS
WERE EVER ANSWERED, PROGRAM IS TOO LARGE TO FUNCTION ON MY COMPUTER'''





import random
import itertools
class Bacteria:
	def __init__(self,resistance=3,health=10,life_span=15,birth_counter=3):
		self.resistance=resistance
		self.health=health
		self.life_span=life_span
		self.birth_counter=birth_counter
	def is_alive(self):
		'''checks if bacteria is alive if health and life span greater than 0 '''
		if self.health>0 and self.life_span >0:
			return True
		else:
			return False
	def tick(self):
		'''decrements bc and ls '''
		self.birth_counter-=1
		self.life_span-=1
	def dose(self,dose):
		'''indicates the damage that is to be done by dosage '''
		damage=dose/self.resistance
		self.health=self.health-damage
		return self.health
	def random_num_gen(self):
		'''Adds 1, 0, -1 to resistance. Makes it random '''
		ran=random.randint(-1,1)
		newResistance = self.resistance + ran
		if newResistance >= 10:
			newResistance = 10
		if newResistance <= 1:
			newResistance = 1
		return newResistance
	def reproduce(self):
		'''allows bacteria to reproduce if bacteria is alive and bc is less than or equal to zero. New bacteria has same resistance as parent albeit
		mutated slightly'''
		alive=self.is_alive()
		if alive==True and self.birth_counter<=0:
			self.birth_counter=3
			return Bacteria(self.random_num_gen())

	def __str__(self):
		return'H(%f)     R(%d)     LS(%d)     BC(%d)'%(self.health,self.resistance,self.life_span,self.birth_counter)

class Host(Bacteria):
	def __init__(self,resistance=3,health=10,life_span=15,birth_counter=3):
		super().__init__(resistance=3,health=10,life_span=15,birth_counter=3)
		self.num_bacterias={'resist':[Bacteria.random_num_gen(self)], 'health':[self.health], 'life':[self.life_span],'birth':[self.birth_counter]}
	def tick(self,with_dose=False):
		'''iterates through dictionary. decrements ls and bc. adds dosage when true'''
		avgHealth=[]
		aliveList=[]
		bc=[]
		ls=[]
		for k,v in self.num_bacterias.items():
			if k == 'birth':
				self.birth_counter=v
			if k == 'life':
				self.life_span=v
			if k == 'health':
				self.health=v
		for a,b,c in itertools.zip_longest(self.birth_counter, self.life_span,self.health):
			self.birth_counter = a
			self.life_span=b
			self.health=c
			Bacteria.tick(self)
			bc.append(self.birth_counter)
			ls.append(self.life_span)
			newBact = Bacteria.reproduce(self)
			if newBact != None:
				self.num_bacterias['health'].append(newBact.health)
				self.num_bacterias['life'].append(newBact.life_span)
				self.num_bacterias['birth'].append(newBact.birth_counter)
				self.num_bacterias['resist'].append(newBact.resistance)
		for k,v in self.num_bacterias.items():
			if k=='resist':
				self.resistance= v
			if k == 'health':
				self.health=v
			if k == 'life':
				self.life_span=v
			if k =='birth':
				self.birth_counter=v
		for x, y, z in itertools.zip_longest(self.health,self.resistance,self.life_span):
			self.health=x
			self.resistance=y
			self.life_span=z
			if with_dose == True:
				health=Bacteria.dose(self,25)
				self.health=health
			avgHealth.append(self.health)
			aliveList.append(Bacteria.is_alive(self))
		elem = 0
		while elem < len(avgHealth[:]):
			if aliveList[elem]==False:
				avgHealth.pop(elem)
				aliveList.pop(elem)
				ls.pop(elem)
				bc.pop(elem)
				self.num_bacterias['resist'].pop(elem)
			else:
				elem += 1
		
		self.num_bacterias['health']=avgHealth
		self.num_bacterias['life']=ls
		self.num_bacterias['birth']=bc
		return self.num_bacterias
	def __str__(self):
		a= self.tick(self)
		for k,v in a.items():
			if k == 'resist':
				avgR= sum(v) / len(v)
			if k == 'health':
				avgH = sum(v)/len(v)
				count=len(v)
		print('Count :',count)
		print('Average Health :',avgH)
		print('Average Resistance :',avgR)
		
p1=Host(1)
p2=Host(1)
p3=Host(1)
count=0
while count <=45:
	p1.tick()
	if count <=30:
		p2.tick()
		p3.tick()
	if count >30:
		p2.tick(True)
		if count % 2 == 0:
			p3.tick(True)
		else:
			p3.tick()
	count+=1
print('No dosage')
p1.__str__()
print()
print('Full dosage')
p2.__str__()
print()
print('Half dosed')
p3.__str__()
