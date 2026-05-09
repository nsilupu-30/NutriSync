# nutricion/forms.py

from django import forms
from .models import PerfilUsuario, RegistroHabito, ItemRegistro


# =========================
# CLASES TAILWIND
# =========================
TW_INPUT = "w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500"
TW_SELECT = "w-full border border-gray-300 rounded-lg px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-green-500"


# =========================
# PERFIL USUARIO
# =========================
class PerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = [
            "peso_kg",
            "talla_cm",
            "edad",
            "sexo",
            "nivel_actividad",
            "objetivo",
        ]
        widgets = {
            "peso_kg": forms.NumberInput(attrs={"class": TW_INPUT}),
            "talla_cm": forms.NumberInput(attrs={"class": TW_INPUT}),
            "edad": forms.NumberInput(attrs={"class": TW_INPUT}),
            "sexo": forms.Select(attrs={"class": TW_SELECT}),
            "nivel_actividad": forms.Select(attrs={"class": TW_SELECT}),
            "objetivo": forms.Select(attrs={"class": TW_SELECT}),
        }


# =========================
# REGISTRO HÁBITOS
# =========================
class RegistroHabitoForm(forms.ModelForm):
    class Meta:
        model = RegistroHabito
        fields = [
            "fecha",
            "vasos_agua",
            "horas_sueno",
            "pasos",
            "minutos_ejercicio",
            "tipo_ejercicio",
        ]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date", "class": TW_INPUT}),
            "vasos_agua": forms.NumberInput(attrs={"class": TW_INPUT}),
            "horas_sueno": forms.NumberInput(attrs={"class": TW_INPUT}),
            "pasos": forms.NumberInput(attrs={"class": TW_INPUT}),
            "minutos_ejercicio": forms.NumberInput(attrs={"class": TW_INPUT}),
            "tipo_ejercicio": forms.Select(attrs={"class": TW_SELECT}),
        }


# =========================
# ITEM REGISTRO (COMIDA)
# =========================
class ItemRegistroForm(forms.ModelForm):
    class Meta:
        model = ItemRegistro
        fields = [
            "alimento",
            "cantidad_g",
        ]
        widgets = {
            "alimento": forms.Select(attrs={"class": TW_SELECT}),
            "cantidad_g": forms.NumberInput(attrs={"class": TW_INPUT}),
        }