from django.urls import path
from myapp.views import table1_view, table2_view,table3_view,table4_view,table5_view,table6_view, all_tables_view

urlpatterns = [
    path('table1/', table1_view, name='table1'),
    path('table2/', table2_view, name='table2'),
    path('table3/', table3_view, name='table3'),
    path('table4/', table4_view, name='table4'),
    path('table5/', table5_view, name='table5'),
    path('table6/', table6_view, name='table6'),
    path('alltable/',all_tables_view, name='alltable'),
    
    
]