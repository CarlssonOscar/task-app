from django import forms


class TaskForm(forms.Form):
    # Add task text
    task_input = forms.CharField(max_length=45, widget=forms.TextInput(
        attrs={}))
    # add attributes when html is done
