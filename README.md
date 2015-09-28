The KSC Main Site
===============

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
> - Flask micro web framework - Install using ``` sudo pip install Flask ```
> - uWSGI for Python - Install using ``` sudo pip install uWSGI ```
> - NGINX - Install in OSX using ``` brew install nginx ``` and in Linux systems using ``` sudo apt-get install nginx ```. Again Windows sucks isn't it??
> - node.js - Install in OSX using ``` brew install nodejs ``` and in Linux as ``` sudo apt-get install nodejs ```
> - coffeescript - install using ``` sudo npm install -g coffee-script```

Running
----------
> - Clone this repo using ``` git clone https://github.com/knowledge-sharing-campaign/site ```
> - While inside the folder 'site',  run (will use 7070 port by default)
    - ``` sudo ./ksc -start ``` for production mode
    - ``` sudo ./ksc -start -dev``` for development mode
    - ``` sudo ./ksc -stop ``` to stop the servers
    - ``` sudo ./ksc -restart ``` to restart all servers
    - ``` sudo ./ksc -start --port xxxx ``` to run on xxxx port

Developing
--------------
> - All python code and HTML templates should be written in app/app_core
> - All static content should be put in app/static folder. Referenced as /static/content... from HTML, CSS files.


-- The KSC Team
