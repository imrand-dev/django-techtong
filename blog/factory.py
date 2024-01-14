from django.contrib.auth.models import User

import factory
from factory.faker import faker

from . import models

FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    title = factory.Faker(provider="sentence", nb_words=15)
    subtitle = factory.Faker(provider="sentence", nb_words=10)
    author = User.objects.get_or_create(username="Imran")[0]

    @factory.lazy_attribute
    def content(self):
        paragraphs = ""

        for _ in range(5):
            paragraphs += f"\n{FAKE.paragraph(nb_sentences=30)}\n"

        return paragraphs

    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add(
                "python",
                "django",
                "pytest",
                "javascript",
                "vscode",
                "deployment",
                "full-stack",
                "orm",
                "front-end",
                "back-end",
                "database",
            )
