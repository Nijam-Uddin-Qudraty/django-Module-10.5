from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    ob = {
    'li' : ['Apple', 'Mango', 'Orange'],
    'o' : [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
    ],
    'number' : [1,2,3,4],
    'birthday' : datetime.datetime.now(),
    'string' : 'Python is fun',
    'str' : '',
    'num': 10,
    'mltstr': """ dog
     cat
      horse
        """,
    }
    return render(request,'home.html',ob)