from django import forms
from .models import RendicionDetalle
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class RendicionDetalleForm(forms.ModelForm):
    class Meta:
        model = RendicionDetalle
        fields = ('nombre', 'descripcion', 'monto_neto', 'monto_iva')

    def __init__(self, *args, **kwargs):
        super(RendicionDetalleForm, self).__init__(*args, **kwargs)
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
            Row(
                Column('monto_neto', css_class='form-group col-md-6 mb-0'),
                Column('monto_iva', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar')
        )