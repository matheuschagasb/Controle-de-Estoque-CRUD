# Inventory Control CRUD

This project is a simple inventory control system with product registration, update, listing, and deletion operations, implemented in Python.  
Product data is stored in a MySQL database, and the system uses an in-memory agenda for fast operations during execution.

## Setup

It is recommended to use a Python virtual environment to manage dependencies.  
To create and activate a virtual environment, run:

```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

Then, install the required dependencies:

```
pip install -r requirements.txt
```

## Configuration
Create a .env file in the project root with your database connection details, for example:

DB_HOST=localhost
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=inventory_control

## Usage

To run the program, use:

```
python app/main.py
```

The main menu allows you to:

- Add Product
- Update Product
- List Products
- Delete Product
- Exit Program
During execution, data is kept in memory and synchronized with the database.
When the program ends, the products table is automatically cleared.

## Notes
- This project is for educational purposes and does not handle all edge cases or large datasets.
- The code is organized into modules for easier maintenance and understanding.
- To run on other operating systems, ensure Python and MySQL are properly installed and configured.
