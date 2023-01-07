
from .repositories import AnuncioRepositories
from challenge_geral.utils import mount_list_ids

class AnuncioBusiness:

	@staticmethod
	def bs_get_all():
		return AnuncioRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return AnuncioRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_delete(pk):
		return AnuncioRepositories.rp_delete_by_id(pk)

	@staticmethod
	def bs_get_by_ids(data):
		lst_ids = mount_list_ids(data)
		return AnuncioRepositories.rp_get_in_bulk(lst_ids)