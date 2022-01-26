from allauth.account.forms import AddEmailForm
from allauth.account.models import EmailAddress


# Custom Form to block sending confirmation e-mail
class CustomAddEmailForm(AddEmailForm):
    def save(self, request):
        return EmailAddress.objects.add_email(
            request, self.user, self.cleaned_data["email"], confirm=False
        )


