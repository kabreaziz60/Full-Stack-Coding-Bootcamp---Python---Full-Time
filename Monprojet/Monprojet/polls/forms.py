from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField()  
      comment = forms.CharField()

class ContactForm(forms.Form):
      name = forms.CharField(required=False, min_length=3)
      email = forms.EmailField(
          label="Your email", 
          help_text='Must contain al least 8 characters', 
          min_length=8,
          error_messages={'required': 'Please enter a valid email address'})  
      comment = forms.CharField(widget = forms.Textarea)




def validate_name(name):
    # check if there are numbers in the name
    if (name.isalpha() == False):
        print("Invalid name")  
        raise forms.ValidationError(f'The name {name} is invalid')


class ContactForm(forms.Form):
    name = forms.CharField(
        required=False, 
        min_length=3,
        validators=[validate_name], # Call the validate_name function here
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write your name here'
            })
        )
    email = forms.EmailField(
          label="Your email", 
          help_text='Must contain at least 8 characters and a @',
          widget = forms.EmailInput(
            attrs={
                'placeholder': 'Write your email here'
            })
          )  
    comment = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write your comment here'
                })
            )
      