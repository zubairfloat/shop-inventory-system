from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = {'type','price','status','issues'}

class USBForm(forms.ModelForm):
    class Meta:
        model = USB
        fields = {'type','price','status','issues'}

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = {'type','price','status','issues'}

class MemoryCardForm(forms.ModelForm):
    class Meta:
        model = MemmoryCard
        fields = {'type','price','status','issues'}

class HandfreeForm(forms.ModelForm):
    class Meta:
        model = Handfree
        fields = {'type','price','status','issues'}

class ChargerForm(forms.ModelForm):
    class Meta:
        model =  Charger
        fields = {'type','price','status','issues'}

class DatacabelsForm(forms.ModelForm):
    class Meta:
        model = Datacabels
        fields = {'type','price','status','issues'}

class SpeakersForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = {'type','price','status','issues'}