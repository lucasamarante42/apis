
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