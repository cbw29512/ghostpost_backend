from django import forms
from api.models import Post


class AddPostForm(forms.Form):
    post_title = forms.CharField(max_length=30)
    body = forms.CharField(max_length=200)

    boast_or_roast = forms.BooleanField(help_text="boast if clicked", required=False)
