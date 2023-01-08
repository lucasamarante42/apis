
from .models import Reserva
from challenge_geral.utils import get_datetime_now

class ReservaRepositories():

	@staticmethod
	def rp_get_all():
		return Reserva.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return Reserva.objects.get(pk=pk)
		except Reserva.DoesNotExist:
			return None

	@staticmethod
	def rp_delete_by_id(pk):
		obj = ReservaRepositories.rp_get_by_id(pk)
		if obj:
			obj.data_remocao = get_datetime_now('datetime')
			obj.save()
			return True
		return False

	@staticmethod
	def rp_get_in_bulk(lst_ids):
		return Reserva.objects.in_bulk(id_list=lst_ids, field_name='id')

	@staticmethod
	def rp_create_obj(dict_data=None):
		return Reserva(codigo_reserva=dict_data.get('codigo_reserva'),
						id_anuncio=dict_data.get('id_anuncio'),
						data_check_in=dict_data.get('data_check_in'),
						data_check_out=dict_data.get('data_check_out'),
						preco_total=dict_data.get('preco_total'),
						comentario=dict_data.get('comentario'),
						quantidade_hospede=dict_data.get('quantidade_hospede'))

	@staticmethod
	def rp_save_bulk_create(list_obj=None):
		Reserva.objects.bulk_create(list_obj)