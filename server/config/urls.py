from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.frontend.urls')),
    path('api/', include('service.backend.urls'), name='api'),
    path('wechat/', include('service.wechat.urls')),
    path('docs/', get_swagger_view(title='API docs')),
]

if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
