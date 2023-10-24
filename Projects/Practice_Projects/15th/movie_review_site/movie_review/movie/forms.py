from django.forms import ModelForm, Textarea

from movie.models import Review

class ReviewForm(ModelForm):
    def __init__(self, *args, **kargs):
        super(ReviewForm, self).__init__(*args, **kargs)
        
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})
        
    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        widgets = {
            'text': Textarea(attrs={'row': 3})
        }
        labels = {
            'watchAgain': ('Watch Again')
        }
    