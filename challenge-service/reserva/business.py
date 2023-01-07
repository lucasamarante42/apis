
from .repositories import ReservaRepositories
from challenge_geral.utils import mount_list_ids

class ReservaBusiness:

	@staticmethod
	def bs_get_all():
		return ReservaRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return ReservaRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_delete(pk):
		return ReservaRepositories.rp_delete_by_id(pk)

	@staticmethod
	def bs_get_by_ids(data):
		lst_ids = mount_list_ids(data)
		return ReservaRepositories.rp_get_in_bulk(lst_ids)