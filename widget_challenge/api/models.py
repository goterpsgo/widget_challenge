from django.db import models

class Finish(models.Model):
    """This class represents the widget finish."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Size(models.Model):
    """This class represents the widget size."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Category(models.Model):
    """This class represents the widget categories."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Widget(models.Model):
    """This class represents the widget."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    inventory = models.IntegerField(default=0, null=False, blank=False)
    finish = models.ForeignKey('Finish', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Order(models.Model):
    """This class represents the orders."""

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.id)

class OrderItem(models.Model):
    """This class represents the items in the order."""
    count = models.IntegerField(default=1, null=False, blank=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='orderitems')
    widget = models.ForeignKey('Widget', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.order)
