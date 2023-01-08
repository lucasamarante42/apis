from rest_framework import serializers

from .models import Reserva
from challenge_geral.utils import show_message_errors, data_mapping_to_serializer, data_perform_update

from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

dict_extra_kwargs = {
	'codigo_reserva': show_message_errors('codigo_reserva', '100'),
	'id_anuncio': show_message_errors('id_anuncio'),
	'data_check_in': show_message_errors('data_check_in'),
	'data_check_out': show_message_errors('data_check_out'),
	'preco_total': show_message_errors('preco_total', max_digit_field=12, max_decimal_place=2),
	'comentario': show_message_errors('comentario', '500'),
	'quantidade_hospede': show_message_errors('quantidade_hospede'),
	'data_criacao': show_message_errors('data_criacao'),
	'data_atualizacao': show_message_errors('data_atualizacao'),
	'data_remocao': show_message_errors('data_remocao'),
}

class ReservaListSerializer(serializers.ListSerializer):
	def update(self, instance, validated_data):

		# Maps for id->instance and id->data item.
		data_mapping = data_mapping_to_serializer('id', validated_data)

		# Perform updates.
		return data_perform_update(self, instance, data_mapping)

class ReservaSerializers(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Reserva
		list_serializer_class = ReservaListSerializer
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs


class ReservaSerializer(serializers.ModelSerializer):
	id_anuncio_plataforma_publicada = serializers.ReadOnlyField(source='id_anuncio.plataforma_publicada')
	id_anuncio_taxa_plataforma = serializers.ReadOnlyField(source='id_anuncio.taxa_plataforma')
	id_anuncio_data_criacao = serializers.ReadOnlyField(source='id_anuncio.data_criacao')

	id_anuncio_id_imovel_codigo_imovel = serializers.ReadOnlyField(source='id_anuncio.id_imovel.codigo_imovel')
	id_anuncio_id_imovel_limite_hospede = serializers.ReadOnlyField(source='id_anuncio.id_imovel.limite_hospede')
	id_anuncio_id_imovel_quantidade_banheiro = serializers.ReadOnlyField(source='id_anuncio.id_imovel.quantidade_banheiro')
	id_anuncio_id_imovel_aceita_pet = serializers.ReadOnlyField(source='id_anuncio.id_imovel.aceita_pet')
	id_anuncio_id_imovel_valor_limpeza = serializers.ReadOnlyField(source='id_anuncio.id_imovel.valor_limpeza')
	id_anuncio_id_imovel_data_ativacao = serializers.ReadOnlyField(source='id_anuncio.id_imovel.data_ativacao')
	id_anuncio_id_imovel_data_criacao = serializers.ReadOnlyField(source='id_anuncio.id_imovel.data_criacao')

	class Meta:
		model = Reserva
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs

	def validate(self, data):
		"""
		Check that the start is before the stop.
		"""
		if data['data_check_in'] > data['data_check_out']:
			raise serializers.ValidationError("A data de check-in não pode ser maior que a data de check-out!")
		return data

class BulkReservaSerializer(BulkSerializerMixin, serializers.ModelSerializer):

	class Meta(object):
		model = Reserva
		fields = '__all__'

		list_serializer_class = BulkListSerializer
		update_lookup_field = 'id'