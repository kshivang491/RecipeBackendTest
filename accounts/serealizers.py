from rest_framework import serializers
from accounts.models import AccountDetails, RecipesDetails

class recipeSerializer(serializers.ModelSerializer):
    user_name=serializers.ReadOnlyField(source = 'user.user_name')
    class Meta:
        model = RecipesDetails
        fields = "__all__"
        read_only_fields = ('user','recipe_id','recipe_created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = "__all__" 