from django import forms
from .models import AffiliatePartner, Contact, EnquireModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'phone_number', 'message']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name*', 'required': 'required'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email*', 'required': 'required'})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject*', 'required': 'required'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone*', 'required': 'required'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message*', 'required': 'required'})
    )


from .models import AffiliatePartner

class AffiliatePartnerForm(forms.ModelForm):
    class Meta:
        model = AffiliatePartner
        fields = ['firstname', 'last_name', 'email', 'phone_number', 
                  'Referrer_name', 'Referrer_email', 'Referrer_phone_number', 
                  'course_name', 'message', 'country', 'city', 'zipcode']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your phone number'
        self.fields['Referrer_name'].widget.attrs['placeholder'] = 'Enter referrer\'s name'
        self.fields['Referrer_email'].widget.attrs['placeholder'] = 'Enter referrer\'s email'
        self.fields['Referrer_phone_number'].widget.attrs['placeholder'] = 'Enter referrer\'s phone number'
        self.fields['course_name'].widget.attrs['placeholder'] = 'Enter the course name'
        self.fields['message'].widget.attrs['placeholder'] = 'Optional: Leave a message'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter your country'
        self.fields['city'].widget.attrs['placeholder'] = 'Enter your city'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Enter your zipcode'

class EnquireModelForm(forms.ModelForm):
    class Meta:
        model = EnquireModel
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'Select_Course_Certification_Exam',
                  'preferred_date_time', 'any_previous_experience_on_IT', 'Any_special_request_accommodations', 'comments_question']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'Select_Course_Certification_Exam': forms.Select(attrs={'placeholder': 'Select course', 'class': 'form-select'}),
            'preferred_date_time': forms.DateTimeInput(attrs={'placeholder': 'Select preferred date and time', 'class': 'form-control'}),
            'any_previous_experience_on_IT': forms.Textarea(attrs={'placeholder': 'Any previous experience on IT', 'class': 'form-control'}),
            'Any_special_request_accommodations': forms.Textarea(attrs={'placeholder': 'Any special request or accommodations', 'class': 'form-control'}),
            'comments_question': forms.Textarea(attrs={'placeholder': 'Any comments or questions', 'class': 'form-control'}),
        }