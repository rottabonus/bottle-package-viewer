# bottle-package-viewer

_On a Debian and Ubuntu systems, there is a file called /var/lib/dpkg/status that holds information about software packages that the system knows about. 
This is a program that exposes some key information about packages in the file via an HTML interface._

Application is made with [bottle framework](https://bottlepy.org/docs/dev/index.html) and is served by a [waitress WSGI server](https://docs.pylonsproject.org/projects/waitress/en/stable/).

Hosted to [http://104.248.35.146/](http://104.248.35.146/)

If you want to install and try this on your own machine, clone the repo

```
$ git clone https://github.com/rottabonus/bottle-package-viewer.git
```

Then go to repository and create virtual env

```
$ cd bottle-package-viewer
$ mkdir venv
$ virtualenv --no-site-packages venv
```

Now you can activate virtual environment

```
$ source venv/bin/activate
```
Or if you're using Windows, in project dir create and activate environment with

```
$ virtualenv venv
$ drive:\Users\'Username'\bottle-package-viewer\venv\Scripts\activate.bat
```


(also remember to deactivate later, just type `deactivate`)

Now you have to install two dependencies

```
$ pip install bottle
$ pip install waitress
```

And run program

```
$ python app.py
```
