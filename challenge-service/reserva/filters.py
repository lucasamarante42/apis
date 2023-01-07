from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Reserva
from challenge_geral.filter import NumberInFilter

class ReservaFilter(filters.FilterSet):
	id = NumberInFilter(field_name='id', lookup_expr='in')
	codigo_reserva = filters.CharFilter(field_name='codigo_reserva', lookup_expr='icontains')
	id_anuncio = NumberInFilter(field_name='id_anuncio', lookup_expr='in')

	data_check_in_inicial = filters.DateFilter(field_name='data_check_in', lookup_expr='gte')
	data_check_in_final = filters.DateFilter(field_name='data_check_in', lookup_expr='lte')

	data_check_out_inicial = filters.DateFilter(field_name='data_check_out', lookup_expr='gte')
	data_check_out_final = filters.DateFilter(field_name='data_check_out', lookup_expr='lte')

	preco_total_maior_que = NumberInFilter(field_name='preco_total', lookup_expr='gt')
	preco_total_menor_que = NumberInFilter(field_name='preco_total', lookup_expr='lt')

	data_criacao_inicial = filters.DateFilter(field_name='data_criacao', lookup_expr='gte')
	data_criacao_final = filters.DateFilter(field_name='data_criacao', lookup_expr='lte')

	data_atualizacao_inicial = filters.DateFilter(field_name='data_atualizacao', lookup_expr='gte')
	data_atualizacao_final = filters.DateFilter(field_name='data_atualizacao', lookup_expr='lte')

	class Meta:
		model = Reserva
		fields = [
				'id', 'codigo_reserva', 'id_anuncio',
				'data_check_in_inicial', 'data_check_in_final',
				'data_check_out_inicial', 'data_check_out_final',
				'preco_total_maior_que', 'preco_total_menor_que',
				'data_criacao_inicial', 'data_criacao_final',
				'data_atualizacao_inicial', 'data_atualizacao_final'
				]