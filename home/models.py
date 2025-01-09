from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    adres = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    smtp_email = models.CharField(max_length=100)
    smtp_pasword = models.CharField(max_length=100)
    smtp_port = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    icone = models.ImageField(null=False, upload_to='images/')
    aboutus = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


from django.db import models


# Create your models here.
class SettingLang(models.Model):
    setting = models.ForeiginKey(Setting,one_delate=models.CASCADEC)
    lang = models.CharField(max_length=6,choices=lanlist)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    adres = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    smtp_email = models.CharField(max_length=100)
    smtp_pasword = models.CharField(max_length=100)
    smtp_port = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    icone = models.ImageField(null=False, upload_to='images/')
    aboutus = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.title

