from django.contrib.auth import user_logged_in, get_user_model
from django.dispatch import receiver
from django.http import Http404
from django.shortcuts import render

from jobs.models import Job, Location, Employer
from matches.models import PositionMatch, Match

User = get_user_model()


@receiver(user_logged_in)
def get_user_matches_reciever(sender, request, user, *args, **kwargs):
	for u in User.objects.exclude(username=user.username).order_by("-id")[:200]:
		Match.objects.get_or_create_match(user_a=u, user_b=user)


def position_match_view(request, slug):
	try:
		instance = Job.objects.get(slug=slug)
	except Job.MultipleObjectsReturned:
		queryset = Job.objects.filter(slug=slug).order_by("-id")
		instance = queryset[0]
	except Job.DoesNotExist:
		raise Http404

	template = "matches/position_match_view.html"
	context = {
		"instance": instance,
	}
	return render(request, template, context)


def location_match_view(request, slug):
	try:
		instance = Location.objects.get(slug=slug)
	except Location.MultipleObjectsReturned:
		queryset = Location.objects.filter(slug=slug).order_by("-id")
		instance = queryset[0]
	except Location.DoesNotExist:
		raise Http404

	matches = PositionMatch.objects.filter(job__text__iexact=instance.text)
	template = "matches/location_match_view.html"
	context = {
		"instance": instance,
		"matches": matches,
	}
	return render(request, template, context)


def employer_match_view(request, slug):
	try:
		instance = Employer.objects.get(slug=slug)
	except Employer.MultipleObjectsReturned:
		queryset = Employer.objects.filter(slug=slug).order_by("-id")
		instance = queryset[0]
	except Employer.DoesNotExist:
		raise Http404

	template = "matches/employer_match_view.html"
	context = {
		"instance": instance,
	}
	return render(request, template, context)
