from django import forms
from database.models import Sport


class ImageForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ["sport_id", "image"]
