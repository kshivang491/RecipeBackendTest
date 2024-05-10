from django.contrib import admin
from accounts.models import AccountDetails, RecipesDetails

# Register your models here.
class personalAccountdetails(admin.ModelAdmin):
    list_display = ('user_name','user_email','user_password')

admin.site.register(AccountDetails,personalAccountdetails)


class recipes(admin.ModelAdmin):
    list_display = ('recipe_id','user','recipe_title','recipe_description','recipe_created_at','recipe_ratings')

admin.site.register(RecipesDetails, recipes)