from django import forms


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=False)
    pub_date = forms.DateTimeField(label='Date Published', required=False)
    author = forms.CharField(label='Author', max_length=100, required=False)
