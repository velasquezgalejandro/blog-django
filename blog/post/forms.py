from django import forms
from .models import Post
from datetime import datetime

class PostModelForm(forms.ModelForm):
    fecha_publicacion = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy'}),
    )

    class Meta:
        model = Post
        fields = ['titulo', 'contenido','fecha_publicacion', 'categoria', 'autor']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            raise forms.ValidationError('El título es obligatorio.')
        if len(titulo) < 4:
            raise forms.ValidationError('El título debe tener al menos 4 caracteres.')
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido')
        if not contenido:
            raise forms.ValidationError('El contenido es obligatorio.')
        return contenido

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('La categoria es obligatorio.')
        return categoria

    def clean_autor(self):
        autor = self.cleaned_data.get('autor')
        if not autor:
            raise forms.ValidationError('El autor es obligatorio.')
        return autor

    def clean_fecha_publicacion(self):
        fecha_publicacion_str = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion_str:
            try:
                fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%d/%m/%Y').date()
                return fecha_publicacion
            except ValueError:
                raise forms.ValidationError('La fecha debe estar en el formato dd/mm/yyyy.')
        return fecha_publicacion_str
