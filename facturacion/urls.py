# facturacion/urls.py
# Rutas del módulo de Facturación y Cobros.

from django.urls import path
from facturacion import views

app_name = "facturacion"

urlpatterns = [
    # Dashboard
    path("", views.facturacion_dashboard, name="dashboard"),
    # Cobros
    path("cobros/", views.CobrosListView.as_view(), name="cobros_lista"),
    path("cobros/crear/", views.CobroCreateView.as_view(), name="cobro_crear"),
    path("cobros/<int:pk>/", views.CobroDetailView.as_view(), name="cobro_detalle"),
    path(
        "cobros/<int:pk>/pago/",
        views.cobro_registrar_pago,
        name="cobro_registrar_pago",
    ),
    path(
        "cobros/cita/<int:cita_pk>/",
        views.cobro_crear_desde_cita,
        name="cobro_desde_cita",
    ),
    # Facturas
    path("facturas/", views.FacturasListView.as_view(), name="facturas_lista"),
    path("facturas/crear/", views.FacturaCreateView.as_view(), name="factura_crear"),
    path(
        "facturas/<int:pk>/", views.FacturaDetailView.as_view(), name="factura_detalle"
    ),
    path(
        "facturas/<int:pk>/item/",
        views.factura_agregar_item,
        name="factura_agregar_item",
    ),
    path(
        "facturas/<int:pk>/cobros/",
        views.factura_agregar_cobros,
        name="factura_agregar_cobros",
    ),
    path(
        "facturas/<int:pk>/emitir/",
        views.factura_emitir,
        name="factura_emitir",
    ),
    path(
        "facturas/<int:pk>/pago/",
        views.factura_registrar_pago,
        name="factura_registrar_pago",
    ),
    # Suscripción
    path("suscripcion/", views.suscripcion_detalle, name="suscripcion_detalle"),
    path(
        "suscripcion/cambiar/",
        views.suscripcion_cambiar_plan,
        name="suscripcion_cambiar",
    ),
    # Reporte de Ingresos
    path("ingresos/", views.ingresos_reporte, name="ingresos_reporte"),
    path(
        "ingresos/exportar/",
        views.ingresos_exportar_csv,
        name="ingresos_exportar_csv",
    ),
    # AJAX
    path(
        "ajax/calcular-igv/",
        views.ajax_calcular_igv,
        name="ajax_calcular_igv",
    ),
    path(
        "ajax/cobros-pendientes/<int:paciente_id>/",
        views.ajax_cobros_pendientes_paciente,
        name="ajax_cobros_pendientes",
    ),
]
