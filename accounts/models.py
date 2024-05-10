from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class AccountDetails(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(primary_key=True,max_length=25, unique=True)
    user_password = models.CharField(max_length=20)

    def __str__(self):
          return self.user_name

class RecipesDetails(models.Model):
    recipe_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(AccountDetails, on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=50)
    recipe_description = models.TextField()
    recipe_created_at = models.DateTimeField(auto_now_add=True)
    recipe_ratings = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)

    def __str__(self):
          return self.recipe_title