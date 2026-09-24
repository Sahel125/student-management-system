
class StudentNode:
    """A node in the Binary Search Tree (BST)"""
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.left = None
        self.right = None