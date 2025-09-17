<<<<<<< HEAD
# Django Student Management System

## Setup

### Using Virtual Environment (venv)

1. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # For Windows use `env\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

### Using Docker

1. Build the Docker image:
    ```bash
    docker build -t student_management_system .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 student_management_system
    ```

3. Access the Django app in your browser at `http://localhost:8000`.

### Important Notes

- Ensure that secrets (e.g., passwords, access tokens) are not committed to the repository.
- Add them to a `.env` file or environment variables, depending on your deployment strategy.

# Django Capstone Project

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv env

2. Activate the virtual environment:

On Windows: env\Scripts\activate
On Mac/Linux: source env/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate
python manage.py runserver

To build the Docker container, follow the steps in the Dockerfile.

## Conclusion
By following these steps, you’ll have a well-structured Django project with login functionality, user registration, proper documentation, and a Git setup that adheres to best practices.
8c03de51721c0726d9adcbd5e76266a815ef1559
