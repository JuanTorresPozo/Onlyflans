from django.db import models
import uuid

# Create your models (class)(tabla) here.
class Flan(models.Model):
    #nombre_atributo = tipo_de_dato
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)  #varchar
    descripcion = models.TextField()
    image_url = models.URLField()
    url = models.CharField(max_length=64)
    slug= models.SlugField()
    id_private= models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"objeto Flan: ({self.id}) - {self.name}"
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False) #con valor por defecto uuid.uuid4, no editable
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64) 
    message = models.TextField()
    
    def __str__(self) -> str:
        return f"Contact Form: ({self.id}) - {self.customer_email}"
        
        
        