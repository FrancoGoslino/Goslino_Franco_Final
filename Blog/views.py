from django.shortcuts import render
from Blog.models import Receta, Mensaje, Perfil
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "Blog/index.html")


class RecetaList(ListView):
    model = Receta
    context_object_name= "recetas"

class RecetaMineList(LoginRequiredMixin, RecetaList):
    
    def get_queryset(self):
        return Receta.objects.filter(propietario=self.request.user.id).all()



class RecetaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    success_url = reverse_lazy("receta-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        receta_id =  self.kwargs.get("pk")
        return Receta.objects.filter(propietario=user_id, id=receta_id).exists()

class RecetaDetail(DetailView):
    model=Receta

class RecetaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receta
    context_object_name= "receta"
    success_url = reverse_lazy("receta-list")

    def test_func(self):
        user_id = self.request.user.id
        receta_id =  self.kwargs.get("pk")
        return Receta.objects.filter(propietario=user_id, id=receta_id).exists()


class RecetaCreate(LoginRequiredMixin, CreateView):
    model = Receta
    success_url = reverse_lazy("receta-list")
    fields = [ 'nombre' ,'detalle', 'precio' ,'imagen']

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)



class RecetaSearch(ListView):
    model = Receta
    context_object_name = 'recetas' 
    
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        resultado = Receta.objects.filter(nombre__icontains=criterio).all()
        return resultado

class Login(LoginView):
    next_page = reverse_lazy("receta-list")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('receta-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"


#-------MENSJAERIA---------------------------------->

class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'
    
class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    
class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()
    
    
 #-------PERFIL---------------------------------->
    
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Perfil
    success_url = reverse_lazy("receta-list")
    fields = ['avatar','redes_sociales', 'user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PerfilUpDate(UserPassesTestMixin, UpdateView):
    model = Perfil
    success_url = reverse_lazy('receta-list')
    fields = ['avatar','redes_sociales', 'user']
    
    def test_func(self):
        return Perfil.objects.filter(user=self.request.user).exists()
    