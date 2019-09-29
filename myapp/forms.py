from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=2047, widget=forms.Textarea(attrs={"rows":6}))

    name.widget.attrs.update({'class':'form-control','placeholder':'Name'})
    email.widget.attrs.update({'class':'form-control','placeholder':'Email'})
    message.widget.attrs.update({'class':'form-control','placeholder':'Message'})
