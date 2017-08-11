# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import unittest

from wine.data_handler import *
from wine.data_loader import *
from collaborative_filtering import *


class TestCases(unittest.TestCase):

	
	def test_cpf_compare_different(self):
		self.assertFalse(cpf_compare('000.000.222.33', '000.000.222-32'))

	def test_cpf_compare_equal(self):	
		self.assertTrue(cpf_compare('000.000.222.33', '000.000.222.33'))

	def test_cpf_compare_digit_only(self):	
		self.assertTrue(cpf_compare('00000022233', '00000022233'))

	def test_get_total_purchases_1(self):
		customer = { 'cpf' : '00000000001'}
		purchases = [
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
					]
		self.assertEqual(get_total_purchases(customer,purchases), 3000)

	def test_get_total_purchases_2(self):
		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
					]
		self.assertEqual(get_total_purchases(customer,purchases), 0)

	def test_get_total_purchases_3(self):
		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 1000,
						},
					]
		self.assertEqual(get_total_purchases(customer,purchases), 1000)


	def test_get_unique_compra_1(self):
		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1005,
							"data" 		 : "19-02-2016",
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 4000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 9000,
							'data'		 : "01-02-2016"
						},
					]
		self.assertEqual(get_unique_compra(customer,purchases,2016), 4000)

	def test_get_unique_compra_2(self):
		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1005,
							"data" 		 : "19-02-2016",
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 4000,
							'data'		 : "01-02-2014"
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 9000,
							'data'		 : "01-02-2016"
						},
					]
		self.assertEqual(get_unique_compra(customer,purchases,2016), 1005)

	def test_get_unique_compra_3(self):
		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1005,
							"data" 		 : "19-02-2016",
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 4000,
							'data'		 : "01-02-2014"
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 9000,
							'data'		 : "01-02-2016"
						},
					]
		self.assertEqual(get_unique_compra(customer,purchases,2011), 0.0)

	def test_get_unique_compra_4(self):
		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1005,
							"data" 		 : "19-02-2016",
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 4000,
							'data'		 : "01-02-2014"
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 9000,
							'data'		 : "01-02-2016"
						},
					]
		self.assertEqual(get_unique_compra(customer,purchases,2011), 0.0)


	def test_get_fidelidade_1(self):

		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1005,
							"data" 		 : "19-02-2016",
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 4000,
							'data'		 : "01-02-2014"
						},
						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 9000,
							'data'		 : "01-02-2016"
						},
					]
		self.assertEqual(get_fidelidade(customer,purchases), 3+3)



	def test_get_fidelidade_1(self):

		customer = { 'cpf' : '00000000002'}
		purchases = [
						{
							'cliente' 	 : '00000000003',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1000,
							'data'		 : "01-02-2016"
						},
						{
							'cliente' 	 : '00000000002',
							'valorTotal' : 1005,
							"data" 		 : "19-02-2016",
						},

						{
							'cliente' 	 : '00000000001',
							'valorTotal' : 9000,
							'data'		 : "01-02-2016"
						},
					]
		self.assertEqual(get_fidelidade(customer,purchases), 2+1)



if __name__ == '__main__':
	unittest.main()