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


class PicTest(TestCase):
    
    # Setup method
    def setUp(self):
        self.pic = Pics(pic = 'food2.jpg')
        
        
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pic,Pics))
        
   