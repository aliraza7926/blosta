from django import forms
from .models import Review
class ReviewForm(forms.Form):
    class Meta:
        model = Review
        fields=('author','review',)
    tes=forms.CharField(label='your comment',max_length=200)