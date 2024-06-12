# Accessing Data with MySQL

This guide demonstrates how to access a MySQL database in Python using SQLAlchemy. We will set up a simple database, add a user, and retrieve users from the database.

## Requirements

- Python 3.x
- `SQLAlchemy` library
- `PyMySQL` library
- MySQL database

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Update the `DATABASE_URI` in `app/db_access.py` with your MySQL database credentials:
    ```python
    DATABASE_URI = 'mysql+pymysql://user:password@localhost/test_db'
    ```

3. Ensure your MySQL database is running and accessible.

4. Run the application:
    ```sh
    python run.py
    ```

## Code Explanation

### `app/models.py`

This module defines the database models.

- **`Base`**: The base class for all models.
- **`User`**: A model representing a user with `id`, `name`, and `email` fields.

### `app/db_access.py`

This module contains functions to interact with the database.

- **`setup_database`**: Creates the database and tables.
- **`add_user`**: Adds a new user to the database.
- **`get_users`**: Retrieves all users from the database.

### `run.py`

This script serves as the entry point for the application. It sets up the database, adds a user, and prints all users in the database.

## Additional Information

- Ensure your MySQL credentials and database name are correct in the `DATABASE_URI`.
- You can modify the `add_user` and `get_users` functions to perform more complex database operations.
- SQLAlchemy is a powerful ORM that supports a wide range of database operations and can be extended with custom queries and models.
