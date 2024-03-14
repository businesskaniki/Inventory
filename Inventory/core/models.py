from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=45, default="soap")
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    dispatched = models.IntegerField(default=0)
    added = models.IntegerField(default=0)
    remaining = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    # Override the save method
    def save(self, *args, **kwargs):
        self.remaining = self.added - self.dispatched

        if not self.pk:  # If the object is being created
            last_item = Product.objects.order_by("-id").first()  # Get the last item
            if last_item:
                self.item_number = str(
                    int(last_item.item_number) + 1
                )  # Increment the item number
            else:
                self.item_number = "1"  # Start with 1 if no items exist

            if self.remaining <= 0:
                self.in_stock = False
            else:
                self.in_stock = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_number
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add more fields as needed
