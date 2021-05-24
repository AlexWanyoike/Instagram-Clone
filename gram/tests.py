from django.test import TestCase
from .models import Image, Comment, Profile, Follow
from django.contrib.auth.models import User
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.alex = User(username = "alex", email = "code.wanyoike@gmail.com", password = "@Roverson12345")
        self.profile = Profile(bio='bio', user=self.alex)
        self.home = Image(image = 'imageurl', name ='banglow', caption = 'Its amazing', profile = self.profile)

        self.alex.save()
        self.profile.save()
        self.home.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.home, Image))

    def test_save_image_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.home.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        self.home.update_caption('Pasta')
        self.assertEqual(self.home.caption, 'Pasta')

    def test_get_profile_images(self):
        self.book.save_image()
        images = Image.get_profile_images(self.profile)
        self.assertEqual(len(images),2)