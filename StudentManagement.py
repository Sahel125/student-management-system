
from Student import StudentNode
from Stack import Stack

class StudentBST:
    """Binary Search Tree for Student Records"""
    def __init__(self):
        self.root = None

    def insert(self, student_id, name, marks):
        """Insert a student record into the tree """
        new_node = StudentNode(student_id, name, marks)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if student_id < current.student_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, student_id):
        """Search for a student by ID"""
        current = self.root
        while current:
            if current.student_id == student_id:
                return current
            elif student_id < current.student_id:
                current = current.left
            else:
                current = current.right
        return None  # Student not found
    
    def search_by_id(self, student_id):
        
        if not self.root:
            return None

        stack = [self.root]

        while stack:
            node = stack.pop()
            if node.student_id == student_id:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return None  # Not found

  
    
    def locate_student(self, student_id):
        """Searches for a student by performing traversal."""
        return self._search_student(self.root, student_id)

    def _search_student(self, node, student_id):
        """Performs traversal to find the student."""
        if node is None:
            return None  # Not found
    
        if node.student_id == student_id:
            return node  # Found the student
    
        left_result = self._search_student(node.left, student_id)
        if left_result:
            return left_result
    
        return self._search_student(node.right, student_id)  # Continue in right subtree
    
    def _collect_students(self, node, students):
        """Helper function to collect students into a list."""
        if node:
            students.append(node)  # Store node in list
            self._collect_students(node.left, students)
            self._collect_students(node.right, students)
    
    def display_sorted(self):
        """Sorts student records using a simple Bubble Sort approach and displays them."""
        students = []
        self._collect_students(self.root, students)  # Collect student records into a list
        
        # Bubble Sort - inefficient sorting
        n = len(students)
        for i in range(n):
            for j in range(0, n-i-1):
                if students[j].student_id > students[j+1].student_id:
                    students[j], students[j+1] = students[j+1], students[j]  # Swap
        
        # Display sorted students
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, marks: {student.marks}")
            
            
     # Student needs to complete these ( Refer to the Assessment Section A1.1 - A1.3)
     # TODO - A.1.1: define search_by_name method and/or any related helper methods
    def search_by_name(self, name):
        all_names = []
        
        def inorder_search(node):
            if node is None:
                return
            inorder_search(node.left)
            if node.name.lower() == name.lower():
                all_names.append(node)
            inorder_search(node.right)
            
        inorder_search(self.root)
        return all_names
        
        # search through the tree and get all those macting the criteria 
        
        return all_names
     
        
    
     # TODO - A.1.2: define total_student_count  method and/or any related helper methods
    def total_student_count(self):        
        def count_recursive(node):
            if node is None:
                return 0
            return 1 + count_recursive(node.left) + count_recursive(node.right)
        
        return count_recursive(self.root)
        # traverse tree
        # update count every time you visit a node   
        
    
    # TODO - A.1.3: define display_ordered  method and/or any related helper methods
    def display_ordered(self):
        
        def inorder_display(node):
            if node is None:
                return 
            inorder_display(node.left)
            print(f"ID: {node.student_id}, Name: {node.name}, Marks: {node.marks}")
            inorder_display(node.right)
            
        inorder_display(self.root)
       # option -1 already displays data in ordered ( ordered by Id)
       # you need to do the same , however, you need to employ  efficient sorting technique
       
        
   # TODO  A.1.4 : Complete this method to count the total number of nodes in the BST
   # This uses iterative approach and makes of of provided stack ( refer to stack.py)
    def total_student_count_iter(self):
        if not self.root:
            return 0
    
        count = 0
        stack = Stack()
        stack.push(self.root)
        
        while stack.is_not_empty():
            node = stack.pop()
            count += 1
            
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
                
        return count
        
        condition = True
        while condition:
            pass
        
        
        return count
       
   # TODO A.1.5: Method to update student record
    def update_student_record(self, student_id):
       # TODO : Use provided methods to check if student with given student_id exists
       student = self.search(student_id)
       
       if student is None:
           print("Student not found")
           return
       
       print(f"Found student: ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")
       
       while True:
           print("\nWhat would you like to update?")
           print("1. Update Name")
           print("2. Update Marks")
           print("3. Update GPA")
           print("4. Update All (Name, Marks, and GPA)")
           print("5. Exit update menu")
           
           try:
               choice = int(input("Enter your choice (1-5): "))
           except ValueError:
               print("Invalid input. Please enter a number. ")
               continue
           
           if choice == 1:
               new_name = input("Enter new name: ").strip()
               if new_name:
                   student.name = new_name
                   print(f"Name updated successfully to: {student.name}")
               else: 
                   print("Name cannot be empty. Update cancelled.")
                   
           elif choice == 2:
              try: 
                  new_marks = float(input("Enter new marks: "))
                  student.marks = new_marks
                  print(f"Marks successfully updated to {student.marks}")
              except ValueError:
                  print("Invalid marks. Please enter a number.")
            
           elif choice == 3:
                try:
                    new_gpa = float(input("Enter new GPA: "))
                    student.gpa = new_gpa
                    print(f"GPA updated successfully to {student.gpa}")
                except ValueError:
                    print("Invalid GPA. Please Enter a number. ")
                    
           elif choice == 4:
               new_name = input("Enter new name: ").strip()
               if new_name:
                   student.name = new_name
                   
               try:
                   new_marks = float(input("Enter new marks: "))
                   student.marks = new_marks
               except ValueError:
                   print("Invalid marks. Keeping existing marks. ")
                   
               try:
                   new_gpa = float(input("Enter new GPA: "))
                   student.gpa = new_gpa
               except ValueError:
                   print("Invalid GPA. Keeping existing GPA")
                   
               print("Update completed!")
               
           elif choice == 5:
               print("Exiting update menu.")
               break
           
           else:
               print("Invalid choice. Please enter 1-5.")
       # If the student exists, prompt the user to  enter options 1 -> To update Name , 2 -> update marks.
       # .. update the record based on user choice
       
   
       
       
           



