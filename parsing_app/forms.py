from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 12, 'cols': 100}))
