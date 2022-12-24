from django.urls import path
from . import views

urlpatterns = [
    path('Addemployee',views.Addemployee,name='Addemployee'),
    path('insertemployee',views.insertemployee,name='insertemployee'),
    path('EmployeeDetails',views.EmployeeDetails,name='EmployeeDetails'),
    path('/update/<int:Id>',views.update,name='update'),
    path('/edit/<int:Id>',views.edit,name='edit'),
    path('/delete/<int:Id>/',views.delete,name='delete')
    
]

