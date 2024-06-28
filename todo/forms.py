from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status']


class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(choices=[('', 'All'), ('completed', 'Completed'), ('not_completed', 'Not Completed')], required=False)
