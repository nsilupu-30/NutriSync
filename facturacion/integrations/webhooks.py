# facturacion/integrations/webhooks.py
# Webhooks de Stripe para manejar eventos de pago.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from facturacion.integrations.stripe_service import verificar_webhook
from facturacion.models import Pago, Cobro, Factura, SuscripcionNutricionista
from facturacion.choices import EstadoPago, EstadoCobro, EstadoFactura, EstadoSuscripcion
import json


@csrf_exempt
@require_POST
def stripe_webhook(request):
    """Endpoint para recibir webhooks de Stripe."""
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    event = verificar_webhook(payload, sig_header)
    if event is None:
        return HttpResponse(status=400)

    # Manejar eventos
    if event["type"] == "payment_intent.succeeded":
        handle_payment_succeeded(event["data"]["object"])
    elif event["type"] == "payment_intent.payment_failed":
        handle_payment_failed(event["data"]["object"])
    elif event["type"] == "invoice.payment_succeeded":
        handle_invoice_payment_succeeded(event["data"]["object"])
    elif event["type"] == "invoice.payment_failed":
        handle_invoice_payment_failed(event["data"]["object"])
    elif event["type"] == "customer.subscription.deleted":
        handle_subscription_deleted(event["data"]["object"])

    return HttpResponse(status=200)


def handle_payment_succeeded(payment_intent):
    """Maneja un pago exitoso."""
    stripe_id = payment_intent["id"]
    pagos = Pago.objects.filter(stripe_payment_intent_id=stripe_id)
    for pago in pagos:
        pago.estado = EstadoPago.COMPLETADO
        pago.save(update_fields=["estado"])

        # Actualizar cobro asociado
        if pago.cobro:
            pago.cobro.estado = EstadoCobro.PAGADO
            pago.cobro.fecha_pago = timezone.now()
            pago.cobro.metodo_pago_usado = "stripe"
            pago.cobro.save()

        # Actualizar factura asociada
        if pago.factura:
            pago.factura.estado = EstadoFactura.PAGADA
            pago.factura.save(update_fields=["estado"])


def handle_payment_failed(payment_intent):
    """Maneja un pago fallido."""
    stripe_id = payment_intent["id"]
    pagos = Pago.objects.filter(stripe_payment_intent_id=stripe_id)
    for pago in pagos:
        pago.estado = EstadoPago.FALLIDO
        pago.save(update_fields=["estado"])


def handle_invoice_payment_succeeded(invoice):
    """Maneja el pago exitoso de una factura de suscripción."""
    subscription_id = invoice.get("subscription")
    if subscription_id:
        suscripcion = SuscripcionNutricionista.objects.filter(
            stripe_subscription_id=subscription_id
        ).first()
        if suscripcion:
            suscripcion.estado = EstadoSuscripcion.ACTIVA
            suscripcion.save(update_fields=["estado"])


def handle_invoice_payment_failed(invoice):
    """Maneja el pago fallido de una factura de suscripción."""
    subscription_id = invoice.get("subscription")
    if subscription_id:
        suscripcion = SuscripcionNutricionista.objects.filter(
            stripe_subscription_id=subscription_id
        ).first()
        if suscripcion:
            suscripcion.estado = EstadoSuscripcion.VENCIDA
            suscripcion.save(update_fields=["estado"])


def handle_subscription_deleted(subscription):
    """Maneja la eliminación de una suscripción."""
    stripe_id = subscription["id"]
    suscripcion = SuscripcionNutricionista.objects.filter(
        stripe_subscription_id=stripe_id
    ).first()
    if suscripcion:
        suscripcion.estado = EstadoSuscripcion.CANCELADA
        suscripcion.save(update_fields=["estado"])
