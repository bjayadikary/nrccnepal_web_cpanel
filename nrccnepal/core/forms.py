from django import forms
from .models import Contact, NewsletterSubscription # , NewsletterMailMessage

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'address', 'phone', 'content']
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': "Your Name",'data-sb-validations':"required", 'data-rule':"minlen:4", 'data-msg':'Please enter at least 4 chars'}),
		'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': "Your Email",'data-sb-validations':"required", 'data-rule':"email", 'data-msg':"Please enter a valid email"}),
		'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address', 'placeholder': "Your Address", 'data-sb-validations':"required", }),
		'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': "Your Phone Number", 'data-sb-validations':"required"}),
		'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': "Message", 'cols': 30, 'rows': 10, 'data-sb-validations':"response"})
		}


class NewsletterSubscriptionForm(forms.ModelForm):
	class Meta:
		model = NewsletterSubscription
		fields = ['email', ]

		# widgets is not required for basic functionality. If want to use placeholder then use. 
		# widgets = {
		# 	'email': forms.EmailInput(attrs={
		# 		'class': 'form-control',
		# 		'name':"email",
		# 		'placeholder': "example@gmail.com",
		# 		'data-sb-validations': "required",
		# 		'data-msg': "Please enter a valid email",
		# 	})
		# }

# class NewsletterMailMessageForm(forms.ModelForm):
# 	class Meta:
# 		model = NewsletterMailMessage
# 		fields = '__all__'