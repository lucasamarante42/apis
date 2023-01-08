
from .models import Imovel
from challenge_geral.utils import get_datetime_now

class ImovelRepositories():

	@staticmethod
	def rp_get_all():
		return Imovel.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return Imovel.objects.get(pk=pk)
		except Imovel.DoesNotExist:
			return None

	@staticmethod
	def rp_delete_by_id(pk):
		obj = ImovelRepositories.rp_get_by_id(pk)
		if obj:
			obj.data_remocao = get_datetime_now('datetime')
			obj.save()
			return True
		return False

	@staticmethod
	def rp_get_in_bulk(lst_ids):
		return Imovel.objects.in_bulk(id_list=lst_ids, field_name='id')

	@staticmethod
	def rp_create_obj(dict_data=None):
		return Imovel(codigo_imovel=dict_data.get('codigo_imovel'),
						limite_hospede=dict_data.get('limite_hospede'),
						quantidade_banheiro=dict_data.get('quantidade_banheiro'),
						aceita_pet=dict_data.get('aceita_pet'),
						valor_limpeza=dict_data.get('valor_limpeza'),
						data_ativacao=dict_data.get('data_ativacao'))

	@staticmethod
	def rp_save_bulk_create(list_obj=None):
		Imovel.objects.bulk_create(list_obj)