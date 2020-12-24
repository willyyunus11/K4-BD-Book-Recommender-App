from django.db import models

# Create your models here.
class Book(models.Model):
  id = models.CharField(max_length=225, primary_key=True)
  title = models.CharField(max_length=50)
  # isbn
  # isbn13
  # asin
  # kindle_asin
  # country_code
  image_url = models.CharField(max_length=200)
  small_image_url = models.CharField(max_length=200)
  large_image_url = models.CharField(max_length=200)
  publication_year = models.CharField(max_length=10)
  publication_month = models.CharField(max_length=10)
  publication_day = models.CharField(max_length=10)
  publisher = models.CharField(max_length=100)
  # language_code
  is_ebook = models.CharField(max_length=10)
  description = models.CharField(max_length=200)
  average_rating = models.CharField(max_length=3)
  num_pages = models.CharField(max_length=5)
  # format
  edition_information = models.CharField(max_length=10)
  # text_reviews_count
  url = models.CharField(max_length=200)
  link = models.CharField(max_length=200)
