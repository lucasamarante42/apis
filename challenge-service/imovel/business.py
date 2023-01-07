
from .repositories import ImovelRepositories
from challenge_geral.utils import mount_list_ids

class ImovelBusiness:

	@staticmethod
	def bs_get_all():
		return ImovelRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return ImovelRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_delete(pk):
		return ImovelRepositories.rp_delete_by_id(pk)

	@staticmethod
	def bs_get_by_ids(data):
		lst_ids = mount_list_ids(data)
		return ImovelRepositories.rp_get_in_bulk(lst_ids)