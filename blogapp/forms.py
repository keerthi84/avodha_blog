from django import forms
from . models import blog

class postform(forms.ModelForm):
    class Meta:
        model=blog
        fields=['title','title_tag','author','body','img','date']

        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-group'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }