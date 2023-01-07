from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import Imovel
from .serializers import ImovelSerializer
from challenge_geral.utils import get_datetime_now

class ImovelTests(APITestCase):

	valid_body = {
		'codigo_imovel': 'JGK403',
		'limite_hospede': 7,
		'quantidade_banheiro': 2,
		'aceita_pet': True,
		'valor_limpeza': 100.00,
		'data_ativacao': '2023-01-30'
	}

	invalid_body = {
		'codigo_imovel': '',
		'limite_hospede': 2,
		'quantidade_banheiro': 1,
		'aceita_pet': True,
		'valor_limpeza': 50.00,
		'data_ativacao': '2023-03-30'
	}

	Imovel.objects.create(codigo_imovel='EFDS34',
						limite_hospede=2, quantidade_banheiro=1,
						aceita_pet=False, valor_limpeza=40.00,
						data_ativacao=get_datetime_now('date'))

	def test_post_with_valid(self):
		url = reverse('get_post')
		response = self.client.post(url, self.valid_body)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_post_with_invalid(self):
		url = reverse('get_post')
		response = self.client.post(url, self.invalid_body)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_get_all(self):
		url = reverse('get_post')
		response = self.client.get(url)

		Imovels = Imovel.objects.all()
		serializer = ImovelSerializer(Imovels, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)