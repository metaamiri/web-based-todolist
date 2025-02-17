from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'enter your todo'}))