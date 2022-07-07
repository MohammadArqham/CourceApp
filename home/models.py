
from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf.urls.static import static

class cource_user(models.Model):

    LABELS = (
        ('1', 'Teacher'),
        ('2', 'Student🔥'),
    )   

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(choices=LABELS,max_length=225)
    image = models.ImageField(default='default.png', upload_to='profile_images')
    des = models.CharField(max_length=250,blank=True)
    detailed_discription = models.TextField(null=True,blank=True,default='No Discription')
    experience  = models.IntegerField(default='2')
    rating = models.FloatField(max_length=5)

    



class Cource(models.Model):
    LABELS = (
        (1, 'latest'),
        (2, 'popular'),
        (3, 'art'),
        (4, 'Knowledge'),
        (5, 'Programing'),
        (6, 'Basic skills'),
        (7, 'setup, productivity and quality'),
        (8, 'busness'),
        (9, 'gaming'),
        (10, 'Advanced skills and Knowledge'),
        (11, 'outher'),

    ) 
    author = models.ForeignKey(cource_user,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    des = models.CharField(max_length=250,blank=True)
    price = models.FloatField()
    duration = models.IntegerField(default=1)
    image = models.ImageField(default='default.png', upload_to='cource_images')
    rating = models.FloatField(max_length=5)
    date = models.DateField(default=timezone.now)
    detailed_discription = models.TextField(null=True,blank=True,default='No Discription')
    preview_video = models.FileField(null=True,blank=True,upload_to='preview_video/')
    pdf = models.FileField(null=True,blank=True,upload_to='pdf/')
    category = models.CharField(choices=LABELS,blank=True,max_length=225)
    
    ########################################################
    bought = models.IntegerField()
    impresions = models.IntegerField()
    clicks = models.IntegerField()
    
    #######################################################


    def __str__(self):
        return self.name

class tags(models.Model):
    cource = models.ForeignKey(Cource,on_delete=models.CASCADE)
    tag = models.CharField(max_length=250,blank=False)

    def __str__(self):
        return self.tag

class cart(models.Model):
    name = models.ForeignKey(cource_user,on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource,on_delete=models.CASCADE)

    def __str__(self):
        return self.cource.name

class my_cources(models.Model):
    name = models.ForeignKey(cource_user,on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource,on_delete=models.CASCADE)

    def __str__(self):
        return self.cource.name

class comment(models.Model):
    name = models.ForeignKey(cource_user,on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource,on_delete=models.CASCADE)
    comment=models.TextField(blank=False,null=False)
    date = models.DateField(default=timezone.now)
   
    def __str__(self):
        return self.comment
