from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name='category title')
    image = models.ImageField(upload_to='images/category_images/', verbose_name='category image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='category created time')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']
