from django.contrib import admin
from django.urls import include,path
from rest_framework.authtoken import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
