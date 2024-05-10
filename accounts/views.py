from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serealizers import UserSerializer,recipeSerializer
from accounts.models import AccountDetails,RecipesDetails

# Create your views here.
#user related api's
@api_view(['GET'])
def users(request):
    accounts_details = AccountDetails.objects.all()
    serealizer = UserSerializer(accounts_details, many=True)
    return Response(serealizer.data)

@api_view(['GET'])
def user(request, pk):
    account = AccountDetails.objects.get(user_name = pk)
    serializer = UserSerializer(account, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    account = AccountDetails.objects.get(user_email = pk)
    serializer = UserSerializer(instance=account, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    account = AccountDetails.objects.get(user_email = pk)
    account.delete()
    return Response("account deleted")

#recipe related api's
@api_view(['GET'])
def recipes(request):
    recipes_details = RecipesDetails.objects.all()
    serealizer = recipeSerializer(recipes_details, many=True)
    return Response(serealizer.data)

@api_view(['GET'])
def userrecipes(request, pk):
    account = RecipesDetails.objects.filter(user = pk)
    print(account)
    serializer = recipeSerializer(account, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchrecipes(request):
    search_query = request.query_params.get('q')
    if search_query:
        recipes_details = RecipesDetails.objects.filter(recipe_title__contains=search_query)
        if not recipes_details.exists():
            return Response({'error': 'No recipes found with the given search query.'})
        
    serializer = recipeSerializer(recipes_details, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addrecipe(request):
    serializer = recipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleterecipe(request, pk):
    recipe = RecipesDetails.objects.get(recipe_id = pk)
    recipe.delete()
    return Response("recipe deleted")

@api_view(['POST'])
def updaterecipe(request, pk):
    recipe = RecipesDetails.objects.get(recipe_id = pk)
    serializer = recipeSerializer(instance=recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)