from django.test import TestCase
from models import Location,tags,Post
from datetime import dt
# Create your tests here.

class LocationTestCase(TestCase):

    #set up method
    def setUp(self):
        self.ruiru = Location(name = 'Ruiru')
    
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ruiru,Location))

class TagsTestCase(TestCase):

    #set up method
    def setUp(self):
        self.test = tags(cat = '#test')
    
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test,tags))
    
class PostTestCase(TestCase):
    def setUp(self):
        #create a location
        self.ruiru = Location(name = "Ruiru")
        self.ruiru.save_location()

        #create a category tag
        self.test = tags(cat = "Test")
        self.test.save_tag()

        self.new_post = Post(location = self.ruiru, tags= self.test, title='This is a test', caption= 'It will be cool')
        self.new_post.save()

        self.new_post.tags.add(self.test)

    def tearDown(self):
        Location.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()
    