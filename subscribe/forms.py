from django import forms

class Subscribe(forms.Form):
    email = forms.CharField()
    # name = forms.CharField(max_length=100)
    # age = forms.IntegerField()

    # def __str__(self):
    #     return self.email

