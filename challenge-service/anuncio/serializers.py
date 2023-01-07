from rest_framework import serializers

from .models import Anuncio
from challenge_geral.utils import show_message_errors, data_mapping_to_serializer, data_perform_update
from reserva.serializers import ReservaSerializer
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

dict_extra_kwargs = {
	'id_imovel': show_message_errors('id_imovel'),
	'plataforma_publicada': show_message_errors('plataforma_publicada', '100'),
	'taxa_plataforma': show_message_errors('taxa_plataforma', max_digit_field=12, max_decimal_place=2),
	'data_criacao': show_message_errors('data_criacao'),
	'data_atualizacao': show_message_errors('data_atualizacao'),
	'data_remocao': show_message_errors('data_remocao'),
}

class AnuncioListSerializer(serializers.ListSerializer):
	def update(self, instance, validated_data):

		# Maps for id->instance and id->data item.
		data_mapping = data_mapping_to_serializer('id', validated_data)

		# Perform updates.
		return data_perform_update(self, instance, data_mapping)

class AnuncioSerializers(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Anuncio
		list_serializer_class = AnuncioListSerializer
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs


class AnuncioSerializer(serializers.ModelSerializer):
	id_imovel_codigo_imovel = serializers.ReadOnlyField(source='id_imovel.codigo_imovel')
	id_imovel_limite_hospede = serializers.ReadOnlyField(source='id_imovel.limite_hospede')
	id_imovel_quantidade_banheiro = serializers.ReadOnlyField(source='id_imovel.quantidade_banheiro')
	id_imovel_aceita_pet = serializers.ReadOnlyField(source='id_imovel.aceita_pet')
	id_imovel_valor_limpeza = serializers.ReadOnlyField(source='id_imovel.valor_limpeza')
	id_imovel_data_ativacao = serializers.ReadOnlyField(source='id_imovel.data_ativacao')
	id_imovel_data_criacao = serializers.ReadOnlyField(source='id_imovel.data_criacao')

	reserva = ReservaSerializer(many=True, read_only=True)

	class Meta:
		model = Anuncio
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs

class BulkAnuncioSerializer(BulkSerializerMixin, serializers.ModelSerializer):

	class Meta(object):
		model = Anuncio
		fields = '__all__'

		list_serializer_class = BulkListSerializer
		update_lookup_field = 'id'