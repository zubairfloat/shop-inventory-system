from django.conf.urls import url
from .views import *


urlpatterns =[
    url(r'^$', index , name='index'),
    url(r'^display_laptop$', display_laptops, name="display_laptops"),
    url(r'^display_USB$', display_USB, name="display_USB"),
    url(r'^display_mobile$', display_mobiles, name="display_mobiles"),
    url(r'^display_memorycard$', display_memorycard, name="display_memorycard"),
    url(r'^display_handfree$', display_handfree, name="display_handfree"),
    url(r'^display_charger$', display_charger, name="display_charger"),
    url(r'^display_datacabels$', display_datacabels, name="display_datacabels"),
    url(r'^display_speakers$', display_speakers, name="display_speakers"),


    url(r'^add_laptop$', add_laptop, name="add_laptop"),
    url(r'^add_USB$', add_USB, name="add_USB"),
    url(r'^add_mobile$', add_mobile, name="add_mobile"),
    url(r'^add_memorycard$', add_memorycard, name="add_memorycard"),
    url(r'^add_handfree$', add_handfree, name="add_handfree"),
    url(r'^add_charger$', add_charger, name="add_charger"),
    url(r'^add_datacabels$', add_datacabels, name="add_datacabels"),
    url(r'^add_speakers$', add_speakers, name="add_speakers"),


    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name="edit_laptop"),
    url(r'^edit_mobile/(?P<pk>\d+)$', edit_mobile, name="edit_mobile"),
    url(r'^edit_usb/(?P<pk>\d+)$', edit_usb, name="edit_usb"),
    url(r'^edit_memorycard/(?P<pk>\d+)$', edit_memorycard, name="edit_memorycard"),
    url(r'^edit_handfree/(?P<pk>\d+)$', edit_handfree, name="edit_handfree"),
    url(r'^edit_charger/(?P<pk>\d+)$', edit_charger, name="edit_charger"),
    url(r'^edit_datacabels/(?P<pk>\d+)$', edit_datacabels, name="edit_datacabels"),
    url(r'^edit_speakers/(?P<pk>\d+)$', edit_speakers, name="edit_speakers"),

    url(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name= "delete_laptop"),
    url(r'^delete_USB/(?P<pk>\d+)$', delete_USB, name= "delete_USB"),
    url(r'^delete_mobile/(?P<pk>\d+)$', delete_mobile, name= "delete_mobile"),
    url(r'^delete_memmorycard/(?P<pk>\d+)$', delete_memmorycard, name= "delete_memmorycard"),
    url(r'^delete_handfree/(?P<pk>\d+)$', delete_handfree, name= "delete_handfree"),
    url(r'^delete_charger/(?P<pk>\d+)$', delete_charger, name= "delete_charger"),
    url(r'^delete_datacabel/(?P<pk>\d+)$', delete_datacabel, name= "delete_datacabel"),
    url(r'^delete_speaker/(?P<pk>\d+)$', delete_speaker, name= "delete_speaker"),


]