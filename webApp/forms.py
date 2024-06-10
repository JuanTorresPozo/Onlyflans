from django import forms
  
class ContacFormForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre") 
    message = forms.CharField(label="Mensaje")
    
    
