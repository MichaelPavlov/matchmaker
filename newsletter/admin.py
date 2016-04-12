from django.contrib import admin

from newsletter.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__uniclode__", "timestamp", "updated"]

	class Meta:
		model = SignUp

admin.site.register(SignUp, SignUpAdmin)
