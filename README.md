
This reposiotry contains a basic solution for the powerplant coding challenge

## Run the app:
 - navigate to the directory where this repository is cloned
 - make a python environment. (explanation can be found here: https://docs.python.org/3/tutorial/venv.html)
 - activate the environment
 - install the requirements that can be found in requirements.txt using the following commmand: pip install -r requirements.txt
 - run the following command to start the application: python .\app.py

The post request should be sent to the following endpoint: [http://127.0.0.1:8888/](http://127.0.0.1:8888/productionplan).
The post request should contain a JSON payload provided in the body following the structured payload example in folder example_payloads.
![image](https://user-images.githubusercontent.com/63374110/214080640-4b1da3a0-00bd-49ac-887f-86f385047ac0.png)

if all previous steps go well, a response body should look like the following:
![image](https://user-images.githubusercontent.com/63374110/214081197-f0129568-3475-4e36-b825-71f1b0e69ef2.png)


Code documentation is provided inside the python files next to the code. However, here is a general overview:
 - app.py contains the code to run the dev. server
 - payload.py: contains the classes used to give a form to the input
 - payload_processor: contains a basic implementation of the algorithms that give the desired response.
 - requirements.txt contains the dependencies needed for the python environement to run the Flask app. 
