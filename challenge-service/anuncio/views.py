from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import AnuncioSerializer, AnuncioSerializers, BulkAnuncioSerializer
from .business import AnuncioBusiness
from .filters import AnuncioFilter

from challenge_geral.utils import check_filtered_params_exists

from rest_framework_tracking.mixins import LoggingMixin
from challenge_geral.views import MultiObjectCreateAPIView, MultiObjectUpdateDestroyAPIView
from rest_framework_bulk import BulkModelViewSet

"""
 View genérica RetrieveUpdateAPIView => utilizado para método GET e PUT (por ID)

 Classe: get_update

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
"""
class get_update(LoggingMixin, RetrieveUpdateAPIView):

	def should_log(self, request, response):
		return (request.method == 'GET' and response.status_code != 200) or request.method != 'GET'

	queryset = AnuncioBusiness.bs_get_all()
	serializer_class = AnuncioSerializer

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

	queryset = AnuncioBusiness.bs_get_all()
	serializer_class = AnuncioSerializer

	filterset_class = AnuncioFilter

"""
 View MultiObjectCreateAPIView => utilizado para método POST
 (criação de múltiplos objetos)

 Classe: post_list

 Variáveis:
	serializer_class => serializer do model
"""
class post_list(LoggingMixin, MultiObjectCreateAPIView):

	serializer_class = AnuncioSerializer

"""
 View MultiObjectUpdateDestroyAPIView => utilizado para método PUT
 (atualização de múltiplos objetos)

 Classe: update_bulk

 Variáveis:
	bussiness_class => bussiness
	serializer_class => serializer do model
"""
class update_bulk(LoggingMixin,	MultiObjectUpdateDestroyAPIView):

	bussiness_class = AnuncioBusiness
	serializer_class = AnuncioSerializers

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
	queryset = AnuncioBusiness.bs_get_all()
	serializer_class = BulkAnuncioSerializer

	filterset_class = AnuncioFilter

	def allow_bulk_destroy(self, qs, filtered):
		filters = list(self.filterset_class.get_fields().keys())
		return check_filtered_params_exists(self.request.query_params, filters, filtered)