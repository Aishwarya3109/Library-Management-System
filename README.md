# Library Management System

## Overview
The Library Management System is a Python-based application designed to facilitate the management of book records in a library. It utilizes a MySQL database to store and retrieve information about books, authors, and other related data.

## Features
- **Add New Book Records**: Easily insert new books into the database.
- **Display Book Records**: View all available books with detailed information.
- **Search Books**: Search for books by their unique book number.
- **Update Book Records**: Modify existing book details as needed.
- **Delete Book Records**: Remove books from the database with confirmation.

## Technologies Used
- **Python**: The programming language used for building the application.
- **MySQL**: The database management system for storing book records.
- **MySQL Connector**: A library for connecting Python to MySQL for executing SQL queries.

## Setup and Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install MySQL**: Ensure MySQL Server is installed and running on your machine.

3. **Install required Python packages**:
   ```bash
   pip install mysql-connector-python
   ```

4. **Configure the Database**:
   - Create a database named `LIBRARY`.
   - Run the SQL script provided in the repository to set up the necessary tables.

5. **Run the Application**:
   ```bash
   python project.py
   ```

## Usage
Upon running the application, you will be presented with a menu to select various operations related to book management. Follow the prompts to add, view, search, update, or delete book records.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or suggestions.
