from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('Telecom', 'Telecom'),
        ('ICT', 'ICT'),
        ('Power', 'Power & Energy'),
        ('Support', 'Support Services'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ICT')

    def __str__(self):
        return self.title


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Telecom', 'Telecom'),
        ('ICT', 'ICT'),
        ('Power', 'Power & Energy'),
        ('Support', 'Support Services'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ICT')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.name
