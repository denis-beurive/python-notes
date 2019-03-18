# URL manipulation

Use the package "`urllib`".

[This example](code/url.py) illustrates the use of the package previously mentioned.

Result:

    https://en.wikipedia.org:8080/wiki/Internet?index=0&view=no#Terminology

    URL components:

    * Scheme:   https
    * Netloc:   en.wikipedia.org:8080
    * Hostname: en.wikipedia.org
    * Port:     8080
    * Path:     /wiki/Internet
    * Params:   
    * Fragment: Terminology
    * Username: None
    * Password: None
    * Query:    index=0&view=no

    Query parameters:

    * index: 0
    * view: no

    https://en.wikipedia.org:8080/wiki/Internet?p1=10&p2=this+is+a+param#Terminology

