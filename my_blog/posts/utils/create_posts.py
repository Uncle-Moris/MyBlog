from random import randint
from faker import Faker
from my_blog.posts.models import Post

fake = Faker()


def create_fake_posts(n: int = 10):
    for _ in range(n):

        Post.objects.create(
            title=fake.text(randint(10, 15)),
            content=fake.text(randint(100,1000))
        )