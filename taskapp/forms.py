from django import forms


class TaskForm(forms.ModelForm):
    # Add task text
    class Meta:
        task_input = forms.CharField(max_length=45, widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 
            'Add tasks', 'aria-label' : 'Task', 'aria-describedby' : 'add-btn'}))
    # add attributes when html is done
