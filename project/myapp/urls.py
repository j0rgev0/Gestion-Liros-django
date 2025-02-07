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
    path('autores/nuevo/', views.AutorCreateView.as_view(), name='add_autor'),
    path('autores/<int:pk>/edit/', views.AutorUpdateView.as_view(), name='edit_autor'),
    path('autores/<int:pk>/delete/', views.AutorDeleteView.as_view(), name='delete_autor'),
    
]
