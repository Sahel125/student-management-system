from StudentManagement import StudentBST


def insert_sample_students(student_tree):
    """Inserts 12 sample student records into the BST"""
    students = [
        (105, "Alice Johnson", 3.5),
        (102, "Bob Smith", 3.8),
        (110, "Charlie Brown", 2.9),
        (107, "Diana Prince", 3.7),
        (101, "Ethan Hunt", 3.2),
        (115, "Fiona Clark", 3.9),
        (108, "George Miller", 3.1),
        (104, "Hannah Lee", 3.6),
        (112, "Ian Wright", 3.4),
        (109, "Jessica Davis", 3.0),
        (103, "Kyle Johnson", 3.3),
        (106, "Liam Scott", 3.75)
    ]

    
    for student_id, name, marks in students:
        student_tree.insert(student_id, name, marks)
    
    print("12 student records inserted successfully.")

def main():
    bst = StudentBST()
    insert_sample_students(bst)

    while True:
        print("\n===== Student Records Menu =====")
        print("1. Display")
        print("2. Insert Student Record")
        print("3. Search for a Student by ID")
        print("4. Search for Students by Name") 
        print("5. Display Total Student Count - Recursive")
        print("6. Display All Student Records (Sorted by ID)")
        print("7. Display Total Student Count - Iterative")
        print("8. Update student record")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        
        if choice == "1":
            print("==========Display all data=========")
            bst.display_sorted()
            
        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            marks = float(input("Enter marks: "))
            bst.insert(student_id, name, marks)
            print("Student record inserted successfully!")

        elif choice == "3":
            student_id = int(input("Enter Student ID to search: "))
            student = bst.search_by_id(student_id)
            if student:
                print(f"Student Found - ID: {student.student_id}, Name: {student.name}, marks: {student.marks}")
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Enter Student Name to search: ")
            matching_students = []        
            matching_students = bst.search_by_name(name)
            
            
            if matching_students:
                print("Matching Students:")
                for student in matching_students:
                    print(f"ID: {student.student_id}, Name: {student.name}, marks: {student.marks}")
            else:
                print("No students found with that name.")

        elif choice == "5":
            count = bst.total_student_count()
            print(f"Total number of students: {count} - recursive")
            
            
            

        elif choice == "6":
            print("\nStudent Records (Sorted by Id ):")
            bst.display_ordered()
            
            
               
                
        elif choice == "7":
            count = bst.total_student_count_iter()
            print(f"Total number of students: {count} - Iterative")
            
             
            
            
            
        elif choice == "8":
            student_id = int(input("Enter Student ID to update: "))
            bst.update_student_record(student_id)
            print("Update operation completed")
            
            
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break    
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
