from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model= Location
        fields= ["name", "imagefile", "country", "location", "locationDescription"]
