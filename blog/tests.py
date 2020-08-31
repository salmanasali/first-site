from django.urls import resolve
from django.test import TestCase
from blog.views import post_list, post_edit


class HomePageTest(TestCase):
   
    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)

    
    def test_post_list_returns_correct_html(self):
       response = self.client.get('/')
       html = response.content.decode('utf8')
       self.assertTrue(html.strip().startswith('<html>'))
       self.assertIn('<title>Salman Asali</title>', html)
       self.assertIn('<h1><a>My Posts</a></h1>', html)
       self.assertTrue(html.strip().endswith('</html>'))
       self.assertTemplateUsed(response, 'blog/post_list.html')

        

        
