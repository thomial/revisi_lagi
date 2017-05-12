from django import forms
from models import table_post_description

class Document(forms.ModelForm):
    class Meta :
        model = table_post_description
        fields = ('judul', 'deskripsi', 'document', )
