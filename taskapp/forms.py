from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['tasks']
        widgets = {
            'tasks': forms.TextInput(attrs={'size': '37'}),
        }
        
    def __init__(self, *args, **kwargs): 
        super(TaskForm, self).__init__(*args, **kwargs) 
        self.fields['tasks'].label = False
        self.fields['tasks'].widget.attrs['placeholder'] = 'Add a task, date, etc.'