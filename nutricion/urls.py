# nutricion/urls.py

from django.urls import path
from . import views, views_auth

app_name = "nutricion"

urlpatterns = [
    # ======================
    # DASHBOARD
    # ======================
    path("", views.dashboard, name="dashboard"),

    # ======================
    # AUTH
    # ======================
    path("login/", views_auth.login_view, name="login"),
    path("logout/", views_auth.logout_view, name="logout"),
    path("registro/", views_auth.registro_view, name="registro"),

    # ======================
    # PERFIL
    # ======================
    path("perfil/", views_auth.perfil_view, name="perfil"),

    # ======================
    # COMIDAS
    # ======================
    path("comidas/", views.lista_comidas, name="lista_comidas"),
    path("comidas/nueva/", views.crear_comida, name="crear_comida"),

    # ======================
    # HÁBITOS
    # ======================
    path("habitos/", views.lista_habitos, name="lista_habitos"),

    # ======================
    # LOGROS
    # ======================
    path("logros/", views.logros_view, name="logros"),
]