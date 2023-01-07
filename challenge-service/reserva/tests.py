from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import Reserva
from .serializers import ReservaSerializer
from challenge_geral.utils import get_datetime_now
from anuncio.repositories import AnuncioRepositories

class ReservaTests(APITestCase):

	valid_body = {
		'id_anuncio': 1,
		'data_check_in': '2023-01-30',
		'data_check_out': '2023-01-31',
		'preco_total': 100.00,
		'comentario': 'OBSERVAÇÕES',
		'quantidade_hospede': 10
	}

	invalid_body = {
		'id_anuncio': 1444,
		'data_check_in': '2023-01-30',
		'data_check_out': '2023-01-31',
		'preco_total': False,
		'comentario': 'OBSERVAÇÕES',
		'quantidade_hospede': 'DEZ'
	}

	Reserva.objects.create(id_anuncio=AnuncioRepositories.rp_get_by_id(1),
						data_check_in=get_datetime_now('date'),
						data_check_out=get_datetime_now('date'),
						preco_total=254.68,
						comentario='OBS',
						quantidade_hospede=2)

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

		Reservas = Reserva.objects.all()
		serializer = ReservaSerializer(Reservas, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)