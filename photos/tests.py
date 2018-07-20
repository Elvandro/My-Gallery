from django.test import TestCase
from . models import Location, Category, Image
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):
    def setup(self):
        self.test_location = Location(location="Luzhniki Stadium, Russia")

class CategoryTestClass(TestCase):
    def setup(self):
        self.test_category = category(category="Success story")

class ImageTestClass(TestCase):
    def setUp(self):
        # Location
        self.test_location = Location(location="Luzhniki Stadium, Russia")
        self.test_location.save()
        # Category
        self.test_category = Category(category="Success story")
        self.test_category.save()
        # Image
        self.test_image = Image(image="testImage",
                                image_url="testImageurl",
                                image_name="Test",
                                description="This is a test",
                                location=self.test_location)
        self.test_image.save()
        self.test_image.category.add(self.test_category)

    def test_instance(self):
        self.asserTrue(isinstance(self.test_image, Image))

    def test_saving_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
