from django.test import TestCase
from .models import ibyiciro,Ahanu,Pics

# Create your tests here.
class ibyiciroTest(TestCase):

    # SetUp Class
    def setUp(self):
        self.name = ibyiciro(name = "fashion")
        
        
    def test_save_ciro(self):
        self.name.save_ciro()
        category = ibyiciro.objects.all()
        self.assertTrue(len(category)>= 1)
        
    def test_delete_ciro(self):
        self.name.save_ciro()
        categoria = self.name.delete_ciro()
        category = ibyiciro.objects.all()
        self.assertTrue(len(category) <= 1)


# class PicTest(TestCase):
    
#     # Setup method
#     def setUp(self):
#         self.hanu = Ahanu(hanu='Kigali')
#         self.hanu.save()
        
#         self.ciro = ibyiciro(ciro = 'fashion')
#         self.ciro.save()
        
#         self.pic = Pics(pic = 'food2.jpg')
        
        
#     def tearDown(self):
#         Image.objects.all().delete()
#         Location.objects.all().delete()
#         Category.objects.all().delete()
        
        
        
#     # Testing Instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.image,Image))
        
#     # testing the save method
#     def test_save_method(self):
#         self.image = Image(image = 'image1.jpg', image_name='test',image_description='This is a test image',date_taken='2017-2-28',location = self.location, category = self.category)
#         self.image.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) >= 1)
        
#     def test_delete_method(self):
#         self.image = Image(image = 'image1.jpg', image_name='test',image_description='This is a test image',date_taken='2017-2-28',location = self.location, category = self.category)
#         self.image.save_image()
#         images = self.image.delete_image()
#         deleted = Image.objects.all()
#         self.assertTrue(len(deleted) <= 0)
        
#     def test_update_method(self):
        
        
# class LocationTestClass(TestCase):
#     # SetUp Class
#     def setUp(self):
        
#         self.location = Location(location="Nairobi")
        
#     def tearDown(self):
#         Location.objects.all().delete()
        
#     def test_save_location(self):
#         self.location.save_location()
#         location = Location.objects.all()
#         self.assertTrue(len(location)>= 1)
        
#     def test_delete_location(self):
#         self.location.save_location()
#         locations = self.location.delete_location()
#         location = Location.objects.all()
#         self.assertTrue(len(location) <= 0)
        
