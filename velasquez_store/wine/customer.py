from django.shortcuts import render

from wine.data_handler import *
from wine.data_loader import *


def list(request):
	# for customer in customers:
	# 	customer.update({'total_purchases' : get_total_purchases(customer, purchases) 		})
	# 	customer.update({'maior_2016'      : get_unique_compra(customer, purchases, 2016) 	})
	# 	customer.update({'fidelidade' 	   : get_fidelidade(customer, purchases) 			})
	# return None

	(customers, purchases) = load_data()

	#process_customers(customers, purchases)

	context = {
		'content' : None,
		'value'   : None,
		'customers' : customers ,
	}	
	return render(request, 'customer.html', context)

def purchases(request):

	(customers, purchases) = load_data()
	
	data = []

	for customer in customers:
		customer.update({'total_purchases' : get_total_purchases(customer, purchases)})
	
	context = {
		'content' 	: 'purchases',
		'value' 	: 'Total de Compras',
		'customers' : sorted(customers, key=lambda k: k['total_purchases'],reverse=True) ,
	}
	return render(request, 'customer.html', context)

def unique (request):

	(customers, purchases) = load_data()
	
	data = []

	for customer in customers:
		customer.update({'maior_2016' : get_unique_compra(customer, purchases, 2016)})


	context = {
		'content' : 'unique',
		'value' 	: 'Valor da Compra',
		'customers' 	: sorted(customers, key=lambda k: k['maior_2016'],reverse=True) ,
	}
	return render(request, 'customer.html', context)

def fidelity (request):

	(customers, purchases) = load_data()
	
	data = []

	for customer in customers:
		customer.update({'fidelidade' : get_fidelidade(customer, purchases)})

	context = {
		'content' : 'fidelity',
		'value'   : 'Score',
		'customers' 	  : sorted(customers, key=lambda k: k['fidelidade'],reverse=True),
	}
	return render(request, 'customer.html', context)




