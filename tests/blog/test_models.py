import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):
        post_title = post_factory()
        assert post_title.__str__() == "Test Post Title"

    def test_add_tag(self, post_factory):
        post_title = post_factory(tags=["test-tag"])
        assert post_title.tags.count() == 1
