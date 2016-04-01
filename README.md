# Boring Man Clan
A competitive Boring Man website

## Contributing

This website is a Django app and is developed on Linux and hosted on Github. If you would like to contribute to the website and work on it on your own computer there are a few steps you will need to take.

### Getting setup on Windows (or Mac... the steps are basically the same)

To work on the website there are a few tools you will need to install:  

You will need to install Docker toolbox to run the website on your own computer.  
[Download Docker Toolbox Here](https://www.docker.com/products/docker-toolbox)

If you aren't a Git expert you might want to install Github Desktop to download the source code for the website.  
[Download Github Desktop Here](https://desktop.github.com/)

If you don't already have a text editor you will need to download one in order to edit the source code.  A good one to get started with is Atom.  
[Download Atom Text Editor Here](https://atom.io/)

### Getting setup on Linux
Clone repo. Install docker. Run develop.sh. Goto localhost in your browser.

### Downloading the website source code and running the website on your computer

Now that you have all the tools, you need to get the source code to start working on the website. To get started you need to open up "Docker Quickstart Terminal", its part of the Docker Toolbox you installed. It will look something like this:  

![Docker Quickstart Terminal](https://docs.docker.com/windows/images/b2d_shell.png)

After you have the terminal open type (to copy/paste just right click the mouse in the terminal):
```
git clone https://github.com/aldencolerain/boringmanclan.git
```

Now go into the boringmanclan folder:
```
cd boringmanclan
```

Create a secrets.py file:
```
echo "import os
os.environ['ENVIRONMENT'] = 'development'
os.environ['API_SECRET'] = 'Thisisaninsecuresecret'
os.environ['DJANGO_SECRET_KEY'] = 'Thisisanotherinsecuresecret'
" >> project/secrets.py
```

Your almost done! Find your Docker Machine's IP address by typing (write it down somewhere):
```
docker-machine ip
```

Run the website server (This will take a while on your first run if you have a slow internet connection/computer):
```
bash development.sh
```

Thats it. If everything worked you should have something like this showing in your terminal.  If you don't, leave a comment here describing what happened and I will do my best to help. This does require some amount of expertise, if its not a quick fix I might have to refer you to the Docker/Git/Django docs.
```
Django version 1.9, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

Now you should be able to visit the boringmanclan development website on your own computer by typing the Docker Machine IP you wrote down earlier in your web browser.  It will be something like this:
```
192.168.99.100
```
You can login using the default "root" who's password is also "root"  

**If that pulls up... congratulations! Your ready to roll.**  

To stop the server press *Ctrl-C*.  To start it again type ``python manage.py runserver``. To exit the Docker container press *Ctrl-D*. To open it up again type ``bash develop.sh``. If all else fails you can always just close the terminal window, re-open it, and navigate back to the boringmanclan folder.


### Editing the project

Want to change the way the website looks?  Start messing around in project/templates and project/static/css directories.

### Saving and contributing your changes

To save your changes you need to make a git **commit** using the terminal or open up the Github Desktop app. This will record your changes to the project. For directions on how to make a commit, [read this paragraph](https://guides.github.com/activities/hello-world/#commit).

After you have committed your changes, you need to make a **pull request**. A pull request lets me know you made changes and I can take those changes and pull them into the project and put them on the website. To learn how to make a pull request [read this](https://guides.github.com/activities/hello-world/#pr).  When you have done that let me know!  I'll review it and when its ready, your changes will be incorporated into the website.
