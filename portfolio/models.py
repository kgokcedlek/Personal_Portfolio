from django.db import models

# Create your models here.
#modeller oop yaspisi mantiginda kullanim icin cok iyidir. tum proje database islemlerini olustuaracagin model yapisindaki objelerle yurutmek icin iyi.
#projede database ile ilgili islemlerin calistirmak icin terminalden "python manage.py migrate" komutunu calistirmak gerek.
#ama yukaridaki komut projede migrationi yapilmis tum database islemlerinin entegre edilmesini sagliyor.
#kendi olusturdugun database modellerini, islemlerini projeye entegre etmek icin ilk olarak "python manage.py makemigrations" komutunu calistirman ardindan
#"python manage.py migrate" komutunu calistirmak gerek.
class Project(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=250,blank=True)
    image = models.ImageField(upload_to='portfolio/images/',blank=True)
    url = models.URLField(blank=True)
