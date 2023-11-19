from django import forms
from Posts_App.models import PostModel

class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ['post_image', 'caption']

