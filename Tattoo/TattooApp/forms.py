from django import forms

class form_cliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    ciudad = forms.CharField(max_length=40)
    email = forms.EmailField()

class form_artista(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    ciudad = forms.CharField(max_length=40)
    estilo = forms.CharField(max_length=40)

class form_tattoos(forms.Form):
    id = forms.IntegerField()
    nombre_cliente = forms.CharField(max_length=40)
    apellido_cliente = forms.CharField(max_length=40)
    nombre_artista = forms.CharField(max_length=40)
    fecha_tat = forms.DateField()
    estilo_tat = forms.CharField(max_length=200)
    lugar_tat = forms.CharField(max_length=200)

