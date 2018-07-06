from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='ToDo App API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api-auth/', include(('rest_framework.urls', None), namespace='rest_framework')),

    # url(r'^api/api-test/', include(('apps.api-test.urls', 'api-test'), namespace='api-test')),
    url(r'^api/', include(('apps.quotes.api.urls', 'quotes'), namespace='quotes')),

    # Swagger
    url('^api/schema/$', schema_view)
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
