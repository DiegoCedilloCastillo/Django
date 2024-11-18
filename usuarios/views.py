from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm

# Listar usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuarios.html'
    context_object_name = 'usuarios'

# Detalle de usuario
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/detalle_usuario.html'

# Crear usuario
class UsuarioCreateView(SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('listar_usuarios')
    success_message = "Usuario creado exitosamente."

# Editar usuario
class UsuarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('listar_usuarios')
    success_message = "Usuario actualizado correctamente."

# Eliminar usuario
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('listar_usuarios')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Usuario eliminado con éxito.")
        return super().delete(request, *args, **kwargs)