# facturacion/validators.py
# Validadores del módulo de Facturación.

from django.core.exceptions import ValidationError
from decimal import Decimal


def validate_monto_positivo(value):
    """Valida que el monto sea un valor positivo."""
    if value is not None and value <= 0:
        raise ValidationError("El monto debe ser mayor a cero.")


def validate_monto_maximo(value):
    """Valida que el monto no supere el límite razonable."""
    if value is not None and value > 999999.99:
        raise ValidationError("El monto no puede superar S/ 999,999.99.")


def validate_porcentaje(value):
    """Valida que el porcentaje esté entre 0 y 100."""
    if value is not None:
        if value < 0 or value > 100:
            raise ValidationError("El porcentaje debe estar entre 0 y 100.")
