from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    help_needed = models.TextField()
    needs_help = models.BooleanField(default=True)
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter_name = models.CharField(max_length=100)
    adopter_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Adoption request for {self.animal.name} by {self.adopter_name}"