from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class userdata(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    product_saledate = models. DateTimeField (null=True)
    qr_image = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     data = f"http://127.0.0.1:8000/readUserDetail/{self.id}/"
    #     qr_image = qrcode.make(data)
    #     qr_offset = Image.new('RGB', (310, 310), 'white')
    #     draw_img = ImageDraw.Draw(qr_offset)
    #     qr_offset.paste(qr_image)
    #     file_name = f'{self.name}-{self.id}qr.png'
    #     stream = BytesIO()
    #     qr_offset.save(stream, 'PNG')
    #     self.qr_image.save(file_name, File(stream), save=False)
    #     qr_offset.close()
        # super().save(*args, **kwargs)