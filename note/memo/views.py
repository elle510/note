from django.shortcuts import render
from .models import Test

# Create your views here.


from django.http import HttpResponse
from pymongo import MongoClient

# db connection
client = MongoClient()
# client = MongoClient("localhost", 27017)
# client = MongoClient("mongodb://mongodb0.example.net:27017")

# database 얻어오기
# > db          현재 사용중인 db
# > show dbs    db 리스트 확인
db = client.test

# 컬렉션 가져오기
coll = db.articles

# cursor = coll.find()
# for document in cursor:
#     print(document)
cursor = coll.find_one({"title": "Hello world"})
# print(cursor['title'])

def index(request):
    return render(request, 'memo/index.html', {'cursor': cursor['title']})
    # return HttpResponse(cursor['title'])#HttpResponse("Hello, world. You're at the memo index.")

def test(request):
    return render(request, 'memo/test.html', {'cursor': cursor['title']})

def postgres(request):
    data = Test.objects.filter(id=1)
    # print(data[0].id)
    return render(request, 'memo/postgres.html', {'data': data[0]})
