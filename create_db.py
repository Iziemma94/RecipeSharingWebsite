import sqlite3

# Function to create the database and tables
def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()


    # Define SQL statements for table creation
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username VARCHAR UNIQUE,
        Email VARCHAR UNIQUE,
        Password VARCHAR
    );
    """

    create_recipes_table = """
    CREATE TABLE IF NOT EXISTS recipes (
        RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT,
        Ingredients TEXT,
        Instructions TEXT,
        AuthorID INTEGER,
        FOREIGN KEY (AuthorID) REFERENCES users (UserID)
    );
    """

     # Execute SQL statements to create tables
     cursor.execute(create_users_table)
     cursor.execute(create_recipes_table)

      # Commit changes and close connection
      connection.commit()
      connection.close()


# Call the function to create the database
if __name__ == "__main__":
    create_database()
