from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateField
from django.utils.translation import gettext_lazy as _
from PIL import Image
import datetime

#----------------------Menu barlarni qayd qilish-----------------------------------#
class Sidebar(models.Model):
    title=models.CharField(max_length=20)
    url_name=models.CharField(max_length=20)
    menu_name=models.CharField(max_length=20)
    icon_name=models.CharField(max_length=40)
    

    def __str__(self):
        return self.menu_name
  
class Submenu(models.Model):
    title=models.CharField(max_length=20)
    url_name=models.CharField(max_length=20)
    menu_name=models.CharField(max_length=20)
    icon_name=models.CharField(max_length=40,blank=True)
    

    def __str__(self):
        return self.menu_name
#--------------------------------kadrlarni qayd etish------------------------------------------------#  
class Staff(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    birthday=models.DateField(auto_now=False,blank=False)
    position=models.OneToOneField('Position',on_delete=CASCADE)
    position_number=models.IntegerField()
    pasport=models.CharField(max_length=20)
    stir_num=models.CharField(null=True,max_length=20)
    image=models.ImageField()


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        size1=300,300

        if self.image:
            pic=Image.open(self.image.path)
            pic.thumbnail(size1,Image.LANCZOS)
            pic.save(self.image.path) 

    def __str__(self):
        return self.first_name
     

class Position(models.Model):
    position_name=models.CharField(max_length=40,blank=False)

    def __str__(self):
        return self.position_name
     
class Tabel(models.Model):
    choices=[
        ('Keldi','Keldi'),
        ('Kelmadi','Kelmadi')
    ]
    staff=models.ForeignKey(Staff,on_delete=SET_NULL,null=True)
    date = models.DateField(default=datetime.date.today)
    public=models.CharField(choices=choices,max_length=20)
    

    def __str__(self):
        return self.public

