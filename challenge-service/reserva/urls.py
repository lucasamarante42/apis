from django.urls import include, path, re_path
from . import views
from django.conf import settings

from rest_framework_bulk.routes import BulkRouter

router = BulkRouter()

path_reserva = '{}/reserva'.format(settings.API_PATH)

router.register(r'{}/bulk'.format(path_reserva), views.bulk_methods, base_name='bulk')

urlpatterns = [
	re_path(r'^{}/(?P<pk>[0-9]+)$'.format(path_reserva),
		views.get_delete.as_view(),
		name='get_delete'
	),
	path(path_reserva,
		views.get_post.as_view(),
		name='get_post'
	)
]

urlpatterns += router.urls