from django.urls import path

from . import views
# para importar y poder ver als imagenes en el panel de control

urlpatterns = [

    path('',views.tienda, name="Tienda"),

]