from django.test import TestCase
from restaurant.models import Menu

# Para testear una view
from restaurant.views import MenuItemView
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

# class BookingTest(TestCase):
#     def setup(self):
#         Booking.objects.create(name="Susana", numberOfGuest=2,bookingDate="2023-08-15T18:00:00Z")  
#     def test_get_booking(self):
#         book = Booking.objects.get(name="Susana")
#         self.assertEqual(str(book), 'name : Susana')
       
class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Helado", price=80, inventory=100)
        
    def test_get_item(self):
        item = Menu.objects.get(title="Helado")
        self.assertEqual (item.inventory, 100)
        self.assertEqual(item.price, 80)
        self.assertEqual(item.title,"Helado")
        self.assertEqual(str(item), "Helado : 80.00")
        
    def test_get_items(self) :
        items= Menu.objects.all()  
        self.assertEqual(len(items), 1) 
        
# Testeo de un view    
cliente = APIClient()
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Helado", price=80, inventory=100) 
    def test_getall(self):
        respuesta = cliente.get(reverse('menu_view'))
        self.assertEqual(len(respuesta.data),1)
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        
        


