
from .models import Anuncio
from challenge_geral.utils import get_datetime_now

class AnuncioRepositories():

	@staticmethod
	def rp_get_all():
		return Anuncio.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return Anuncio.objects.get(pk=pk)
		except Anuncio.DoesNotExist:
			return None

	@staticmethod
	def rp_delete_by_id(pk):
		obj = AnuncioRepositories.rp_get_by_id(pk)
		if obj:
			obj.data_remocao = get_datetime_now('datetime')
			obj.save()
			return True
		return False

	@staticmethod
	def rp_get_in_bulk(lst_ids):
		return Anuncio.objects.in_bulk(id_list=lst_ids, field_name='id')