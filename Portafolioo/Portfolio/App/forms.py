from django import forms

class FormContacto(forms.Form):
    nombrepersona = forms.CharField(label='Nombre', max_length=200)
    correo = forms.EmailField(label='Correo') 
    mensaje = forms.CharField(label='Mensaje', max_length=200)
    asunto = forms.CharField(label='Asunto', max_length=200)
    
    
