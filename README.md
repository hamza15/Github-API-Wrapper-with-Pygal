# Github-API-Wrapper-with-Pygal
A python API wrapper that pulls user's repos and plots the stars acquired for each repo using pygal.

## Dependencies:

- Must have python installed.
- We need the 'requests' module to request information from a website and examine the response. To download run the following:

	pip install --user requests
	
- To produce vector graphic files we will use Python's visualization package Pygal. Run the following command to install:
	
	pip intsall --user pygal
	
## Steps:

- Clone the project to a local repo.
- Open terminal and navigate to the repository you cloned the project to.
- If you would like to cutomize the wrapper to plot your repos, edit the 'github_wrapper.py' file and replace the url.
- Edit the following line and replace 'hamza15' with your username:

        url = 'https://api.github.com/users/hamza15/repos?q=language:python&sort=stars'
	
- To execute, open terminal and navigate to the directory you cloned this repo to and run with the following command :
	
        python github_wrapper.py

- Running the script will create a file github_wrapper.svg in your current directory.
- Open the python_repos.svg with chrome or any other browser available.

![screen shot 2018-08-29 at 11 33 40 pm](https://user-images.githubusercontent.com/5506327/44828036-0899f200-abe4-11e8-8cf4-600e13c51d6d.png)
