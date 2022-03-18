from django import forms
from .models import Cliente, Sitios_cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class FormularioCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('direccion', css_class='form-group col-md-6 mb-0'),
            css_class='row-fluid'
            ), 
            Row(
                Column('telefono', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
            css_class='row-fluid'
            ), 
            Submit('submit', 'Enviar', css_class='d-grid gap-2 col-2 mx-auto')
        )

class FormularioSitioCliente(forms.ModelForm):

    class Meta:
        model = Sitios_cliente
        fields = ['nombre', 'direccion', 'telefono', 'email', 'encargado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('direccion', css_class='form-group col-md-6 mb-0'),
            css_class='row-fluid'
            ), 
            Row(
                Column('telefono', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('encargado', css_class='form-group col-md-4 mb-0'),
            css_class='row-fluid'
            ), 
            Submit('submit', 'Enviar', css_class='d-grid gap-2 col-2 mx-auto')
        )
