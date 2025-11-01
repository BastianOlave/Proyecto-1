from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Tu Nombre", required=True)
    email = forms.EmailField(label="Tu Email", required=True)
    asunto = forms.CharField(label="Asunto", required=False)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET' 
        self.helper.form_action = '' 
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3')
            ),
            'asunto',
            'mensaje',
            Submit('submit', 'Enviar Mensaje', css_class='btn btn-primary btn-lg px-5 mt-4')
        )