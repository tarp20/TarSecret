from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name','last_name','username','email')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean_subject(self):
        data = self.cleaned_data['subject']
        if "thanks" or "thank you" not in data.lower():
            raise forms.ValidationError("You should definitely thank us!")
        return data

class PostForm(forms.Form):
    group = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea,required=True)

