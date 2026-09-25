from django.test import TestCase
from . models import PostModel
from django.urls import reverse


class PostModelTest(TestCase):
    def setUp(self):
        PostModel.objects.create(text = "Test Text")

    def test_test_context(self):
        post = PostModel.objects.get(id=1)
        post_text = f'{post.text}'
        self.assertEqual(post_text,'Test Text')

class TestHomePageView(TestCase):
    def setUp(self):
        PostModel.objects.create(text = "It is for checking !")

    def test_url(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code,200)

    def test_url_by_name(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code,200)

    def test_correct_template(self):
        resp = self.client.get(reverse("home"))
        resp2 = self.client.get(reverse("list"))
        self.assertEqual(resp.status_code,200)
        self.assertEqual(resp2.status_code,200)
        self.assertTemplateUsed(resp,'base.html')
        self.assertTemplateUsed(resp2,'list.html')