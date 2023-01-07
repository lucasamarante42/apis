from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import ImovelSerializer, ImovelSerializers, BulkImovelSerializer
from .business import ImovelBusiness
from .filters import ImovelFilter

from challenge_geral.utils import check_filtered_params_exists

from rest_framework_tracking.mixins import LoggingMixin
from challenge_geral.views import MultiObjectCreateAPIView, MultiObjectUpdateDestroyAPIView
from rest_framework_bulk import BulkModelViewSet

"""
 View genérica RetrieveUpdateDestroyAPIView => utilizado para método GET, PUT e DELETE (por ID)

 Classe: get_delete_update

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
"""
class get_delete_update(LoggingMixin, RetrieveUpdateDestroyAPIView):

	def should_log(self, request, response):
		return (request.method == 'GET' and response.status_code != 200) or request.method != 'GET'

	queryset = ImovelBusiness.bs_get_all()
	serializer_class = ImovelSerializer

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

	queryset = ImovelBusiness.bs_get_all()
	serializer_class = ImovelSerializer

	filterset_class = ImovelFilter

"""
 View MultiObjectCreateAPIView => utilizado para método POST
 (criação de múltiplos objetos)

 Classe: post_list

 Variáveis:
	serializer_class => serializer do model
"""
class post_list(LoggingMixin, MultiObjectCreateAPIView):

	serializer_class = ImovelSerializer

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
	queryset = ImovelBusiness.bs_get_all()
	serializer_class = BulkImovelSerializer

	filterset_class = ImovelFilter

	def allow_bulk_destroy(self, qs, filtered):
		filters = list(self.filterset_class.get_fields().keys())
		return check_filtered_params_exists(self.request.query_params, filters, filtered)