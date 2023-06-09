"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog.views import (index, RecetaList, RecetaSearch, RecetaCreate, RecetaDelete, RecetaUpdate, RecetaMineList, 
                        RecetaDetail, Login, Logout, SignUp, MensajeCreate, MensajeDelete, MensajeList, PerfilUpDate, ProfileCreate
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "index/"),
    path('receta/list', RecetaList.as_view(), name= 'receta-list'),
    path('receta/mine/list', RecetaMineList.as_view(), name= 'receta-mine'),
    path('receta/<pk>/update', RecetaUpdate.as_view(), name= 'receta-update'),
    path('receta/<pk>/delete', RecetaDelete.as_view(), name= 'receta-delete'),
    path('receta/create', RecetaCreate.as_view(), name= 'receta-create'),
    path('receta/buscar', RecetaSearch.as_view(), name= 'receta-buscar'),
    path('receta/<pk>/detail', RecetaDetail.as_view(), name= 'receta-detail'),
    path('login', Login.as_view(), name= 'login'),
    path('logout', Logout.as_view(), name= 'logout'),
    path('signup', SignUp.as_view(), name= 'signup'),
    path('mensaje/create', MensajeCreate.as_view(), name='mensaje-create'),
    path('mensaje/list', MensajeList.as_view(), name='mensaje-list'),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name='mensaje-delete'),
    path('perfil/create', ProfileCreate.as_view(), name='perfil-create'),
    path('perfil/<pk>/update', PerfilUpDate.as_view(), name='perfil-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)