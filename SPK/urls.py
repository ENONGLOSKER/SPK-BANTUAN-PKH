from django.urls import path
from . import views

app_name= 'SPK'

urlpatterns = [
    # alternatif
    path('alternatif/', views.alternatif_list, name='alternatif'),
    path('inalternatif/', views.alternatif_create, name='inalternatif'),
    path('upalternatif/<int:id>', views.alternatif_update, name='upalternatif'),
    path('delalternatif/<int:id>', views.alternatif_delete, name='delalternatif'),
    # kriteria
    path('kriteria/', views.kriteria_list, name='kriteria'),
    path('inkriteria/', views.kriteria_create, name='inkriteria'),
    path('upkriteria/<int:id>', views.kriteria_update, name='upkriteria'),
    path('delkriteria/<int:id>', views.kriteria_delete, name='delkriteria'),
    # subkriteria
    path('sub_kriteria/', views.subkriteria_list, name='sub_kriteria'),
    path('insub_kriteria/', views.subkriteria_create, name='insubkriteria'),
    path('upsub_kriteria/<int:id>', views.subkriteria_update, name='upsubkriteria'),
    path('delsub_kriteria/<int:id>', views.subkriteria_delete, name='delsubkriteria'),
    # penilaian
    path('penilaian/', views.penilaian_list, name='penilaian'),
    path('inperengkingan/', views.create_penilaian, name='inperengkingan'),
    path('uppenilaian/<int:id>', views.update_penilaian, name='uppenilaian'),
    path('delperengkingan/<int:id>', views.delete_penilaian, name='delperengkingan'),
    # rengking 
    path('rengking/', views.rengking, name='perengkingan'),
]
