# -*- coding: utf-8 -*-
#  python manage.py test misa -v 3 --keepdb
#  coverage run --source='.' manage.py test galaxy -v 3 --keepdb
#  coverage report
#  coverage html --omit="admin.py"
from __future__ import unicode_literals, print_function



from django.contrib.auth.models import AnonymousUser, User
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from gfiles.views import GFileCreateView


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_response(request)
    return request

class GFileCreateViewTestCase(TestCase):
    urls = 'galaxy.test_urls'
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')

    def test_login_redirect(self):
        """
        Test to check if a guest user is redirect to the login page
        """
        request = self.factory.get(reverse('upload_gfile'))

        print(self.user)
        request.user = AnonymousUser()
        request = add_middleware_to_request(request, SessionMiddleware)
        response = GFileCreateView.as_view()(request)
        print(response)

        # client acts as a fake website for the request
        response.client = Client()

        self.assertRedirects(response, '/login/?next=/upload_gfile/')
