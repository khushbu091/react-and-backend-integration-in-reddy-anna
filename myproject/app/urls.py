from django.urls import path
from .views import get_blogs
from .views import submit_contact_form


urlpatterns = [
    path('blogs/', get_blogs, name='get_blogs'),  
    path("contact/", submit_contact_form, name="submit_contact_form"),  # ✅ Ensure this exists

]
