from django import forms

class EmailForm(forms.Form):
    emailto=forms.EmailField()
    subject=forms.CharField(max_length=40)
    text=forms.CharField(widget=forms.Textarea)


