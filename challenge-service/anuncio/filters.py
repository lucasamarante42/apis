from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Anuncio
from challenge_geral.filter import NumberInFilter

class AnuncioFilter(filters.FilterSet):
	id = NumberInFilter(field_name='id', lookup_expr='in')
	id_imovel = NumberInFilter(field_name='id_imovel', lookup_expr='in')
	plataforma_publicada = filters.CharFilter(field_name='plataforma_publicada', lookup_expr='icontains')

	taxa_plataforma_maior_que = NumberInFilter(field_name='taxa_plataforma', lookup_expr='gt')
	taxa_plataforma_menor_que = NumberInFilter(field_name='taxa_plataforma', lookup_expr='lt')

	data_criacao_inicial = filters.DateFilter(field_name='data_criacao', lookup_expr='gte')
	data_criacao_final = filters.DateFilter(field_name='data_criacao', lookup_expr='lte')

	data_atualizacao_inicial = filters.DateFilter(field_name='data_atualizacao', lookup_expr='gte')
	data_atualizacao_final = filters.DateFilter(field_name='data_atualizacao', lookup_expr='lte')

	class Meta:
		model = Anuncio
		fields = [
				'id', 'id_imovel', 'plataforma_publicada',
				'taxa_plataforma_maior_que', 'taxa_plataforma_menor_que',
				'data_criacao_inicial', 'data_criacao_final',
				'data_atualizacao_inicial', 'data_atualizacao_final'
				]