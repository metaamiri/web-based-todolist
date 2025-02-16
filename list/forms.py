from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="new task")