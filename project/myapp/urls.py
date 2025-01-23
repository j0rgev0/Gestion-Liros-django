from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PaginaPrincipalView.as_view(), name='index'),
    path('autores/', views.AutorListView.as_view(), name='lista_autores'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='detalle_autor'),
    path('libros/', views.LibroListView.as_view(), name='lista_libros'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='detalle_libro'),
]
