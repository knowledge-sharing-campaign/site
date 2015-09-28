The KSC Main Site
===============

[![Join the chat at https://gitter.im/knowledge-sharing-campaign/site](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/knowledge-sharing-campaign/site?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is the repo for the code for the main knowledge sharing campaign website at http://knowledgesharingcampaign.org

The backend has been designed for high scalability and performance for a large number of concurrent users and heavy loads.

Tech Stack
-------------
> - HTML 5
> - CSS 3
> - CoffeeScript / Javascript
> - Python 2.7.x / PyPy
> - The Flask micro web framework
> - uWSGI in threaded multi python interpreter mode
> - NGINX for static content delivery and public facing networking via unix sockets


Development requirements
--------------------------------
> - *Nix Systems like any Linux or OSX system. Windows can't run this as this is poetic code and windows is sadly prosaic.
> - Python 2.7.x / PyPy which is most probably installed in your system. Windows sucks isn't it??
> - pip - Install using ``` sudo easy_install pip ```
> - NGINX - Install in OSX using ``` brew install nginx ``` and in Linux systems using ``` sudo apt-get install nginx ```. Again Windows sucks isn't it??
> - node.js - Install in OSX using ``` brew install nodejs ``` and in Linux as ``` sudo apt-get install nodejs ```
> - coffeescript - install using ``` sudo npm install -g coffee-script```

Running
----------
> - Clone this repo using ``` git clone https://github.com/knowledge-sharing-campaign/site ```
> - Go inside the site folder using ``` cd site ```
> - run ``` sudo pip install -U -r requirements.txt ```
> - run the following commands (will use *7070* port by default)
    - *For production mode*
        - ``` sudo ./ksc -start ```
        - ``` sudo ./ksc -stop ```
        - ``` sudo ./ksc -restart ```
    - *For development mode*
        - ``` sudo ./ksc -start -dev```
        - ``` sudo ./ksc -stop -dev```
        - ``` sudo ./ksc -restart -dev```
    - ``` sudo ./ksc -start --port xxxx ``` to run on xxxx port

Developing
--------------
> - All python code and HTML templates should be written in app/app_core
> - All static content should be put in app/static folder. Referenced as /static/content... from HTML, CSS files.


-- The KSC Team
