from rest_framework import serializers

from .models import Imovel
from challenge_geral.utils import show_message_errors, data_mapping_to_serializer, data_perform_update
from anuncio.serializers import AnuncioSerializer
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

dict_extra_kwargs = {
	'codigo_imovel': show_message_errors('codigo_imovel', '100'),
	'limite_hospede': show_message_errors('limite_hospede'),
	'quantidade_banheiro': show_message_errors('quantidade_banheiro'),
	'aceita_pet': show_message_errors('aceita_pet'),
	'valor_limpeza': show_message_errors('valor_limpeza', max_digit_field=12, max_decimal_place=2),
	'data_ativacao': show_message_errors('data_ativacao'),
	'data_criacao': show_message_errors('data_criacao'),
	'data_atualizacao': show_message_errors('data_atualizacao'),
	'data_remocao': show_message_errors('data_remocao'),
}

class ImovelListSerializer(serializers.ListSerializer):
	def update(self, instance, validated_data):

		# Maps for id->instance and id->data item.
		data_mapping = data_mapping_to_serializer('id', validated_data)

		# Perform updates.
		return data_perform_update(self, instance, data_mapping)

class ImovelSerializers(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Imovel
		list_serializer_class = ImovelListSerializer
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs


class ImovelSerializer(serializers.ModelSerializer):
	anuncio = AnuncioSerializer(many=True, read_only=True)

	class Meta:
		model = Imovel
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs

class BulkImovelSerializer(BulkSerializerMixin, serializers.ModelSerializer):

	class Meta(object):
		model = Imovel
		fields = '__all__'

		list_serializer_class = BulkListSerializer
		update_lookup_field = 'id'