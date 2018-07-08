import unittest
import home_app
from PIL import Image


class TestMyCode(unittest.TestCase):

    def setUp(self):
        print('Подготовка для тестов')

    def tearDown(self):
        print('Прибираемся после завершения теста')

    def test_for_app(self):
        image = Image.open('background.jpg')
        width1 = 300
        height1 = 300
        result1 = home_app.HomeApp.convert_image(image, width1, height1)
        new_image1 = image.resize((width1, height1))
        self.assertEqual(new_image1.size, result1.size)
        width2 = 300
        height2 = None
        result2 = home_app.HomeApp.convert_image(image, width2, height2)
        ratio = int(width2) / image.size[0]
        height_ratio = int((float(image.size[1]) * float(ratio)))
        new_image2 = image.resize((int(width2), height_ratio))
        self.assertEqual(new_image2.size, result2.size)
        width3 = None
        height3 = 400
        result3 = home_app.HomeApp.convert_image(image, width3, height3)
        ratio = int(height3) / image.size[1]
        width_ratio = int((float(image.size[0]) * float(ratio)))
        new_image3 = image.resize((width_ratio, int(height3)))
        self.assertEqual(new_image3.size, result3.size)
        width4 = None
        height4 = None
        result4 = home_app.HomeApp.convert_image(image, width4, height4)
        self.assertEqual(ValueError, result4)


