from django import forms 
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):  
    class Meta:
        model = StudentModel
        # fields = ['name', 'roll'] # only ai 2 ta show korbe
        # exclude = ['roll] # roll bade baki shob gula show korbe
        fields = '__all__' # shob gula show korbe
        
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            # 'roll' : forms.PasswordInput()
        }
        
        help_texts = {
            'name' : "write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }