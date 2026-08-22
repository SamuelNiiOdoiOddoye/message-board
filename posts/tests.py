from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    
    #this is to test 
    def setUpTestData(cls):
        # Create a test post
        cls.post = Post.objects.create(text="This is a test post.")
    
    #this is to test
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test post.")
    
    #this is to     
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    #this is to test     
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    #this is to test     
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "This is a test post.")