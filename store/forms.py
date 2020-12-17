from django import forms
from .models import Artist

class ContactForm(forms.ModelForm):
    
  # create meta class 
  class Meta: 
      # specify model to be used 
      model = Artist 

      # specify fields to be used 
      fields = [ 
          "name", 
          "instrument", 
      ] 

  
  
