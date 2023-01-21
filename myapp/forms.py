from django import forms
from PIL import Image

class ProfilePictureForm(forms.Form):
    picture = forms.ImageField()

    def clean_picture(self):
        picture = self.cleaned_data.get("picture")
        if not picture:
            raise forms.ValidationError("No image was selected")
        try:
            image = Image.open(picture)
            width, height = image.size
            if width > 180 or height > 180:
                raise forms.ValidationError("The image size should be 180x180")
        except:
            raise forms.ValidationError("Invalid image format")
        return picture
