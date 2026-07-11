# pacientes/urls.py
# URLs de la app pacientes. Namespace 'pacientes' para referenciar desde templates.

from django.urls import path
from . import views

app_name = "pacientes"

urlpatterns = [
    path("", views.PacienteListView.as_view(), name="lista"),
    path("nuevo/", views.PacienteCreateView.as_view(), name="nuevo"),
    path("<int:pk>/", views.PacienteDetailView.as_view(), name="detalle"),
    path("<int:pk>/editar/", views.PacienteUpdateView.as_view(), name="editar"),
    path("<int:pk>/guardar-informacion/", views.paciente_guardar_informacion, name="guardar_informacion"),
    path("<int:pk>/toggle/", views.paciente_toggle_estado, name="toggle"),
    path("<int:pk>/mediciones/", views.paciente_mediciones_list, name="mediciones_list"),
    path("<int:pk>/mediciones/guardar/", views.paciente_medicion_guardar, name="medicion_guardar"),
    path("<int:pk>/mediciones/<int:medida_id>/eliminar/", views.paciente_medicion_eliminar, name="medicion_eliminar"),
    path("<int:pk>/evaluacion/", views.paciente_evaluacion_get, name="evaluacion_get"),
    path("<int:pk>/evaluacion/guardar/", views.paciente_evaluacion_guardar, name="evaluacion_guardar"),
    path("<int:pk>/plan/", views.paciente_plan_get, name="plan_get"),
    path("<int:pk>/plan/guardar/", views.paciente_plan_guardar, name="plan_guardar"),
    path("<int:pk>/plan/nueva-version/", views.paciente_plan_nueva_version, name="plan_nueva_version"),
    path("<int:pk>/plan/duplicar/", views.paciente_plan_duplicar, name="plan_duplicar"),
    path("<int:pk>/plan/eliminar/", views.paciente_plan_eliminar, name="plan_eliminar"),
    path("<int:pk>/plan/enviar/", views.paciente_plan_enviar, name="plan_enviar"),
    path("<int:pk>/plan/<int:plan_id>/imprimir/", views.paciente_plan_imprimir, name="plan_imprimir"),
    path("<int:pk>/seguimiento/", views.paciente_seguimiento_get, name="seguimiento_get"),
    path("<int:pk>/seguimiento/guardar/", views.paciente_seguimiento_guardar, name="seguimiento_guardar"),
    path("<int:pk>/archivos/", views.paciente_archivos_list, name="archivos_list"),
    path("<int:pk>/archivos/subir/", views.paciente_archivo_subir, name="archivo_subir"),
    path("<int:pk>/archivos/<int:archivo_id>/eliminar/", views.paciente_archivo_eliminar, name="archivo_eliminar"),
]

