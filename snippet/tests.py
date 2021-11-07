from django.test import TestCase
from .models import Snippets
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
# Create your tests here.

class TestSnippet(TestCase):
    def test_snippet_post(self):
        # movie = Movie.objects.create(title='original title')
        print('POST Snippet')
        user = get_user_model()(username='test', password='As@12345'
        ,email="test@yopmail.com",first_name="test",last_name="tt")
        user.save()
        user = get_user_model().objects.get(username='test')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post(f'/snippets/snippet/', {
            
                "title":"test",
                "message":"test",
                "tags":[
                    {"title":"test2"}
                ]
                
            
        }, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        
        # ...add more specific asserts

    def test_snippet_put(self):
        print('PUT Snippet')
        user = get_user_model()(username='test', password='As@12345'
        ,email="test@yopmail.com",first_name="test",last_name="tt")
        user.save()
        client = APIClient()
        client.force_authenticate(user=user)
        snippet = Snippets(title="test",message="test",author=user)
        snippet.save()
        response = client.put(f'/snippets/snippet/{snippet.pk}/', {
            
                "title":"test2",
                "message":"test2",
                "tags":[
                    {"title":"test"},
                    {"title":"test2"}
                ]
                
            
        }, format='json')
        self.assertEqual(response.status_code, 200, response.content)

    def test_snippet_delete(self):
        print('Delete Snippet')
        user = get_user_model()(username='test', password='As@12345'
        ,email="test@yopmail.com",first_name="test",last_name="tt")
        user.save()
        client = APIClient()
        client.force_authenticate(user=user)
        snippet = Snippets(title="test",message="test",author=user)
        snippet.save()
        response = client.delete(f'/snippets/snippet/{snippet.pk}/', {
            
        }, format='json')
        self.assertEqual(response.status_code, 200, response.content)
