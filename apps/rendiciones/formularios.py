from django import forms
from .models import RendicionDetalle, TipoDeGasto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class RendicionDetalleForm(forms.ModelForm):
    class Meta:
        model = RendicionDetalle
        fields = ('nombre', 'descripcion', 'monto', 'documento', 'kilometraje_inicial', 'kilometraje_final', 'img_km_inicial', 'img_km_final', 'tipo_gasto', 'fecha', 'is_region', 'sitios_cliente')

        labels = {
            'img_km_inicial': 'Imagen del Kilometraje Inicial',
            'img_km_final': 'Imagen del Kilometraje Final',
            'is_region': '¿Es una Rendición de Región?',
            'fecha': 'Fecha de la Rendición',
            'sitios_cliente': 'Sitio',
        }

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(RendicionDetalleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('sitios_cliente', css_class='form-group col-md-6 mb-0'),
                css_class="row-fluid",
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-12 mb-0'),
                css_class="row-fluid",
            ),
            Row(
                Column('fecha', css_class='form-group col-md-6 mb-0'),
                Column('is_region', css_class='form-group col-md-6 mb-0 align-self-center mx-auto text-center'),
            ),
            Row(
                Column('tipo_gasto', css_class='form-group col-md-6 mb-0'),
                Column('monto', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('documento', css_class='form-group col-md-12 mb-0'),
                css_class="row-fluid",
            ),
            Row(
                Column('kilometraje_inicial', css_class='form-group col-md-6 mb-0'),
                Column('kilometraje_final', css_class='form-group col-md-6 mb-0'),
                css_class="row-fluid",
            ),
            Row(
                Column('img_km_inicial', css_class='form-group col-md-6 mb-0'),
                Column('img_km_final', css_class='form-group col-md-6 mb-0'),
                css_class="row-fluid",
            ),

            Submit('submit', 'Guardar')
        )

class FormularioTipoDeGasto(forms.ModelForm):
    class Meta:
        model = TipoDeGasto
        fields = ('nombre', 'descripcion')

        labels = {
            'nombre': 'Nombre del Tipo de Gasto',
            'descripcion': 'Descripción del Tipo de Gasto',
        }

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(FormularioTipoDeGasto, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-12 mb-0'),
                css_class="row-fluid",
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-12 mb-0'),
                css_class="row-fluid",
            ),
            Submit('submit', 'Guardar')
        )