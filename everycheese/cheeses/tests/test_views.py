import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse


from .factories import CheeseFactory
from ..models import Cheese
from ..views import (
    CheeseListView,
    CheeseDetailView,
)

pytestmark = pytest.mark.django_db

def test_good_cheese_list_view_expanded(rf):
    url = reverse('cheeses:list')

    request = rf.get(url)

    callable_obj = CheeseListView.as_view()

    response = callable_obj(request)

    assertContains(response, 'Cheese List')

def test_good_cheese_list_view(rf):
    # Get the request
    request = rf.get(reverse("cheeses:list"))
    # Use the request to get the response
    response = CheeseListView.as_view()(request)
    # Test that the response is valid 
    assertContains(response, 'Cheese List') 

def test_good_cheese_detail_view(rf):
    # Order some cheese from the CheeseFactory
    cheese = CheeseFactory()
    # Make a request for our new cheese
    url = reverse("cheeses:detail", kwargs={'slug': cheese.slug}) 
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    # Test that the response is valid 
    assertContains(response, cheese.name)