from django import forms  # forms api            
from django.core import validators # builtin validator use korar jonno

# widget = field to html input

class contactForm(forms.Form): # froms api theke Form k inherit 
    name = forms.CharField(label = "User Name: ", initial= "Obaydul Hasan Nayeem", help_text="Total length must be within 50 characters", required = False, disabled = False, widget = forms.Textarea(attrs = {'id': 'text_area', 'class': 'class 1 class 2', 'placeholder': 'Enter your name'}))

    email = forms.EmailField(label = "User Email")
    
    age = forms.IntegerField(widget = forms.NumberInput)
   
    weight = forms.FloatField()
    
    balance = forms.DecimalField()
   
    check = forms.BooleanField()
    
    birthday = forms.DateField(widget = forms.DateInput(attrs = {'type': 'date'})) # DateField er jaygay CharField likhleo hobe.
   
    appointment = forms.DateTimeField(widget = forms.DateInput(attrs = {'type': 'datetime-local'}))
    
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)  # ChoiceField er jaygay CharField likhleo hobe.
    
    MEAL = [('P', 'Pepparoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = MEAL, widget=forms.CheckboxSelectMultiple)
    
    # file = forms.FileField() 

# VALIDATION ---------------------------------------------------

# class StudentData(forms.Form):
#     name = forms.CharField(widget = forms.TextInput)
#     email = forms.CharField(widget = forms.EmailInput)
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with atleast 10 characters.")
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("You email must contain .com")
#     #     else:
#     #         return valemail
    
#     def clean(self): # multiple field validate korar jonno
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
        
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with atleast 10 characters.")
        
#         if '.com' not in valemail:
#             raise forms.ValidationError("You email must contain .com")

#BUILT IN VALIDATION ---------------------------------------------

def len_check(value):
    if len(value) < 10: 
        raise forms.ValidationError("Enter a value atleast 10 characters.")

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Enter a name with atleast 10 characters.")])

    text = forms.CharField(widget=forms.TextInput, validators = [len_check])

    email = forms.CharField(widget = forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email.")])
    
    age = forms.IntegerField(validators=[validators.MinValueValidator(10, message="age must be minimum 10"), validators.MaxValueValidator(35, message="age must be maximum 35")])
    
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message="file extension ended with pdf")])
    
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self): # multiple field validate korar jonno
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conf_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        
        if val_pass != val_conf_pass:
            raise forms.ValidationError("Password doesn't matched!")
        
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be atleast 15 characters.")