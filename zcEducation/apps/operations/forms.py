from django import forms
import re

class UserCommentForm(forms.Form):
    course = forms.IntegerField(required=True)
    content = forms.CharField(required=True,min_length=1,max_length=300)


