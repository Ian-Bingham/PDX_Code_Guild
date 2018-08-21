from django import forms


class MakePostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=True)
    body = forms.CharField(label='Body', widget=forms.Textarea(), required=True)


class MakeCommentForm(forms.Form):
    body = forms.CharField(label='Comment', widget=forms.Textarea(), required=False)
