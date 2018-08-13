from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=20)
    grumpy = models.BooleanField(default=False)
    
Cat.object.create(
    name="Fluffy", "Mr.Bunns"
    breed="Persian", "British"
)

cat = Cat.object.get(id=1)
cats = Cat.object.filter(name__startswith="Mr")

fluffy = Cat.objects.get(id=1)
fluffy.name = "Mr.Fluffs"
fluffy.save()
