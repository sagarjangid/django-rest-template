"""
Base test runner.
"""
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
from oauth2_provider.models import get_application_model, AccessToken, RefreshToken


class AssertStatusMixin(object):
    """
    Shortcuts to assert response codes.
    """

    def assert200(self, response):
        """
        Assert a 200 response
        """
        self.assertEquals(response.status_code, 200)
        return response

    def assert201(self, response):
        """
        Assert a 201 created response
        """
        self.assertEquals(response.status_code, 201)
        return response

    def assert400(self, response):
        """
        Assert a 400 response
        """
        self.assertEquals(response.status_code, 400)
        return response

    def assert401(self, response):
        """
        Assert a 401 response
        """
        self.assertEquals(response.status_code, 401)
        return response

    def assert403(self, response):
        """
        Assert a 403 response
        """
        self.assertEquals(response.status_code, 403)
        return response

    def assert404(self, response):
        """
        Assert a 404 response
        """
        self.assertEquals(response.status_code, 404)
        return response

    def assert405(self, response):
        """
        Assert a 405 response
        """
        self.assertEquals(response.status_code, 405)
        return response


class OAuth2Mixin(object):

    def setUp(self):
        self.create_oauth2_application()

    def create_oauth2_application(self):
        user_model = get_user_model()

        application_user = user_model.objects.create_user(
            'application_user@test')
        application_user.save()

        Application = get_application_model()
        self.oauth2_application = Application.objects.create(
            name='test_application',
            client_id='hEk5hpYrWaWkjSgIUJ5F9VnWx6mxnhz78j6R2ya5',
            client_secret='client_secret',
            redirect_uris='',
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
            user=application_user,
        )
        self.oauth2_application.save()

    def get_access_token(self, user, scope, token_name='access_token'):
        access_token = AccessToken.objects.create(
            token=token_name,
            application=self.oauth2_application,
            user=user,
            expires=timezone.now() + timedelta(days=1),
            scope=scope or 'read write',
        )

        return access_token

    def get_refresh_token(self, user, access_token):
        refresh_token = RefreshToken.objects.create(
            user=access_token.user,
            access_token=access_token,
            application=self.oauth2_application,
        )

        return refresh_token

    def get_authorization_header(self, user, scope=None, token_name='access_token'):
        access_token = self.get_access_token(user, scope, token_name)

        return "Bearer {0}".format(access_token.token)

