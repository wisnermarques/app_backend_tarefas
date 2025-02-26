from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views  # Para autenticação por token

urlpatterns = [
    # URL do painel de administração do Django
    path('admin/', admin.site.urls),

    # URLs da API de tarefas
    path('api/', include('tarefas.urls')),

    # Autenticação por token (opcional, se estiver usando TokenAuthentication)
    path('api-token-auth/', auth_views.obtain_auth_token),
    
]