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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kondisi_rumah'].queryset = SubKriteria.objects.filter(kriteria__nama_kriteria='Kondisi Rumah')
        self.fields['penghasilan'].queryset = SubKriteria.objects.filter(kriteria__nama_kriteria='Penghasilan')
        self.fields['bumil_dan_bunsui'].queryset = SubKriteria.objects.filter(kriteria__nama_kriteria='Bumil dan Bunsui')
        self.fields['lansia'].queryset = SubKriteria.objects.filter(kriteria__nama_kriteria='Lansia')
        self.fields['anak_sekolah'].queryset = SubKriteria.objects.filter(kriteria__nama_kriteria='Anak Sekolah')

        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Penilaian
        fields = '__all__'