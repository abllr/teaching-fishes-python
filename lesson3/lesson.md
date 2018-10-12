## Lesson 3 : Consuming API and Processing Data


### Basics 

An API is a function that can be exposed locally using a library or a module or remotely trough a networking protocol such as RPC or HTTP 
in this lesson we are going to look at HTTP and see how it works , how to use HTTP exposed APIs and how to process that data to a database


### HTTP 

**HTTP** is a stateless protocol i.e doesn't keep a state, an HTTP request or verb lives when it is created till it's completed . HTTP is a client-server
oriented protocol, one entity the client makes requests in a specific vocabulary that we will refer to as a **protocol** , a protocol is a language
agreed upon between computers and that they can understand .

HTTP is composed of 4 main verbs :

* **GET** : fetch data
* **POST** : take this data (client sends data to a server)
* **PUT** : update this data
* **DELETE** : delete this data


HTTP is stateless but supports **sessions**, when you go to a websites you asking the server to give you data in form of **HTML** , **JS** and **CSS** the browser
interprets this data accordingly to create the end result *the webpage* . Once you login the connection between you and the server dies, cookies that store 
**sessions** are added to your request to **authentificate** you, your session cookies are passwords created by the server and given to the client when they first talk 
/ login your session cookies are then used as the key to unlock your data during a session . Once that session expires - something you can spot when you receive
the message *your session has expired, please login again* . - you need to recreate a new session by giving the server your password again so he can give you
fresh cookies , no one likes cookies after two day the become tasteless .

HTTP runs oon the TCP protocol one of the languages computers use to communicate your HTTP request is transfered as bytes over the TCP protcol which defines how
bytes are actually exchanged between computers .

* http://intronetworks.cs.luc.edu/current/ComputerNetworks.pdf

### REST

REST *Representational State Transfer* is an architecture used to build APIs that can be access using the HTTP Protocol messages (GET,POST ...) . 
REST itself is just a language that is used so we can leverage URLs api.example.com/price/BTC-USD and content types ( GIFs, Videos , Data that is consumable (JSON,HTML ...) )
to expose a function so it can be accessed remotely .

* References : 

* https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview


### Requests or HTTP for humans

A smart fella invented what I call the greatest Python library ever [requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) .
Requests is a python library that makes it easy to use HTTP to communicate thus you can use it to communicate with REST APIs remotely .

using requests to fetch an HTML page :

```python

import requests

my_request = requests.get('http://twitter.com')
print(my_request.raw)


```

This will show you the HTML code of twitter.com since HTML is a ressources that was asked for using the *GET* verb . 

**Authentification** 

Requests can be used to make authentified requests to secured endpoints / APIs .

```python

>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'disk_usage': 368627, u'private_gists': 484, ...}

```


You can learn more about requests by checking out their fantastic [docs](http://docs.python-requests.org/en/master/)


### JSON 

JSON is a string based data transfer format that uses dictionnaries (lesson 3 !) to structure data in between computers, JSON is easier to parse and read than 
it's distant cousin XML which under no condition so be allowed to be used or created , BURN IT . 
JSON data inspired the creation *NoSQL* databases that store data in documents instead of the famous TABLES . To be fair SQL or NoSQL doesn't constitute
a big difference in terms of what they do but SQL is deterministic a QUERY will return what it is expected of her . NoSQL can face some inconsisties 
you can use whichever you prefer as JSON is very python-friendly (JSON is basically a python dictionnary) and NoSQL databases use JSON to save and export data
so in this lesson we will stick to NoSQL .

* [MongoDB queries are not deterministic](https://blog.meteor.com/mongodb-queries-dont-always-return-all-matching-documents-654b6594a827)
* [Introducing MongoDB and Python](https://realpython.com/blog/python/introduction-to-mongodb-and-python/)

**PS** : 
* I would have prefered we use SQLite but let's not get to that for a bit let's get crazy .
* Get your hands dirty by finding out more about MongoDB JSON and play with it .




## Consuming REST APIs

### Fetch and Show

By consuming REST APIs we fetch data and process it for information that's the end goal doing this in python is incredibly easy let's start by fetching crypto
prices :

```python

import requests

binance_endpoint = 'https://api.binance.com/'
route = '/api/v1/trades'
parameters = {'symbol':'BTCUSD'}

# Now that we have variables that hold the api route and parameters let's fetch the JSON data that the trades function exposes

request = requests.get(binance_endpoint+route,params=parameters)

json_result = request.json()

# let's print all btc trades higher with a quantity higher than 1

for trade in json_result :
	if float(trade['qty']) > 1 :
		print(trade)


``` 

Gotcha , now that we have a usage template for data fetching remember the data is in a dictionary of strings , you have to convert to float (as values are usually 
floats) to make comparisons sums ... 

* [Binance Docs](https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md)

```

### Fetch and store


TO BE EXPLORED :) 
