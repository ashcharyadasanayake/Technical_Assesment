from django.shortcuts import render


from myapp.models import student_1, student_2,student_3,student_4,student_5,student_6

def table1_view(request):
    table1_data = student_1.objects.all()
    return render(request, 'table1.html', {'table1_data': table1_data})

def table2_view(request):
    table2_data = student_2.objects.all()
    return render(request, 'table2.html', {'table2_data': table2_data})

def table3_view(request):
    table3_data = student_3.objects.all()
    return render(request, 'table3.html', {'table3_data': table3_data})

def table4_view(request):
    table4_data = student_4.objects.all()
    return render(request, 'table4.html', {'table4_data': table4_data})

def table5_view(request):
    table5_data = student_5.objects.all()
    return render(request, 'table5.html', {'table5_data': table5_data})

def table6_view(request):
    table6_data = student_5.objects.all()
    return render(request, 'table6.html', {'table6_data': table6_data})

def all_tables_view(request):
    table1_data = student_1.objects.all()
    table2_data = student_2.objects.all()
    table3_data = student_3.objects.all()
    table4_data = student_4.objects.all()
    table5_data = student_5.objects.all()
    table6_data = student_6.objects.all()
  

    return render(request, 'all_tables.html', {'table1_data': table1_data, 'table2_data': table2_data , 'table3_data': table3_data,'table4_data':table4_data,'table5_data':table5_data,'table6_data':table6_data})