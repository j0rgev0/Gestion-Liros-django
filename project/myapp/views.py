from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Libro, Autor
from .serializers import AutorSerializer, LibroSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # Redirige si ya está autenticado
    success_url = reverse_lazy('index')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro exitoso. Ahora puedes iniciar sesión ✅")
        return response

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

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    template_name = 'add_autor.html'
    fields = ['nombre', 'apellido', 'fecha_nacimiento']
    success_url = reverse_lazy('lista_autores')

    def form_valid(self, form):
        messages.success(self.request, "Autor añadido correctamente ✅")
        return super().form_valid(form)

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'add_book.html'
    fields = ['titulo', 'fecha_publi', 'genero', 'isbn', 'autor']
    success_url = reverse_lazy('lista_libros')

    def form_valid(self, form):
        messages.success(self.request, "Libro añadido correctamente ✅")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al añadir el libro ❌")
        return self.render_to_response(self.get_context_data(form=form))

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'fecha_nacimiento']
    template_name = 'edit_autor.html'
    success_url = reverse_lazy('lista_autores')

    def form_valid(self, form):
        messages.success(self.request, "Autor actualizado correctamente ✅")
        return super().form_valid(form)

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = 'edit_book.html'
    fields = ['titulo', 'fecha_publi', 'genero', 'isbn', 'autor']
    success_url = reverse_lazy('lista_libros')

    def form_valid(self, form):
        messages.success(self.request, "Libro actualizado correctamente ✅")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el libro ❌")
        return self.render_to_response(self.get_context_data(form=form))

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = 'delete_autor.html'
    success_url = reverse_lazy('lista_autores')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Autor eliminado correctamente ✅")
        return super().delete(request, *args, **kwargs)

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'delete_book.html'
    success_url = reverse_lazy('lista_libros')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Libro eliminado correctamente ✅")
        return super().delete(request, *args, **kwargs)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]