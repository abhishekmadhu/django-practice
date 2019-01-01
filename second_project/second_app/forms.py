from django import forms
from second_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():       # the () is for pytho three, doesn't really matter
        model = User    # has to be named model every time
        fields = '__all__'
