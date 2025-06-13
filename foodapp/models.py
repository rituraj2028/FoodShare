from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    donor_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    food_description = models.TextField()
    quantity = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_description} by {self.donor_name}"
