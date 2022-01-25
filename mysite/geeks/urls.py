from django.urls import path

# importing views from views..py
"""
For detail_view one would need some identification to get a particular 
instance of the model. Usually it is primary key such as id. To specify
this identification we need to define it in urls.py. Go to geeks/urls.py
"""
from .views import detail_view
urlpatterns = [
    path('<id>', detail_view)
]
