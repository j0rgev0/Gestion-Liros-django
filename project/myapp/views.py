
from django.views.generic import TemplateView, ListView, DetailView
from .models import Libro, Autor

class PaginaPrincipalView(TemplateView):
    template_name = 'index.html'

class AutorListView(ListView):
    model = Autor
    template_name = 'lista_autores.html'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'detalle_autor.html'
    context_object_name = 'autor'

class LibroListView(ListView):
    model = Libro
    template_name = 'lista_libros.html'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'detalle_libro.html'
    context_object_name = 'libro'