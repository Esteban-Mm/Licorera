from django import forms

class FormVenta(forms.Form):

    names = forms.CharField(
        label="Nombres",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite su nombre',
                'class': 'nombre_form_article'
            }
        )
    )

    direction = forms.CharField(
        label="Direción",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Direccion de entrega',
                'class': 'direccion_form_article'
            }
        )
    )

    email = forms.EmailField(
        label="Correo Electronico",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite su correo electronico',
                'class': 'correo_form_article'
            }
        )
    )

    mobil = forms.CharField(
        label="Telefono",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Numero de contacto',
                'class': 'celular_form_article'
            }
        )
    )

    unit = forms.IntegerField(
        label="Unidad a comprar",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Cantidades',
                'class': 'unidades_form_article'
            }
        )
    )

