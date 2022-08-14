from django import forms
from wagtail.admin.forms import WagtailAdminPageForm

from wagtail_qrcode.wagtail_hooks import send_qr_code_email


class QrCodeEmailForm(WagtailAdminPageForm):
    email_address = forms.EmailField(
        label="Recipient Email",
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "Email address"}),
        help_text="The email address will not be saved to the database and is used only once to send the EPS file.",
    )
    email_subject = forms.CharField(
        label="Subject",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Subject if email is sent"}),
    )
    email_body = forms.CharField(
        label="Body",
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Body of the email if sent"}),
    )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["email_address"]:
            if not cleaned_data["email_subject"]:
                self.add_error(
                    "email_subject",
                    "The email subject is required if an email address is provided.",
                )
            if not cleaned_data["email_body"]:
                self.add_error(
                    "email_body",
                    "The email body is required if an email address is provided.",
                )

        return cleaned_data

    def save(self, commit=True):
        page = super().save(commit=False)

        # send email if email_address is available
        if self.cleaned_data["email_address"]:
            email_address = self.cleaned_data["email_address"]
            email_subject = self.cleaned_data["email_subject"]
            email_body = self.cleaned_data["email_body"]
            send_qr_code_email(page, email_address, email_subject, email_body)

            print("Sending email to {}".format(self.cleaned_data["email_address"]))

        if commit:
            page.save()
        return page
