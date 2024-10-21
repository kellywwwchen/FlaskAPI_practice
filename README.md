## FlaskAPI_practice

### Create a RESTful server with following RESTful APIs:

- A POST API to create a user with “name” and “age” fields.
- A DELETE API to delete a specific user by “name”.
- A GET API to get a list of users who have been added.
- A POST API to add multiple users from CSV file.
- The CSV file should be uploaded in API request.
- Refer to the attached CSV file: backend_users.csv
- A GET API to calculate average age of each group of users.
- Please use pandas package to calculate  it.
- Group by the first character of the usernames.

### RESTful APIs
- GET /user
- POST /user
- DELETE /user/{name}
- POST /user/upload
- GET /user/average-age

### Folder
    project-folder/
    │-- repositories/              <- Handle data access and communication with the database.
    │   └── user_repository.py
    │
    │-- services/                  <- Contain business logic, coordinating between repositories and views.
    │   └── user_service.py
    │
    │-- views/                     <- Define the endpoints (routes) and handle HTTP requests and responses.
    │   └── user_view.py
    │
    ├── Dockerfile        
    ├── app.py            
    ├── backend_users.csv 
    ├── docker-compose.yml
    ├── requirements.txt  
    ├── swagger.yml       
    ├── test_app.py       
    └── README.md         

### Predrequisites
- Python 3.10
- Flask
- flasgger
- pandas
- Docker (optional)

### Intallation
```
git clone https://github.com/kellywwwchen/FlaskAPI_practice.git
cd FlaskAPI_practice
```
1. Virtualenv：
    ```
    python3 -m venv .venv
    pip install -r requirements.txt
    python app.py
    ```

2. Docker
    ```
    docker-compose up --build
    ```
    
    ```
    docker-compose run python /bin/bash
    pip install -r requirements.txt
    ```

### Running Tests
```
python -m unittest test_app.py
```