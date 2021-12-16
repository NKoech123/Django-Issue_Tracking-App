from django.test import TestCase
from projects_app.views import home, add_project  #imports from views
from django.urls import reverse, resolve
from projects_app.models import Project

# Create your tests here.
class URLTests(TestCase):
    #check if the homepage URL is working
    def test_testhomepageURL(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        url=reverse('home')
        self.assertEquals(resolve(url).func, home)
        print(resolve(url))
        
    

    def test_addprojectURL(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200) 
        url=reverse('addproject')
        self.assertEquals(resolve(url).func, add_project)
        print(resolve(url))  
        

   
class TestMyViews(TestCase):
    pass


class TestModels(TestCase):
    pass