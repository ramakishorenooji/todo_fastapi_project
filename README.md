# tasktracking_fastapi_project
# todo managing project
# FastAPI Template using the Repository Pattern Approach

This project is a backend template for a FastAPI-based application that uses the repository pattern approach to provide an abstraction layer between the business logic and the data access layer. It aims to provide a scalable and maintainable architecture for building web applications.

# Todo FastAPI Application

This is a Todo application built with FastAPI. It allows users to manage their todo items with functionalities to create, read, update, and delete todos. The application also includes user authentication and authorization.

## Features

- User authentication and authorization
- Create, read, update, and delete todos
- Render HTML pages for viewing, adding, and editing todos

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- Jinja2
- Starlette

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:ramakishorenooji/todo_fastapi_project.git
    cd todo-fastapi
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    # Make sure to configure your database settings in the `database.py` file
    python create_db.py
    ```

## Running the Server

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## API Endpoints

### Authentication

- `POST /auth/login`: Login a user
- `POST /auth/register`: Register a new user

### Todos

- `GET /todos/`: Get all todos for the authenticated user
- `GET /todos/todo/{todo_id}`: Get a specific todo by ID
- `POST /todos/todo`: Create a new todo
- `PUT /todos/todo/{todo_id}`: Update an existing todo
- `DELETE /todos/todo/{todo_id}`: Delete a todo

### Pages

- `GET /todos/todo-page`: Render the todo page
- `GET /todos/add-todo-page`: Render the add todo page
- `GET /todos/edit-todo-page/{todo_id}`: Render the edit todo page

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


![Screenshot 2025-03-22 123454](https://github.com/user-attachments/assets/c1bbc5e0-8eda-46f5-9150-af06a4ca3b5a)


![Screenshot 2025-03-22 123531](https://github.com/user-attachments/assets/1c0988bb-09ac-46c0-982b-a9d8426622ee)
