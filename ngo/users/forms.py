

        }

class UpdateCustomUserForm(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    Password = forms.CharField()

class LoginForm(AuthenticationForm):
    email = forms.CharField(label='Email ')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'location',
            'birth_date',
            'cma_num',
            'phone',
            'addressLineOne',
            'addressLineTwo',
            'city',
            'state',
            'zip_code',
            'country',
            'urbanization',
        ]

        widgets = {
            'bio' : forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
            'cma_num': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'addressLineOne': forms.TextInput(attrs={'class': 'form-control'}),
            'addressLineTwo': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'urbanization': forms.TextInput(attrs={'class': 'form-control'}),


        }


class UpdateProfile(forms.ModelForm):
    bio = forms.CharField()
    location = forms.CharField()
    birth_date = forms.DateField()
    cma_num = forms.IntegerField()
    phone = forms.CharField()
    addressLineOne = forms.CharField()
    addressLineTwo = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.CharField()
    country = forms.CharField()
    urbanization = forms.CharField()
