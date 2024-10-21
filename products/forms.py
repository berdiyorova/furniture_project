from django import forms


class ColorPickerForm(forms.ModelForm):
    code = forms.CharField(
        label="Choose a color:",
        widget=forms.TextInput(attrs={'type': 'color'})
    )
