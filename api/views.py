from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .serializers import ItemSerializer
from books.models import Item

# @api_view(['GET'])
# def getData(request):
#     person={'name':'Dennis','age':28}
#     return Response(person)


# Deals with requests related to single book in the model
@api_view(['GET','PUT','DELETE'])
def getDataDetail(request,id):
    # Trying to get the book by id
    try:
        book = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    # GET request is dealt here
    if request.method == 'GET':
        serializer= ItemSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # PUT request dealt here
    elif request.method == 'PUT':
        serializer=ItemSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message' : "Book updated successfully"
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({'error' : "Wrong input format"},status=status.HTTP_400_BAD_REQUEST)
    # DELETE a book of id
    elif request.method=='DELETE':
        book.delete()
        return Response({"message": "Book deleted successfully"},status=status.HTTP_204_NO_CONTENT)


    
# Deals with request related to books table
@api_view(['GET','POST'])
def getData(request):
    #GET request to get all table values
    if(request.method == 'GET'):
        items= Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # POST request to add a new book
    elif request.method == 'POST':
        serializer=ItemSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(
                {
                    'id' : book.id,
                    'message' : "Book added successfully"
                }, 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'error' : "Wrong input format"},status=status.HTTP_400_BAD_REQUEST
            )
