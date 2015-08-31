# Language-Detection
A simple python server which can detect language based on text

The server is a Django server which can be started by running : 

```
        python manage.py runserver
```
if there are unapplied migrations we can redo the migrations by running

```
        python manage.py migrate
```

from the project root directory. 

The classifier is simple multinomial naive bayes classifier trained on character n-grams we take n-grams from the range 3-6 on sentences and limit our features to 15000 most frequent TfIDF features. By doing a 60-40 training test split we found the accuracy to be over 0.9999. 

The server accepts post requests (by default) at http://localhost:8000/lang_id/ endpoint with "text" as post parameter. The text parameter contains the string to be identified in unicode format. 

The return values are tuples in from of language, probability as calculated by the classifier. 

The folder contains a self contained testing file which assumes that host_url is http://localhost:8000/lang_id/
which can be changed in the file and tests it against a bunch of different variantions of 'this be a test'

The classifier is currently trained on the European Parliament NLTK sample corpus which has 11 languages

1. Danish
2. Dutch
3. English
4. Finnish
5. French
6. German
7. Greek
8. Italian
9. Portugese
10. Spanish
11. Swedish


When the server starts it loads a pretrained classifier in the memory whose path is mentioned in manager/LanguageManager.py

## Post Spec

The server accepts post requests on /lang_id/ endpoint.

params (Post) : {"text": "The language you want to test"}

return ["top_language": probablity of it]


###Extensions

If you want to add a new language to the classifier copy the language in the  europarl_raw folder in the form 'language/text_files' and run refesh.py to retrain the classifier. 


### Python modules used
The project has some dependency on the following python modules

1. Requests : For sending post requests. 
2. Django Framework: To run the webserver
3. pickle : For saving the classifier
4. json : for sending post request back
5. nltk: tokenization, and courpus reader
6. numpy and scipy: for sparse matrix manipulations
7. sklearn: for learning and feature extraction and testing
