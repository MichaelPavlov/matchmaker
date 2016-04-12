from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from newsletter.forms import ContactForm


def newsletter_contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		subject = "Django mail test"
		from_email = settings.EMAIL_HOST_USER
		to_email = ["buddah@inbox.ru", "rastafarri@gmail.com", "supersonike@yahoo.com"]
		contact_message = "This is the body of email. Hi from django application"
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

	context = {
		"form": form,
	}
	return render(request, "forms.html", context)
