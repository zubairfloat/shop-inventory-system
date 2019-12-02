from django.shortcuts import render , redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_laptops(request):
    items = Laptop.objects.all()
    context= {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'index.html', context)

def display_USB(request):
    items = USB.objects.all()
    context= {
        'items': items,
        'header': 'USB',
    }
    return render(request, 'index.html', context)

def display_mobiles(request):
    items = Mobile.objects.all()
    context= {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'index.html', context)

def display_memorycard(request):
    items = MemmoryCard.objects.all()
    context= {
        'items': items,
        'header': 'MemoryCard',
    }
    return render(request, 'index.html', context)

def display_handfree(request):
    items = Handfree.objects.all()
    context= {
        'items': items,
        'header': 'Handfree',
    }
    return render(request, 'index.html', context)

def display_charger(request):
    items = Charger.objects.all()
    context= {
        'items': items,
        'header': 'Charger',
    }
    return render(request, 'index.html', context)

def display_datacabels(request):
    items = Datacabels.objects.all()
    context= {
        'items': items,
        'header': 'Datacabels',
    }
    return render(request, 'index.html', context)

def display_speakers(request):
    items = Speakers.objects.all()
    context= {
        'items': items,
        'header': 'Speakers',
    }
    return render(request, 'index.html', context)

#======================== ADD VALUES======================================
def add_item(request,cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return  render(request, 'add_new.html', {'form':form})

'''
def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = LaptopForm()
        return  render(request, 'add_new.html', {'form':form})
'''
def add_laptop(request):
    return add_item(request, LaptopForm)

def add_USB(request):
    return add_item(request, USBForm)

def add_mobile(request):
    return add_item(request, MobileForm)

def add_memorycard(request):
    return add_item(request, MemoryCardForm)

def add_handfree(request):
    return add_item(request, HandfreeForm)

def add_charger(request):
    return add_item(request, ChargerForm)

def add_datacabels(request):
    return add_item(request, DatacabelsForm)

def add_speakers(request):
    return add_item(request, SpeakersForm)


#================================EDITING SECTIONS ===========================================
def edit_device(request, pk , model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance= item )
        return render(request, 'edit_item.html',{'form':form})

def edit_laptop(request, pk):
    return edit_device(request,pk, Laptop,LaptopForm)

def edit_mobile(request, pk):
    return edit_device(request,pk, Mobile,MobileForm)

def edit_usb(request, pk):
    return edit_device(request,pk, USB ,USBForm)

def edit_memorycard(request, pk):
    return edit_device(request,pk, MemmoryCard ,MemoryCardForm)

def edit_handfree(request, pk):
    return edit_device(request,pk, Handfree ,HandfreeForm)

def edit_charger(request, pk):
    return edit_device(request,pk, Charger ,ChargerForm)

def edit_datacabels(request, pk):
    return edit_device(request,pk, Datacabels ,DatacabelsForm)

def edit_speakers(request, pk):
    return edit_device(request,pk, Speakers ,SpeakersForm)

#============================== DELETE SECTION ==========================================
def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()
    items = Laptop.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)

def delete_USB(request, pk ):
    USB.objects.filter(id=pk).delete()
    items = USB.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)


def delete_mobile(request, pk ):
    Mobile.objects.filter(id=pk).delete()
    items = Mobile.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)

def delete_memmorycard(request, pk ):
    MemmoryCard.objects.filter(id=pk).delete()
    items = MemmoryCard.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)

def delete_handfree(request, pk ):
    Handfree.objects.filter(id=pk).delete()
    items = Handfree.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)

def delete_charger(request, pk ):
    Charger.objects.filter(id=pk).delete()
    items = Charger.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)

def delete_datacabel(request, pk ):
    Datacabels.objects.filter(id=pk).delete()
    items = Datacabels.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)

def delete_speaker(request, pk ):
    Speakers.objects.filter(id=pk).delete()
    items = Speakers.objects.all()

    context = {
        'items':items,
    }

    return render(request, 'index.html' , context)