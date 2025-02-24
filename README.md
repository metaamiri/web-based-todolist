# Django To-Do List Metodo
A simple To-Do List web application built with Django, HTML, CSS, and JavaScript. The application allows users to add tasks, mark them as finished, and move them between "Open" and "Finished" lists dynamically using JavaScript and Fetch API.

## Features
- Add new tasks
- Mark tasks as finished
- Move tasks between "Open" and "Finished" lists
- Persistent task storage using Django's session
- Dynamic UI updates with JavaScript and Fetch API

## Installation

Clone the repository:
```
git clone https://github.com/metaamiri/web-based-todolist.git
```
Go to project directory and install requirements:
```
pip install -r requirements.txt
```
Run migrations :
```
python manage.py migrate
```
## Run
Run the below command in the project directory to run The server:
```
python manage.py runserver
```
Open the browser and go to http://127.0.0.1:8000/

## API Communication
- The frontend communicates with the backend using Fetch API.
- When a task is marked as finished, a POST request updates the session storage.
- Data is stored and retrieved dynamically without page reloads.

## Screenshots
![Screenshot of output.](https://github.com/metaamiri/nowruz-counter/blob/main/main/Templates/screenshot/Screenshot.png)
