from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from todo.views import TodoViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register('todo', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('api/', include(route.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

