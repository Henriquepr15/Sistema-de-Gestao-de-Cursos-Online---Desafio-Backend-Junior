from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from courses.views import homepage  # Certifique-se de que este import está correto

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Online Courses API",
        default_version='v1',
        description="API para Gerenciamento de Cursos Online",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@cursosonline.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

# Página inicial alternativa para debug
def homepage_debug(request):
    return HttpResponse("<h1>Bem-vindo à API de Gerenciamento de Cursos Online!</h1>")

# Configuração das URLs principais
urlpatterns = [
    # Página inicial - usando a view 'homepage' do app 'courses'
    path('', homepage, name='homepage'),

    # Django Admin
    path('admin/', admin.site.urls),

    # Swagger - Documentação da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # JWT Autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # URLs do app "courses"
    path('api/', include('courses.urls')),  # Certifique-se de que o arquivo courses/urls.py está configurado corretamente
]
