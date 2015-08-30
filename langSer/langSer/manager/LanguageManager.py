import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from Lclassifier import testClassifier
import pickle
import os

classifier_path = 'langSer/manager/classifier.pickle'

@csrf_exempt
def detect (request):
    if request.method == "POST":
        return detectLang (request)
    else:
        return HttpResponse (
            json.dumps({'success': False}), 
            content_type="application/json",
        )

def detectLang (request):
    print "here1"
    text = request.POST.get ('text', '')
    print "here2"
    lang = classifyLang ([text])
    first_val = lang[0]
    return HttpResponse (json.dumps (first_val), content_type="application/json")
    

def setUp():
    f = open(classifier_path)
    classifier = pickle.load(f)
    f.close()
    return classifier
    

global classifier
classifier  = setUp()

def classifyLang (text):
    return testClassifier (classifier[0], text, classifier[1], classifier[2])
