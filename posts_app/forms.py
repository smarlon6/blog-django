from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts # nosso modelo
        fields = ['title', 'description', 'image'] # campos do nosso modelo poderia ser '__all__'