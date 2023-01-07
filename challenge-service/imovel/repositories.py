
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