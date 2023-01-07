from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Imovel
from challenge_geral.filter import NumberInFilter

class ImovelFilter(filters.FilterSet):
	id = NumberInFilter(field_name='id', lookup_expr='in')
	codigo_imovel = filters.CharFilter(field_name='codigo_imovel', lookup_expr='icontains')
	limite_hospede = NumberInFilter(field_name='limite_hospede', lookup_expr='in')
	quantidade_banheiro = NumberInFilter(field_name='quantidade_banheiro', lookup_expr='in')
	aceita_pet = filters.BooleanFilter(field_name='aceita_pet', lookup_expr='exact')

	valor_limpeza_maior_que = NumberInFilter(field_name='valor_limpeza', lookup_expr='gt')
	valor_limpeza_menor_que = NumberInFilter(field_name='valor_limpeza', lookup_expr='lt')

	data_ativacao_inicial = filters.DateFilter(field_name='data_ativacao', lookup_expr='gte')
	data_ativacao_final = filters.DateFilter(field_name='data_ativacao', lookup_expr='lte')

	data_criacao_inicial = filters.DateFilter(field_name='data_criacao', lookup_expr='gte')
	data_criacao_final = filters.DateFilter(field_name='data_criacao', lookup_expr='lte')

	data_atualizacao_inicial = filters.DateFilter(field_name='data_atualizacao', lookup_expr='gte')
	data_atualizacao_final = filters.DateFilter(field_name='data_atualizacao', lookup_expr='lte')

	class Meta:
		model = Imovel
		fields = [
				'id', 'codigo_imovel', 'limite_hospede', 'quantidade_banheiro', 'aceita_pet',
				'valor_limpeza_maior_que', 'valor_limpeza_menor_que',
				'data_ativacao_inicial', 'data_ativacao_final',
				'data_criacao_inicial', 'data_criacao_final',
				'data_atualizacao_inicial', 'data_atualizacao_final'
				]