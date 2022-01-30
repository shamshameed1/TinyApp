import datetime
from django.test import TestCase
from tinyapp.models import User, Url
from django.test import Client


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Katherine",
            last_name="Johnson",
            username="KJ",
            email="mathematics@nasa.com",
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password("!P4s5w0*d")
        self.user.save()
        self.url = Url.objects.create(
            short_url='lMN0as',
            long_url='https://www.youtube.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )

        self.url = Url.objects.create(
            short_url='52aBXO',
            long_url='https://www.instagram.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
        self.url = Url.objects.create(
            short_url='m4AdNj',
            long_url='https://www.google.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url = Url.objects.create(
            short_url='bu3xcc',
            long_url='https://www.asos.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url = Url.objects.create(
            short_url='s3HmsI',
            long_url='https://www.adidas.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
    def test_url_list_view_logged_in(self):
        c = Client()
        login_response = c.post('/login/',{'username':'KJ', 'password':'!P4s5w0*d'})   
        login_check = c.get('/login/')
        self.assertEqual(login_check.status_code, 200)
        self.assertEqual(login_response.url, '/urls')
        self.assertEqual(login_response.status_code, 302)

                  