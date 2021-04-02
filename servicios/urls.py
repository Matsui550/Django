from django.urls import path

from . import views
# para importar y poder ver als imagenes en el panel de control
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.servicios, name="Servicios"),
]