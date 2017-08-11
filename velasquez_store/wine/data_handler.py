from datetime import date

def cpf_compare(cpf1, cpf2):

	cpf1 = cpf1.replace('.','').replace('-','')
	cpf2 = cpf2.replace('.','').replace('-','')

	return int(cpf1)==int(cpf2)


def get_total_purchases(customer, purchases):

	total = 0.0
	for purchase in purchases:

		if cpf_compare(purchase['cliente'], customer['cpf']):
			total += float(purchase['valorTotal'])

	return total

def get_unique_compra(customer, purchases, year):
	
	gt_value = 0.0
	
	for purchase in purchases:

		data = purchase['data']

		if int(data[6:]) == year:
			
			if cpf_compare(purchase['cliente'], customer['cpf']):
				
				if purchase['valorTotal'] > gt_value:
					gt_value = purchase['valorTotal']
	return gt_value

def get_fidelidade(customer, purchases):

	total_purchases = 0

	first_year_purchase = int(date.today().year)
	last_year_purchase = 0

	for purchase in purchases:
		
		data = purchase['data']
		year = int(data[6:])

		if year < first_year_purchase:
			first_year_purchase = year

		if year > last_year_purchase:
			last_year_purchase = year

		if cpf_compare(purchase['cliente'], customer['cpf']):
			total_purchases += 1

	total_years = last_year_purchase - first_year_purchase +1
	fd = total_purchases + total_years

	return fd

def get_product_list(purchases):
	products = []
	for purchase in purchases:
		for item in purchase['itens']:
			if item not in products:
				products.append(item)

	counter = 0
	for product in products:
		counter+=1
		product.update({'id' : counter})

	return products

def get_customer_products(customers, product_list, purchases):
	result = []
	for customer in customers:
		for p in product_list:
			total = 0
			for purchase in purchases:
				if cpf_compare(purchase['cliente'], customer['cpf']):
					for item in purchase['itens']:
						if p==item:
							total+=1
			if total>0:
				
				result.append({
								'customer_id': customer['id'],
								'product_id' : p['id']	,
								'total' 	 : total,
							  })
	return result
	

