
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView , CreateView , UpdateView , DeleteView
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
    
class AutorCreateView(CreateView):
    model = Autor
    template_name = 'add_autor.html'
    fields = ['nombre', 'apellido', 'fecha_nacimiento']
    success_url = reverse_lazy('lista_autores')
    
class BookCreateView(CreateView):
    model = Libro
    template_name = 'add_book.html'
    fields = ['titulo', 'fecha_publi', 'genero', 'isbn','autor']
    success_url = reverse_lazy('lista_libros')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["autores"] = Autor.objects.all()
        return context
    
class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'fecha_nacimiento']
    template_name = 'edit_autor.html'
    success_url = reverse_lazy('lista_autores')
    

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'delete_autor.html'
    success_url = reverse_lazy('lista_autores')

    