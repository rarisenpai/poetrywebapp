from django import forms


from .models import Poems

class PoemsForm(forms.ModelForm):
  class Meta:
    model = Poems
    fields = ('title', 'text')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
      'text': forms.Textarea(attrs={'class': 'form-control my-5'})
    }
    labels = {
      'text': 'poem here'
    }
