from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from api.serializers import ItemSerializer,UsersSerializer
from books.models import Item
from .models import Users

# Deals with requests related to single user in the model
# GET
    # returns "User not found" if entered user doesn't exist
    # else returns the data of the particular user

# POST
    # returns "User not found" if entered user doesn't exist
    # returns "Book not found" error if bookId given as input deosn't exist
    # returns "Book is already in favorites" if book already exits in the favourites list
    # else add and return "Book added to favourites" message


@api_view(['GET','POST','PUT'])
def getUserData(request,userId):
    # Trying to get the user by userId field
    try:
        user = Users.objects.get(userId=userId)
    except Users.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # GET request is dealt here
    if request.method == 'GET':
        serializer= ItemSerializer(user.favourites.all(),many=True) #Get the users favourite books using itemserializer
        return Response(
            {
                "userId" : user.userId,
                "favorites" : serializer.data
            },
            status=status.HTTP_200_OK
        )

    # POST request to add a book to a user's favorites
    elif request.method == 'POST':
        book_id= request.data.get('bookId')
        try:
            book = Item.objects.get(id = book_id)
        except:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if user.favourites.filter(id=book_id).exists():
            return Response({"message": "Book is already in favorites"}, status=status.HTTP_400_BAD_REQUEST)
        
        user.favourites.add(book)
        return Response({"message": "Book added to favorites"}, status=status.HTTP_201_CREATED)

    # PUT request to share a book with another user
    elif request.method == 'PUT':
        book_id= request.data.get('bookId')
        try:
            book = Item.objects.get(id = book_id)
        except:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user_2_id = request.data.get('userId')
        try:
            user_2 = Users.objects.get(userId=user_2_id)
        except Users.DoesNotExist:
            return Response({'error': 'User 2 not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.favourites.add(book)
        user_2.favourites.add(book)
        return Response({"message": "Book shared successfully"}, status=status.HTTP_201_CREATED)
    
# DELETE
    # returns "User not found" if entered user doesn't exist
    # returns "Book not found" error if bookId given as input deosn't exist
    # returns "Book is not in favorites" if book doesn't exit in the favorites list
    # else delete and return "Book removed from favorites" message

@api_view(['DELETE'])
def delete_user_book(request,userId,bookId):
    try:
        user = Users.objects.get(userId=userId)
    except user.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        book = Item.objects.get(id=bookId)
    except book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    if not user.favourites.filter(id=bookId).exists():
        return Response({'message': 'Book is not in favorites'}, status=status.HTTP_400_BAD_REQUEST)

    user.favourites.remove(book)
    return Response({"message": "Book removed from favorites"}, status=status.HTTP_204_NO_CONTENT)