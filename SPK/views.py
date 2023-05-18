from django.shortcuts import render, redirect, get_object_or_404
from .models import Alternatif, Kriteria, SubKriteria, Penilaian,Rengking
from .forms import AlternatifForm, KriteriaForm, SubKriteriaForm, PenilaianForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Sum, Max, Min, F, Q
from django.db.models.functions import Coalesce,Cast,Round
from django.core.exceptions import ObjectDoesNotExist
from datetime import date

# fungsi untuk menampilkan semua data alternatif
def alternatif_list(request):
    # ambil semua data alternatif dan urutkan berdasarkan id yg terbesar
    alternatif = Alternatif.objects.all().order_by('-id')
    # searching
    cari = request.GET.get('cari')
    if cari:
        page=Alternatif.objects.filter(Q(simbol__icontains=cari) |Q(nama_alternatif__icontains=cari))
    else:        
        page = Alternatif.objects.all()
    # paginations
    halaman = Paginator(page,5)
    page_list = request.GET.get('page')
    page = halaman.get_page(page_list)  
    # lempar ke tamplates
    context = {
        'datas': alternatif,
        'page_obj': page,
    }
    return render(request, 'alternatif.html', context)

# fungsi untuk menambah data alternatif baru
def alternatif_create(request):
    # cek method
    if request.method == 'POST':
        # instance form dan validasi isi datanya
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Tambahkan!")
            return redirect('data:alternatif')
    else:
        form = AlternatifForm()
    return render(request, 'alternatif_form.html', {'form': form})

# fungsi untuk mengubah data alternatif yang sudah ada
def alternatif_update(request, id):
    alternatif = get_object_or_404(Alternatif, id=id)
    if request.method == 'POST':
        form = AlternatifForm(request.POST, instance=alternatif)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Update!")
            return redirect('data:alternatif')
    else:
        form = AlternatifForm(instance=alternatif)
    return render(request, 'alternatif_form.html', {'form': form})

# fungsi untuk menghapus data alternatif yang sudah ada
def alternatif_delete(request, id):
    alternatif = get_object_or_404(Alternatif, id=id)
    alternatif.delete()
    messages.success(request, " Data Berhasil di Delete!")
    return redirect('data:alternatif')

def kriteria_list(request):
    kriteria = Kriteria.objects.all()
    cari = request.GET.get('cari')
    if cari:
        page=Kriteria.objects.filter(Q(simbol__icontains=cari) |Q(nama_kriteria__icontains=cari))
    else:        
        page = Kriteria.objects.all()

    halaman = Paginator(page,5)
    page_list = request.GET.get('page')
    page = halaman.get_page(page_list)  
    context ={
        'datas': kriteria,
        'page_obj':page,
    }
    return render(request, 'kriteria.html', context)

