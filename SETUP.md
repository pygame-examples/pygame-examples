
# Setting up a development environment for `pgex`
  - We recommend using a virtual environment with Python to install dependencies in an isolated environment.
  - You need Python `3.7` which is the minimum supported version, to write code to this repository.
  - The first step, is to make a fork of the repository.
  
<img src= "https://media.discordapp.net/attachments/846348147709837352/972533500605526016/unknown.png?width=1398&height=609"/>

  - The next, is to clone your fork to your computer, to do this first install [git](https://git-scm.com/downloads).
  - Alright, now navigate to your fork, and copy its link. Run this command:
  	- `git clone "the link that you copied"` 
  - Now you should have the repository cloned. CD(Change Directory) into it: `cd pygame_examples`
  - Activate a virtual environment, we recommend using `pipenv`:
  	- `pip install pipenv`
  	- `pipenv shell`  Activate a fresh venv
  	- `pipenv install -r requirements.txt` Install the required dependencies 
  	- `pipenv install -r dev-requirements.txt` Install the development dependencies as well, these are extra dependencies required to develop our codebase. 
  	- Now, finally run the `pgex` directory as a module:
  		- `python -m pgex`
  	- There we have it, if all the steps went smoothly, you should now have a proper development environment setup!
  	- Now every time you come into this directory(`pygame_examples`), use `pipenv shell` to activate the venv, and use Python(3.7) as you would usually.
  	
