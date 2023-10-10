from django import forms

class NameForm(forms.Form):
    sportsmanName = forms.CharField(label_suffix=False, label='', max_length=100,
                                    widget=forms.TextInput(attrs={'placeholder': 'Фамилия Имя Спортсмена'}))