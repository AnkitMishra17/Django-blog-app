from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']


#172.16.68.6:8090
