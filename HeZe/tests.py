from django.test import TestCase
from PIL import Image
# Create your tests here.
image = Image.open('C:\images\c70b0191c65e5c8e029bbbcee980adca.png')
print(image.size())



