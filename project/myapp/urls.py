from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LibroViewSet
from django.urls import path, include
from django.contrib import admin
from myapp import views


router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', views.PaginaPrincipalView.as_view(), name='index'),

    # Autores
    path('autores/', views.AutorListView.as_view(), name='lista_autores'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='detalle_autor'),
    path('autores/nuevo/', views.AutorCreateView.as_view(), name='add_autor'),
    path('autores/<int:pk>/edit/', views.AutorUpdateView.as_view(), name='edit_autor'),
    path('autores/<int:pk>/delete/', views.AutorDeleteView.as_view(), name='delete_autor'),

    # Libros
    path('libros/', views.LibroListView.as_view(), name='lista_libros'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='detalle_libro'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='add_book'),
    path('libros/<int:pk>/edit/', views.LibroUpdateView.as_view(), name='edit_book'),
    path('libros/<int:pk>/delete/', views.LibroDeleteView.as_view(), name='delete_book'),

    # Autenticación
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #api
     path('api/', include(router.urls)),
]
