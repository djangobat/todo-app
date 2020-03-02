from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.core.urls')),
    path('users/', include('apps.users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('todos/', include('apps.todos.urls')),
]
