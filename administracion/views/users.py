# administracion/views/users.py
# Gestión de nutricionistas (usuarios) del panel de administración.

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from administracion.mixins import admin_requerido
from core.models import Rol
from config.choices import EstadoNutricionista


@admin_requerido
def usuarios_lista_view(request):
    """Lista de nutricionistas con filtros y búsqueda."""
    queryset = User.objects.filter(perfil__rol=Rol.NUTRICIONISTA).select_related('perfil', 'suscripcion__plan').order_by('-date_joined')

    # Búsqueda y filtrado
    q = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '').strip()

    if q:
        queryset = queryset.filter(
            Q(username__icontains=q) |
            Q(perfil__nombre_completo__icontains=q) |
            Q(email__icontains=q)
        )
    if estado:
        queryset = queryset.filter(perfil__estado=estado)

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'q': q,
        'estado_filtro': estado,
        'estados': EstadoNutricionista.CHOICES,
    }
    return render(request, 'administracion/users/list.html', context)


@admin_requerido
def usuario_detalle_view(request, pk):
    """Detalle de perfil, suscripción y métricas del nutricionista."""
    usuario = get_object_or_404(User, pk=pk, perfil__rol=Rol.NUTRICIONISTA)

    # Cantidad total de pacientes y citas
    total_pacientes = usuario.pacientes.count()
    total_citas = usuario.citas_creadas.count()

    # Últimos 5 cobros del nutricionista
    ultimos_cobros = usuario.cobros.all().order_by('-fecha_creacion')[:5]

    context = {
        'usuario': usuario,
        'total_pacientes': total_pacientes,
        'total_citas': total_citas,
        'ultimos_cobros': ultimos_cobros,
    }
    return render(request, 'administracion/users/detail.html', context)


@admin_requerido
@require_POST
def usuario_toggle_estado(request, pk):
    """Activa o suspende temporalmente el acceso del nutricionista."""
    usuario = get_object_or_404(User, pk=pk, perfil__rol=Rol.NUTRICIONISTA)
    perfil = usuario.perfil

    if perfil.estado == EstadoNutricionista.HABILITADO:
        perfil.estado = EstadoNutricionista.DESHABILITADO
        messages.warning(request, f"La cuenta de {perfil.nombre_completo} ha sido suspendida.")
    else:
        perfil.estado = EstadoNutricionista.HABILITADO
        messages.success(request, f"La cuenta de {perfil.nombre_completo} ha sido habilitada.")

    perfil.save()
    return redirect('administracion:usuario_detalle', pk=pk)
