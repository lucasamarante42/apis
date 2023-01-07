from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import Anuncio
from .serializers import AnuncioSerializer
from imovel.repositories import ImovelRepositories

class AnuncioTests(APITestCase):

	valid_body = {
		'id_imovel': 2,
		'plataforma_publicada': 'LKW',
		'taxa_plataforma': 100.00
	}

	invalid_body = {
		'id_imovel': 234,
		'plataforma_publicada': '',
		'taxa_plataforma': False
	}

	Anuncio.objects.create(id_imovel=ImovelRepositories.rp_get_by_id(1),
						plataforma_publicada='HHY',
						taxa_plataforma=100.00)

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

		Anuncios = Anuncio.objects.all()
		serializer = AnuncioSerializer(Anuncios, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)