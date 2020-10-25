from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 60)    

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']

    def save_category(self):
        self.save()

    
    
class Location(models.Model):
    name = models.CharField(max_length= 40)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Post(models.Model):    
    title = models.CharField(max_length= 60)
    caption= models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length= 60)
    post_date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'posts/')

    @classmethod
    def get_posts(cls):
        posts = cls.objects.order_by('-post_date')
        return posts

    @classmethod 
    def get_location_post(cls,id):
        posts = cls.objects.filter(location__id = id)
        return posts

    @classmethod
    def search_by_category(cls,search_term):
        post = cls.objects.filter(category__name=search_term)
        return post