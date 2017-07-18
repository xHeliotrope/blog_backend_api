from django.views.decorators.csrf import csrf_protect
from django.db import connection 
from django.shortcuts import render
from django.http import HttpResponse
import json

@csrf_protect
def give_ryan(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT row_to_json(rows) FROM (SELECT * from runs) as rows")
            runs = [result[0] for result in cursor.fetchall()]
            runs = [{k:v for k,v in run.items() if k!='id'} for run in runs]
            cursor.execute("SELECT row_to_json(rows) FROM (SELECT * from reads) as rows")
            books = [result[0] for result in cursor.fetchall()]
            books = [{k:v for k,v in book.items() if k!='id'} for book in books]
            
        return HttpResponse(json.dumps({"books": books, "runs": runs}), content_type="application/json")
    else:
        return HttpResponse("gets only please", content_type="text/plain")
