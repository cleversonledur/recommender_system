

from django.conf.urls import url
from django.contrib import admin

from django.core.urlresolvers import reverse

from wine import customer, recommender, views

urlpatterns = [

	url(r'^customer/$', 			customer.list, 			name='customerall_view'),

	url(r'^customer/purchases/$', 	customer.purchases, 	name='purchases_view'),
	url(r'^customer/unique/$', 	customer.unique, 		name='unique_view'),
	url(r'^customer/fidelity/$', 	customer.fidelity, 		name='fidelity_view'),

    url(r'^recommend/$', 			recommender.list, 		name='recommend_view'),
    
    url(r'^$', 						views.index, 			name='index_view'),

]
