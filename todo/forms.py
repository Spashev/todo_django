from django import forms 
from todo.models import Todo

class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'form-control form-control-alt'
        self.fields['status'].widget.attrs['class'] = 'form-control form-control-alt'

    class Meta:
        model = Todo 
        fields = '__all__'