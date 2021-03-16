from django import forms
DONATION_QUANTITY_CHOICES = [(i,str(i)) for i  in range(1,21)]
class CartAddDonationForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=DONATION_QUANTITY_CHOICES,coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

