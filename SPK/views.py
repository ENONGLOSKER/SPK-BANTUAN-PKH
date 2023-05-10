from django.shortcuts import render, redirect, get_object_or_404
from .models import Alternatif, Kriteria, SubKriteria, Penilaian
from .forms import AlternatifForm, KriteriaForm, SubKriteriaForm, PenilaianForm
from django.core.paginator import Paginator
from django.db.models import Q

# fungsi untuk menampilkan semua data alternatif
def alternatif_list(request):
    alternatif = Alternatif.objects.all().order_by('-id')

    # paginations & searching
    cari = request.GET.get('cari')
    if cari:
        page=Alternatif.objects.filter(Q(simbol__icontains=cari) |Q(nama_alternatif__icontains=cari))
    else:        
        page = Alternatif.objects.all()

    halaman = Paginator(page,3)
    page_list = request.GET.get('page')
    page = halaman.get_page(page_list)  

    context = {
        'datas': alternatif,
        'page_obj': page,
    }

    return render(request, 'alternatif.html', context)

# fungsi untuk menambah data alternatif baru
def alternatif_create(request):
    if request.method == 'POST':
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('data:alternatif')
    else:
        form = AlternatifForm(instance=alternatif)
    return render(request, 'alternatif_form.html', {'form': form})

# fungsi untuk menghapus data alternatif yang sudah ada
def alternatif_delete(request, id):
    alternatif = get_object_or_404(Alternatif, id=id)
    alternatif.delete()
    return redirect('data:alternatif')

# fungsi untuk menampilkan semua data kriteria
def kriteria_list(request):
    kriteria = Kriteria.objects.all()
    cari = request.GET.get('cari')
    if cari:
        page=Kriteria.objects.filter(Q(simbol__icontains=cari) |Q(nama_kriteria__icontains=cari))
    else:        
        page = Kriteria.objects.all()

    halaman = Paginator(page,3)
    page_list = request.GET.get('page')
    page = halaman.get_page(page_list)  
    context ={
        'datas': kriteria,
        'page_obj':page,
    }
    return render(request, 'kriteria.html', context)

# fungsi untuk menambah data kriteria baru
def kriteria_create(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data:kriteria')
    else:
        form = KriteriaForm()
    return render(request, 'kriteria_form.html', {'form': form})

# fungsi untuk mengubah data kriteria yang sudah ada
def kriteria_update(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            return redirect('data:kriteria')
    else:
        form = KriteriaForm(instance=kriteria)
    return render(request, 'kriteria_form.html', {'form': form})

# fungsi untuk menghapus data kriteria yang sudah ada
def kriteria_delete(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    kriteria.delete()
    return redirect('data:kriteria')

def subkriteria_list(request):
    subkriteria = SubKriteria.objects.all()
    cari = request.GET.get('cari')
    if cari:
        page=SubKriteria.objects.filter(Q(kriteria__nama_kriteria__icontains=cari) | Q(nama_sub_kriteria__icontains=cari))
    else:        
        page = SubKriteria.objects.all()

    halaman = Paginator(page,5)
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
            return redirect('data:sub_kriteria')
    return render(request, 'subkriteria_form.html', {'form': form})

def subkriteria_update(request, id):
    subkriteria = SubKriteria.objects.get(id=id)
    form = SubKriteriaForm(instance=subkriteria)
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST, instance=subkriteria)
        if form.is_valid():
            form.save()
            return redirect('data:sub_kriteria')
    return render(request, 'subkriteria_form.html', {'form': form})

def subkriteria_delete(request, id):
    subkriteria = get_object_or_404(SubKriteria, id=id)
    subkriteria.delete()
    return redirect('data:sub_kriteria')

def create_penilaian(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data:penilaian')
    else:
        form = PenilaianForm()
    
    context = {
        'form': form
    }

    return render(request, 'penilaian_form.html', context)

def penilaian_list(request):
    penilaian = Penilaian.objects.all()

    context = {
        'datas': penilaian
    }

    return render(request, 'penilaian.html', context)

def update_penilaian(request, id):
    penilaian = Penilaian.objects.get(id=id)

    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('data:penilaian')
    else:
        form = PenilaianForm(instance=penilaian)
    
    context = {
        'form': form
    }

    return render(request, 'penilaian_form.html', context)

def delete_penilaian(request,id):
    penilaian = Penilaian.objects.get(id=id)

    if request.method == 'POST':
        penilaian.delete()
        return redirect('data:penilaian')

    context = {
        'penilaian': penilaian
    }

    return render(request, 'penilaian.html', context)

def rengking(request):

    context = {
    
    }

    return render(request, 'rengking.html', context)
