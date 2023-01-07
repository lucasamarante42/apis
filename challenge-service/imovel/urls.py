from django.urls import include, path, re_path
from . import views
from django.conf import settings

from rest_framework_bulk.routes import BulkRouter

router = BulkRouter()

path_imovel = '{}/imovel'.format(settings.API_PATH)

router.register(r'{}/bulk'.format(path_imovel), views.bulk_methods, base_name='bulk')

urlpatterns = [
	re_path(r'^{}/(?P<pk>[0-9]+)$'.format(path_imovel),
		views.get_delete_update.as_view(),
		name='get_delete_update'
	),
	path(path_imovel,
		views.get_post.as_view(),
		name='get_post'
	),
	path('{}/create-multiple'.format(path_imovel),
		views.post_list.as_view(),
		name='post_list'
	)
]

urlpatterns += router.urls