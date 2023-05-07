from django import forms
from .models import Alternatif, Kriteria, SubKriteria, Penilaian

class AlternatifForm(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = '__all__'
        widgets = {
            'simbol': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama_alternatif': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control'}),
        }

class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = '__all__'
        widgets = {
            'simbol': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_kriteria': forms.TextInput(attrs={'class': 'form-control'}),
            'bobot': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SubKriteriaForm(forms.ModelForm):
    class Meta:
        model = SubKriteria
        fields = '__all__'
        widgets = {
            'kriteria': forms.Select(attrs={'class': 'form-control'}),
            'nama_sub_kriteria': forms.TextInput(attrs={'class': 'form-control'}),
            'nilai_sub_kriteria': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PenilaianForm(forms.ModelForm):
    class Meta:
        model = Penilaian
        fields = '__all__'
        widgets = {
            'simbol': forms.Select(attrs={'class': 'form-control'}),
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'kondisi_rumah': forms.Select(attrs={'class': 'form-control'}),
            'penghasilan': forms.Select(attrs={'class': 'form-control'}),
            'bumil_dan_bunsui': forms.Select(attrs={'class': 'form-control'}),
            'lansia': forms.Select(attrs={'class': 'form-control'}),
            'anak_sekolah': forms.Select(attrs={'class': 'form-control'}),
        }
