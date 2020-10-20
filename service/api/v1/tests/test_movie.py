"""
Movie Tests.
"""
import uuid
import json
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group, User
from service.core.test import OAuth2Mixin, AssertStatusMixin


class TestMovie(OAuth2Mixin, AssertStatusMixin, APITestCase):
    """
    Test movie endpoints.
    """

    def create_admin_user(self, username):
        new_user = User.objects.create_user(username=username,
                                            password=uuid.uuid4().hex)
        admin_group, created = Group.objects.update_or_create(name='admin')
        admin_group.user_set.add(new_user)
        return new_user

    def setUp(self):
        super(TestMovie, self).setUp()
        self.url = reverse_lazy('api-v1:movie-list')
        self.admin = self.create_admin_user('admin')
        self.data = {
            "name": "string",
            "popularity": 81.2,
            "director": {
                "name": "Fredicson"
            },
            "genres": [
                {
                    "name": "RomCom"
                },
                {
                    "name": "Thriller"
                }
            ],
            "imdb_score": 8.1
        }

    def test_get_request_from_anonymous(self):
        """
        A GET request from anonymous should return a 200
        """
        response = self.client.get(self.url)
        expected_output = {'count': 0, 'next': None, 'previous': None, 'results': []}
        self.assertEqual(json.loads(response.content), expected_output)
        self.assert200(response)

    def test_delete_request_from_admin(self):
        """
        A DELETE request should return a 405
        """
        http_authorization = self.get_authorization_header(self.admin)
        response = self.client.delete(self.url, HTTP_AUTHORIZATION=http_authorization)
        self.assert405(response)

    def test_delete_request_from_anonymous(self):
        """
        A DELETE request from anonymous should return a 401
        """
        response = self.client.delete(self.url)
        self.assert401(response)

    def test_post_request_from_anonymous(self):
        """
        A POST request from anonymous should return a 401
        """
        response = self.client.post(self.url)
        self.assert401(response)

    def test_put_request_from_anonymous(self):
        """
        A PUT request from anonymous should return a 401
        """
        response = self.client.put(self.url)
        self.assert401(response)

    def test_valid_post_request(self):
        """
        A valid POST request should return a 201
        """
        http_authorization = self.get_authorization_header(self.admin)
        response = self.client.post(self.url, HTTP_AUTHORIZATION=http_authorization, data=json.dumps(self.data),
                                    content_type="application/json")
        self.assert201(response)

    def test_invalid_post_request_with_incomplete_data(self):
        """
        A invalid POST request should return a 400
        """
        data = self.data
        data.pop("genres")
        http_authorization = self.get_authorization_header(self.admin)
        response = self.client.post(self.url, HTTP_AUTHORIZATION=http_authorization, data=json.dumps(data),
                                    content_type="application/json")
        self.assert400(response)

    def test_get_request_with_data(self):
        """
        A GET request should return data
        """
        http_authorization = self.get_authorization_header(self.admin)

        post_response = self.client.post(self.url, HTTP_AUTHORIZATION=http_authorization, data=json.dumps(self.data),
                                         content_type="application/json")
        get_response = self.client.get(self.url)
        self.assertEqual(json.loads(get_response.content).get("count"), 1)
        self.assert201(post_response)

    def test_valid_put_request(self):
        """
        A valid PUT request should return a 200
        """
        http_authorization = self.get_authorization_header(self.admin)
        post_response = self.client.post(self.url, HTTP_AUTHORIZATION=http_authorization, data=json.dumps(self.data),
                                         content_type="application/json")
        get_response = self.client.get(self.url)
        record_id = json.loads(get_response.content).get("results")[0].get('id')
        updated_data = self.data
        updated_data.update({"genres": [{"name": "Comedy"}, {"name": "Action"}]})
        put_response = self.client.put(self.url + "{}/".format(record_id), HTTP_AUTHORIZATION=http_authorization,
                                       data=json.dumps(updated_data),
                                       content_type="application/json")
        expected_data = {
            "id": 1,
            "name": "string",
            "popularity": 81.2,
            "director": {
                "name": "Fredicson"
            },
            "genres": [
                {
                    "name": "Comedy"
                },
                {
                    "name": "Action"
                }
            ],
            "imdb_score": 8.1
        }
        self.assert200(get_response)
        self.assert201(post_response)
        self.assert200(put_response)
        self.assertEqual(json.loads(put_response.content), expected_data)
