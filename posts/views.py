from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

posts = [
  {
    "id": 1,
    "name": "Example 1",
    "author": "John Doe"
  },
  {
    "id": 2,
    "name": "Example 2",
    "author": "Jane Doe"
  },
  {
    "id": 3,
    "name": "Example 3",
    "author": "Mike Johnson"
  }
]

@api_view(["GET", "POST"])
def home(request:Request):
    if request.method == "POST":
        data = request.data

        response = {"message": "Basic post request", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(["GET"])
def list_posts(request):
    """ listing posts from temporary created data with list """
    return Response(data=posts, status=status.HTTP_200_OK)

@api_view(["GET"])
def detail_post(request, post_id):
    post = posts[post_id]

    if post:
        return Response(data=post, status=status.HTTP_200_OK)
    
    return Response(data={"error": "post not found"}, status=status.HTTP_404_NOT_FOUND)