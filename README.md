# Todo-list
Django project for managing todo list


# Installation
Python3 must be already installed

1. Clone the repository:
    ```bash
   git clone git@github.com:jyjuk/Todo-list.git
   cd todolist
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the server:
    ```bash
    python manage.py runserver
    ```
