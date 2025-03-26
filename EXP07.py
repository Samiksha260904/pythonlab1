import sqlite3

# Establish database connection
connection = sqlite3.connect('./genericDatabase.db')
cursor = connection.cursor()

# Create students table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
connection.commit()

def create_student(name, age):
    """Insert a new student record into the database"""
    cursor.execute('''
        INSERT INTO students (name, age) 
        VALUES (?, ?)
    ''', (name, age))
    connection.commit()
    print(f"Student '{name}' added successfully!")

def read_students():
    """Retrieve and display all student records"""
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    print("\nStudent Records:")
    print("ID | Name      | Age")
    print("---------------------")
    for row in rows:
        print(f"{row[0]:2} | {row[1]:<9} | {row[2]:3}")
    return rows

def update_student_age(student_id, new_age):
    """Update a student's age by ID"""
    cursor.execute('''
        UPDATE students 
        SET age = ? 
        WHERE id = ?
    ''', (new_age, student_id))
    connection.commit()
    print(f"Student ID {student_id}'s age updated to {new_age} successfully!")

def delete_student(student_id):
    """Delete a student record by ID"""
    cursor.execute('''
        DELETE FROM students 
        WHERE id = ?
    ''', (student_id,))
    connection.commit()
    print(f"Student ID {student_id} deleted successfully!")

# Test the functions
if __name__ == "__main__":
    # Create sample students
    create_student("Griffith", 20)
    create_student("Guts", 22)
    
    # Read all students
    read_students()
    
    # Update Griffith's age
    update_student_age(1, 21)
    read_students()
    
    # Delete Guts' record
    delete_student(2)
    read_students()
    
    # Close the connection
    connection.close()