def kriteria_create(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Tambahkan!")
            return redirect('data:kriteria')
    else:
        form = KriteriaForm()
    return render(request, 'kriteria_form.html', {'form': form})

def kriteria_update(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Update!")
            return redirect('data:kriteria')
    else:
        form = KriteriaForm(instance=kriteria)
    return render(request, 'kriteria_form.html', {'form': form})

def kriteria_delete(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    kriteria.delete()
    messages.success(request, " Data Berhasil di Delete!")
    return redirect('data:kriteria')

def subkriteria_list(request):
    subkriteria = SubKriteria.objects.all()
    cari = request.GET.get('cari')
    if cari:
        page=SubKriteria.objects.filter(Q(kriteria__nama_kriteria__icontains=cari) | Q(nama_sub_kriteria__icontains=cari))
    else:        
        page = SubKriteria.objects.all()

    halaman = Paginator(page,10)
    page_list = request.GET.get('page')
    page = halaman.get_page(page_list)  
    context ={
        'datas': subkriteria,
        'page_obj':page,
    }
    return render(request, 'subkriteria.html', context)

def subkriteria_create(request):
    form = SubKriteriaForm()
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Tambah!")
            return redirect('data:sub_kriteria')
    return render(request, 'subkriteria_form.html', {'form': form})

def subkriteria_update(request, id):
    subkriteria = SubKriteria.objects.get(id=id)
    form = SubKriteriaForm(instance=subkriteria)
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST, instance=subkriteria)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Update!")
            return redirect('data:sub_kriteria')
    return render(request, 'subkriteria_form.html', {'form': form})

def subkriteria_delete(request, id):
    subkriteria = get_object_or_404(SubKriteria, id=id)
    subkriteria.delete()
    messages.success(request, " Data Berhasil di Delete!")
    return redirect('data:sub_kriteria')

def create_penilaian(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Tambah!")
            return redirect('data:penilaian')
    else:
        form = PenilaianForm()
    
    context = {
        'form': form
    }

    return render(request, 'penilaian_form.html', context)

def penilaian_list(request):
    penilaian = Penilaian.objects.all()

    # Mengambil nilai maksimum dari setiap kolom
    max_values = Penilaian.objects.aggregate(
        max_kondisi_rumah=Max('kondisi_rumah__nilai_sub_kriteria'),
        max_penghasilan=Max('penghasilan__nilai_sub_kriteria'),
        max_bumil_dan_bunsui=Max('bumil_dan_bunsui__nilai_sub_kriteria'),
        max_lansia=Max('lansia__nilai_sub_kriteria'),
        max_anak_sekolah=Max('anak_sekolah__nilai_sub_kriteria')
    )

    # Mengambil nilai minimum dari setiap kolom
    min_values = Penilaian.objects.aggregate(
        min_kondisi_rumah=Min('kondisi_rumah__nilai_sub_kriteria'),
        min_penghasilan=Min('penghasilan__nilai_sub_kriteria'),
        min_bumil_dan_bunsui=Min('bumil_dan_bunsui__nilai_sub_kriteria'),
        min_lansia=Min('lansia__nilai_sub_kriteria'),
        min_anak_sekolah=Min('anak_sekolah__nilai_sub_kriteria')
    )

    # NILAI MAX DAN MIN
    max_kondisi_rumah = max_values['max_kondisi_rumah']
    min_kondisi_rumah = min_values['min_kondisi_rumah']
    # pengahasilan
    max_penghasilan = max_values['max_penghasilan']
    min_penghasilan = min_values['min_penghasilan']
    # bumil dan bunsui
    max_bumil_dan_bunsui = max_values['max_bumil_dan_bunsui']
    min_bumil_dan_bunsui = min_values['min_bumil_dan_bunsui']
    # lansia
    max_lansia = max_values['max_lansia']
    min_lansia = min_values['min_lansia']
    # sekolah
    max_anak_sekolah = max_values['max_anak_sekolah']
    min_anak_sekolah = min_values['min_anak_sekolah']

    # Mengambil nilai bobot dari model Kriteria
    kriteria = Kriteria.objects.all()
    bobot_kondisi_rumah = kriteria.get(nama_kriteria='Kondisi Rumah').bobot
    bobot_penghasilan = kriteria.get(nama_kriteria='Penghasilan').bobot
    bobot_bumil_dan_bunsui = kriteria.get(nama_kriteria='Bumil dan Bunsui').bobot
    bobot_lansia = kriteria.get(nama_kriteria='Lansia').bobot
    bobot_anak_sekolah = kriteria.get(nama_kriteria='Anak Sekolah').bobot

    # NORMALISASI
    data_list = []
    for data in penilaian:
        max_kondisi_rumah = max_values['max_kondisi_rumah']
        min_penghasilan = min_values['min_penghasilan']
        max_bumil_dan_bunsui = max_values['max_bumil_dan_bunsui']
        max_lansia = max_values['max_lansia']
        max_anak_sekolah = max_values['max_anak_sekolah']

        kondisi_rumah = data.kondisi_rumah.nilai_sub_kriteria / max_kondisi_rumah
        penghasilan = min_penghasilan / data.penghasilan.nilai_sub_kriteria
        bumil_dan_bunsui = data.bumil_dan_bunsui.nilai_sub_kriteria / max_bumil_dan_bunsui
        lansia = data.lansia.nilai_sub_kriteria / max_lansia
        anak_sekolah = data.anak_sekolah.nilai_sub_kriteria / max_anak_sekolah
        
        kondisi_rumah = round(kondisi_rumah, 2)
        penghasilan = round(penghasilan, 2)
        bumil_dan_bunsui = round(bumil_dan_bunsui, 2)
        lansia = round(lansia, 2)
        anak_sekolah = round(anak_sekolah, 2)

        data_item = {
            'alternatif': data.nama,
            'kondisi_rumah': kondisi_rumah,
            'penghasilan': penghasilan,
            'bumil_dan_bunsui': bumil_dan_bunsui,
            'lansia': lansia,
            'anak_sekolah': anak_sekolah
        }

        data_list.append(data_item)

    # MATRIK
    matriks = []
    for data in penilaian:
        max_kondisi_rumah = max_values['max_kondisi_rumah']
        min_penghasilan = min_values['min_penghasilan']
        max_bumil_dan_bunsui = max_values['max_bumil_dan_bunsui']
        max_lansia = max_values['max_lansia']
        max_anak_sekolah = max_values['max_anak_sekolah']

        kondisi_rumah = data.kondisi_rumah.nilai_sub_kriteria / max_kondisi_rumah
        penghasilan = min_penghasilan / data.penghasilan.nilai_sub_kriteria
        bumil_dan_bunsui = data.bumil_dan_bunsui.nilai_sub_kriteria / max_bumil_dan_bunsui
        lansia = data.lansia.nilai_sub_kriteria / max_lansia
        anak_sekolah = data.anak_sekolah.nilai_sub_kriteria / max_anak_sekolah

        # Mengalikan dengan bobot
        kondisi_rumah *= bobot_kondisi_rumah
        penghasilan *= bobot_penghasilan
        bumil_dan_bunsui *= bobot_bumil_dan_bunsui
        lansia *= bobot_lansia
        anak_sekolah *= bobot_anak_sekolah

        # Menjumlahkan hasil perkalian pada setiap baris
        total = kondisi_rumah + penghasilan + bumil_dan_bunsui + lansia + anak_sekolah

        # format agar 2 angka dibelakang koma
        kondisi_rumah = round(kondisi_rumah, 2)
        penghasilan = round(penghasilan, 2)
        bumil_dan_bunsui = round(bumil_dan_bunsui, 2)
        lansia = round(lansia, 2)
        anak_sekolah = round(anak_sekolah, 2)
        total = round(total, 2)

        # Mengambil nilai ket
        ket = ''
        if total >= 0.6:
            ket = 'Layak'
        else:
            ket = 'Tidak Layak'
        # tampung semuanya
        data_item = {
            'alternatif': data.nama,
            'kondisi_rumah': kondisi_rumah,
            'penghasilan': penghasilan,
            'bumil_dan_bunsui': bumil_dan_bunsui,
            'lansia': lansia,
            'anak_sekolah': anak_sekolah,
            'total': total,
            'ket': ket  # Tambahkan nilai ket
        }
        # tambah ke list matriks
        matriks.append(data_item)

        # Cek apakah data dengan alternatif yang sama sudah ada dalam Rengking
        rengking, created = Rengking.objects.get_or_create(alternatif=data.nama)

        # Assign values ke fields
        rengking.rumah = str(kondisi_rumah)
        rengking.penghasilan = str(penghasilan)
        rengking.bumil_bunsui = str(bumil_dan_bunsui)
        rengking.lansia = str(lansia)
        rengking.anak_sekolah = str(anak_sekolah)

        # Cek jika total calculated
        if total:
            rengking.total_nilai = total
        else:
            # Assign  default value atau handle ketika total tidak di calculated
            rengking.total_nilai = 0.0

        rengking.ket = ket
        rengking.save()

    context = {
        'datas': penilaian,        
        'normalisasi': data_list,
        'matriks': matriks,
        # max dan min
        'max_kondisi_rumah': max_kondisi_rumah,
        'min_kondisi_rumah': min_kondisi_rumah,
        'max_penghasilan': max_penghasilan,
        'min_penghasilan': min_penghasilan,
        'max_bumil_dan_bunsui': max_bumil_dan_bunsui,
        'min_bumil_dan_bunsui': min_bumil_dan_bunsui,
        'max_lansia': max_lansia,
        'min_lansia': min_lansia,
        'max_anak_sekolah': max_anak_sekolah,
        'min_anak_sekolah': min_anak_sekolah,
        # bobot
        'bobot_kondisi_rumah':bobot_kondisi_rumah,
        'bobot_penghasilan':bobot_penghasilan,
        'bobot_bumil_dan_bunsui':bobot_bumil_dan_bunsui,
        'bobot_lansia':bobot_lansia,
        'bobot_anak_sekolah':bobot_anak_sekolah ,
        }

    return render(request, 'penilaian.html', context)

def update_penilaian(request, id):
    penilaian = Penilaian.objects.get(id=id)

    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            messages.success(request, " Data Berhasil di Update!")
            return redirect('data:penilaian')
    else:
        form = PenilaianForm(instance=penilaian)
    
    context = {
        'form': form
    }

    return render(request, 'penilaian_form.html', context)

def delete_penilaian(request,id):
    penilaian = get_object_or_404(Penilaian, id=id)
    penilaian.delete()
    messages.success(request, " Data Berhasil di Delete!")
    return redirect('data:penilaian')

    context = {
        'penilaian': penilaian
    }

    return render(request, 'penilaian.html', context)

def rengking(request):
    rengking_data = Rengking.objects.all().order_by('-total_nilai')

    context = {
        'rengking_data': rengking_data,
    }

    return render(request, 'rengking.html', context)

def print_laporan(request):
    # mendapatkan tanggal saat ini
    tanggal = date.today().strftime("%d %B %Y")

    context = {
        'rengking_data': Rengking.objects.all().order_by('-total_nilai'),
        'tanggal': tanggal,
    }

    return render(request, 'laporan.html', context)

