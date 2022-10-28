from django import forms
from spgdt.models import Pbfree


class AddpbfreeForm(forms.ModelForm):
    class Meta:
        model = Pbfree
        # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        fields = ['nama', 'jk', 'td', 'usia', 'dx', 'alamat', 'nohp', 'tgl']
        # widgets = {'nama': forms.TextInput(attrs={'class': 'form-control'}),
        #            'jk': forms.TextInput(attrs={'class': 'form-control'}),
        #            'td': forms.TextInput(attrs={'class': 'form-control'}),
        #            'usia': forms.TextInput(attrs={'class': 'form-control'}),
        #            'dx': forms.TextInput(attrs={'class': 'form-control'}),
        #            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
        #            'nohp': forms.TextInput(attrs={'class': 'form-control'}),
        #            'tgl': forms.TextInput(attrs={'class': 'form-control'}),
        #            }
