from django import forms

from .models import TinyMCEBlock


class TinyMCEBlockForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "tinymce_textfield"}))

    class Meta:
        model = TinyMCEBlock
        fields = "__all__"
