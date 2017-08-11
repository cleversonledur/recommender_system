# -*- coding: utf-8 -*-



from urllib import urlopen
import json

import pandas as pd

from wine import local



def load_data():

	_customers = []
	_purchases = []

	try:
		_customers 	= urlopen(local.URL_CUSTOMER).read()
	except Exception as e:
		print "Erro de comunicação. (GET Costumers)." + str(e)	

	try:
		_purchases   = urlopen(local.URL_PURCHASES).read()
	except Exception as e:
		print "Erro de comunicação. (GET Purchases)." + str(e)

	try:
		_customers = json.loads(_customers)
	except Exception as e:
		print "Json format error. (Customers)" + str(e)

	try:	
		_purchases = json.loads(_purchases)
	except Exception as e:
		print "Json format error. (Purchases)" + str(e)

	return _customers, _purchases
