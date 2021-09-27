from django import forms#, formset_factory

class LoginUserForm(forms.Form):
    door_id =  forms.IntegerField()
