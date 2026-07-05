from django.db import models
from django.core.validators import RegexValidator

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class CommonProblem(models.Model):
    title = models.CharField(max_length=255, unique=True)
    def __str__(self): return self.title

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_validator = RegexValidator(regex=r'^\d{10}$', message="ስልክ ቁጥር 10 ዲጂት መሆን አለበት!")
    phone_number = models.CharField(validators=[phone_validator], max_length=10, unique=True)
    
    def __str__(self): return f"{self.name} ({self.phone_number})"
    
    @property
    def visit_count(self): return self.tvrepair_set.count()
    
    @property
    def star_rating(self):
        count = self.visit_count
        if count >= 5: return "⭐⭐⭐ (VIP)"
        elif count >= 3: return "⭐⭐"
        elif count >= 2: return "⭐"
        return "Regular"

class TVRepair(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending (ገና ያልተጠገነ)'),
        ('IN_PROGRESS', 'In Progress (በጥገና ላይ ያለ)'),
        ('REPAIRED_UNCLAIMED', 'Repaired (ተጠግኖ ያልወጣ)'),
        ('DELIVERED', 'Delivered (ተጠግኖ የወጣ)'),
    ]
    WARRANTY_CHOICES = [('IN_WARRANTY', 'In Warranty'), ('OUT_WARRANTY', 'Out of Warranty')]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model_number = models.CharField(max_length=100)
    problem = models.ForeignKey(CommonProblem, on_delete=models.PROTECT)
    warranty_status = models.CharField(max_length=20, choices=WARRANTY_CHOICES, default='IN_WARRANTY')
    warranty_void_reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return f"{self.brand.name} - {self.model_number}"