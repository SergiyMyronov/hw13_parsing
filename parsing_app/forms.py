from django import forms


class TaskForm(forms.Form):
    text = forms.Textarea()
