from django import forms

from newsletter.models import SignUp

class ContactForm(forms.ModelForm):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.Textarea()

	class Meta:
		model = SignUp
		fields = ['full_name', 'email']


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
