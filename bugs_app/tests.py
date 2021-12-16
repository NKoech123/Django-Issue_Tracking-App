from django.test import TestCase
from django.urls import reverse, resolve
from bugs_app.views import list_bugs, bug_delete, bug_add  #imports methods from views
# Create your tests here.
# Create your tests here.
class URLTests(TestCase):
    #check if the homepage URL is working
    def test_testbuglistURL(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        url=reverse('bug_list')
        self.assertEquals(resolve(url).func, list_bugs)
        print(resolve(url))
        
    
    def test_testbug_formURL(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200) 
        url=reverse('bug_form')
        self.assertEquals(resolve(url).func, bug_add)
        print(resolve(url)) 

    def test_testbug_deleteURL(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200) 
        url=reverse('bug_delete')
        self.assertEquals(resolve(url).func, bug_delete)
        print(resolve(url))  
        