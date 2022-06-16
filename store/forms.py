from .models import documents 
from django import forms  
      
class UserImage(forms.ModelForm):  
    class meta:  
        models = documents 
        fields = '__all__'  