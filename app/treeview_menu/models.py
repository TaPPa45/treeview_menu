from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Название", max_length=100)
    url = models.CharField("URL", max_length=200, blank=True)
    named_url = models.CharField("Именованный URL", max_length=100, blank=True)
    order = models.IntegerField("Порядок", default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
    
    def __str__(self):
        return self.name
    
    def save(self):
        if not self.url.endswith('/'):
            self.url +='/'
        if not self.url.startswith('/'):
            self.url ='/' + self.url
        return super().save()
    
    