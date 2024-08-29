# About the project
This project is a TODO-like application designed to help users organize and prioritize their daily activities. It was developed by NicolasFloresF and Eduardo-Leal-Carvalho during their computer science graduation course.

## Installation

To get started and install the application, follow the steps below.

### Prerequisites

Before running the project, make sure you have the following prerequisites installed on your machine:

- MySQL
- Python 3
- Poetry

### Setting up the project

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/NicolasFloresF/project_todo.git
    ```

2. Setting up MySQL:

    - Start your SQL server

      ```bash
      mysql -u yourMysqlUsername -p
      ```

    - Create a new database in your local MySQL server.
    - Import the SQL file named `Just_TODO_it.sql` into the newly created database.

      ```
      CREATE database yourDatabaseName;
      USE yourDatabaseName;
      SOURCE pathToSQLFile;
      ```

3. Setting up .env:

    - Create a file named `.env` in project_todo folder.
    - Add the following information to the `.env` file:

      ```
      USER_NAME=yourMysqlUsername
      PASSWORD=yourPassword
      HOST=yourHost
      DATABASE=yourDatabaseName
      ```

4. Poetry setup:

    - Run the following commands to install dependencies and start the virtual environment:

      ```bash
      poetry install
      poetry shell
      ```

### Executing the code

To execute the code, run the following command (in your poetry virtual environment):

```bash
python3 -B -m project_todo
```

That's it! You're now ready to start using the Project Todo application.

