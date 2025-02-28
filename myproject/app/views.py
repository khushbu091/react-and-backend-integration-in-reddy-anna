from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Blog, ContactForm
from .serializers import BlogSerializer, ContactFormSerializer

from rest_framework.decorators import api_view


@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)




@api_view(["POST"])
def submit_contact_form(request):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    phone = request.data.get("phone")
    message = request.data.get("message")
    date = request.data.get("date")

    contact = ContactForm.objects.create(
        first_name=first_name, last_name=last_name, email=email,
        phone=phone, message=message, date=date
    )

    return Response({"message": "Contact form submitted successfully!"}, status=201)

@api_view(['GET'])
def get_contact_forms(request):
    contacts = ContactForm.objects.all().order_by('-date')
    serializer = ContactFormSerializer(contacts, many=True)
    return Response(serializer.data)
