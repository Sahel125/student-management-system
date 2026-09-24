class StudentGraph:
    def __init__(self):
        self.graph = {}  

    def add_student(self, student_id):
        """Add a student node to the graph."""
        if student_id not in self.graph:
            self.graph[student_id] = []

    def add_friendship(self, student1, student2):
        """Create an undirected edge (friendship) between two students."""
        if student1 not in self.graph:
            self.add_student(student1)
        if student2 not in self.graph:
            self.add_student(student2)

        self.graph[student1].append(student2)
        self.graph[student2].append(student1)

    def display_friends(self, student_id):
        """Print friends of a given student."""
        if student_id in self.graph:
            print(f"Friends of Student {student_id}: {self.graph[student_id]}")
        else:
            print(f"Student {student_id} not found!")

    def display_graph(self):
        """Print the full adjacency list."""
        for student, friends in self.graph.items():
            print(f"Student {student}: Friends -> {friends}")
            
            
            
