from django.db import models

# Create your models here.

class Device(models.Model):

    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased '),
        ('SOLD ', 'Item Sold'),
        ('RESTOCKING ', 'Item restocking in few days ')
    )

    status = models.CharField(max_length=10, choices= choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues ")

    class Meta:
        abstract = True


    def __str__(self):
        return 'Type: {0} price: {1}'.format(self.type, self.price)

class Laptop(Device):
    pass

class USB(Device):
    pass

class Mobile(Device):
    pass

class MemmoryCard(Device):
    pass

class Charger(Device):
    pass

class Handfree(Device):
    pass

class Datacabels(Device):
    pass

class Speakers(Device):
    pass

