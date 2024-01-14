import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestHomePage:
    def test_home_page_url(self, client):  # A Django test client instance.
        url_ = reverse("home")
        response = client.get(url_)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client):
        headers = {"HTTP_HX-Request": "true"}
        response = client.get(reverse("home"), **headers)
        assertTemplateUsed(
            response=response, template_name="blog/components/post-list-elements.html"
        )
