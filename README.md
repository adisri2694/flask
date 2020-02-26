**PROBLEM STATEMENT:**

Build a word counter web application. The application should accept words and keep a count of how many times it has seen the word. You should be able to query the application for the count of a particular word. You should also be able to delete words from the application.

**SOLUTION** :

A flask api using an in-memory data structure (dictionary) to store the count of words. The api has custom error messages for error codes 404 ( wrong URL) and 405 ( wrong HTTP methods) which according to me will be the most probable errors if any.

[github link to repository](https://github.com/adisri2694/flask)

**ENVIRONMENT SETUP FOR UBUNTU :**

- Before you start, make sure you have python3.6 installed and, if not follow:

$ sudo add-apt-repository ppa:jonathonf/python-3.6

$ sudo apt-get update

$ sudo apt-get install python3.6

- After that create virtual environment with \*Python3.6\* and activate it

 Install virtual environment :

$ sudo apt-get install python-virtualenv

Install pip  so that we can install further packages using pip :

$ sudo apt-get install python-pip

Make new environment :

$ virtualenv --python=python3.6 flask-env

Activate environment :

$ source flask-env/bin/activate

- Install flask using pip :

 $ Pip install flask

- Install postman using snap package or download from ubuntu software centre

$ sudo snap install postman



**STEPS TO RUN THE SERVER:**

- Clone the  repository :

$ git clone [https://github.com/adisri2694/flask.git](https://github.com/adisri2694/flask.git)   in terminal or download the zip file.

- Save flask1.py file to any location and open terminal  in that location.
- Activate your virtual environment :

 $ source flask-env/bin/activate

- Run flask1.py file :

 $ python flask1.py

 Server will start running on port 3000, output on flask

- Server is running now, copying the URL which will be used as an endpoint for postman tool.

**STEPS TO RUN POSTMAN AND GET RESPONSE FROM THE SERVER :**

- Open Postman tool and click on NEW ---> Request. Write a request name and click on &quot;Save to flask&quot;.

- Choose HTTP methods depending upon the interaction you demand.

**POST** - /word/\&lt;word\&gt; : Adds a word if not present. If the word is already present, increase the count by one.

**GET** - /word/\&lt;word\&gt; : Returns the count of the word.

**DELETE** - /word/\&lt;word\&gt; : Deletes the word.

- Enter request URL :    [http://127.0.0.1:3000/word/](http://127.0.0.1:3000/word/)<word>  and click on &quot;send&quot;.
- Response of the api will come in the &quot;body&quot;.

- Below is a link of Collection named &quot; **flask**&quot;. This contains 5 flask requests showcasing all the above interactions with the server.

[https://www.getpostman.com/collections/26b06b0d3cb8fa4b5b73](https://www.getpostman.com/collections/26b06b0d3cb8fa4b5b73)

Open postman → Import → Import from link

Paste the above link and import the collection and run the requests.
