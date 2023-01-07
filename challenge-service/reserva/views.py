from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from .serializers import ReservaSerializer, ReservaSerializers, BulkReservaSerializer
from .business import ReservaBusiness
from .filters import ReservaFilter

from challenge_geral.utils import check_filtered_params_exists

from rest_framework_tracking.mixins import LoggingMixin
from challenge_geral.views import MultiObjectCreateAPIView, MultiObjectUpdateDestroyAPIView
from rest_framework_bulk import BulkModelViewSet

"""
 View genérica RetrieveDestroyAPIView => utilizado para método GET e DELETE (por ID)

 Classe: get_delete

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
"""
class get_delete(LoggingMixin, RetrieveDestroyAPIView):

	def should_log(self, request, response):
		return (request.method == 'GET' and response.status_code != 200) or request.method != 'GET'

	queryset = ReservaBusiness.bs_get_all()
	serializer_class = ReservaSerializer

"""
 View genérica ListCreateAPIView => utilizado para método GET e POST

 Classe: get_post

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
	filterset_class => filtro do model
"""
class get_post(LoggingMixin, ListCreateAPIView):

	def should_log(self, request, response):
		return request.method == 'GET' and response.status_code != 200

	queryset = ReservaBusiness.bs_get_all()
	serializer_class = ReservaSerializer

	filterset_class = ReservaFilter

"""
 View BulkModelViewSet => utilizado para método GET/DELETE
	=> ação em múltiplos objetos

 Classe: bulk_methods

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
	filterset_class => filtro do model

 Métodos:
	allow_bulk_destroy => lógica para evitar a exclusão em massa
							sem filtro
"""
class bulk_methods(LoggingMixin, BulkModelViewSet):
	queryset = ReservaBusiness.bs_get_all()
	serializer_class = BulkReservaSerializer

	filterset_class = ReservaFilter

	def allow_bulk_destroy(self, qs, filtered):
		filters = list(self.filterset_class.get_fields().keys())
		return check_filtered_params_exists(self.request.query_params, filters, filtered)