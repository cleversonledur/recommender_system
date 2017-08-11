from django.shortcuts import render

from wine.data_handler import *
from wine.data_loader import *

import pandas as pd
from scipy.spatial.distance import cosine

from collaborative_filtering import *


def get_recommendations(cpf, customers, purchases):

	product_list = get_product_list(purchases)

	customers_products = get_customer_products(customers, product_list, purchases)
	
	dataset = {}

	for customer in customers:
		_products = {}

		for product in product_list:
			total = 0
			for purchase in purchases:
				if cpf_compare(purchase['cliente'], customer['cpf']):
					for item in purchase['itens']:
						if product==item:
							total+=1
			_products.update({product['produto'] : total})
		dataset.update({ customer['cpf'] : _products })

	return similarity_score(dataset, cpf, '000.000.000-09')

	return most_similar_users(dataset, cpf,4)

	return user_recommendations(dataset,cpf)




def list(request):

	cpf = request.GET.get('customer')

	(customers, purchases) = load_data()

	recommendations = get_recommendations(cpf, customers, purchases)
	customer = None
	for _customer in customers:
		if _customer['cpf']==cpf:
			customer = _customer

	context = {
		'recommendations' : recommendations,
		'customer' : customer,
	} 

	return render(request, 'recommend.html', context)
