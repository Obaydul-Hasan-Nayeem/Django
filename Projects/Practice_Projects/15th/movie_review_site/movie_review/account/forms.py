from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kargs): # * -> positional argument, ** -> key value argument
        super(UserCreationForm, self).__init__(*args, **kargs) # super -> usercreationform er shob field gulo ekhane peye jabo
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None # help text remove kore dibe
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'}) # form ta k bootstrap diye r aktu shundor korar jonno ei line. widget bolte bojhay html er tag gulo.

class LogInForm(AuthenticationForm):
    def __init__(self, *args, **kargs):
        super(AuthenticationForm, self).__init__(*args, **kargs)
        
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None # help text remove kore dibe
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'}) # form ta k bootstrap diye r aktu shundor korar jonno ei line. widget bolte bojhay html er tag gulo.
