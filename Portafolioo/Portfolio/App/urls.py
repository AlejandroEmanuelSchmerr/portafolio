from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('acerca',views.acerca,name="Acercade"),
    path('contactos',views.contactos,name="Contacto"),
    path('proyectos',views.proyectos,name="Proyectos"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)