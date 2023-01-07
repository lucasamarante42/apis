from django.urls import include, path, re_path
from . import views
from django.conf import settings

from rest_framework_bulk.routes import BulkRouter

router = BulkRouter()

path_anuncio = '{}/anuncio'.format(settings.API_PATH)

router.register(r'{}/bulk'.format(path_anuncio), views.bulk_methods, base_name='bulk')

urlpatterns = [
	re_path(r'^{}/(?P<pk>[0-9]+)$'.format(path_anuncio),
		views.get_update.as_view(),
		name='get_update'
	),
	path(path_anuncio,
		views.get_post.as_view(),
		name='get_post'
	),
	path('{}/create-multiple'.format(path_anuncio),
		views.post_list.as_view(),
		name='post_list'
	),
	path('{}/update-bulk'.format(path_anuncio),
		views.update_bulk.as_view(),
		name='update_bulk'
	),
]

urlpatterns += router.urls