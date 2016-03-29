#Create sample for attribution test
import random
import numpy

dic_touch = {
	'type':[ 
		('click',0.8),
		('impression',0.2)
		],
	'channel':['Direct','SEO','SEM','Remarketing','Display','Facebook','Affiliates'],
	'device':[
		('Smartphone',0.5),
		('Tablet',0.1),
		('Desktop',0.4)
		]
	}

def pick(dic):
   total = sum(w for c, w in dic)
   r = random.uniform(0, total)
   upto = 0
   for c, w in dic:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"

class touch:
	def __init__(self):
		self.transaction_id = x
		self.transaction_timestamp = '2016-03-01 20:00:00'
		self.interaction_type = pick(dic_touch['type'])
		self.interaction_channel = random.choice(dic_touch['channel'])
		self.interaction_device = pick(dic_touch['channel'])
		self.interaction_timestamp = '2016-03-01 20:00:00'

class p2p:
	def __init__(self):
		self.transaction_id = x
		self.transaction_timestamp = '2016-03-01 20:00:00'
		self.touch_count = int(numpy.random.chisquare(4)*3)+1	
