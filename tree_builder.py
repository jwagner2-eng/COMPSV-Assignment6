class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

       def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
       def __init__(self):
        self.root = None
    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Error: Add a team lead first.")
            return

        if current_node is None:
            current_node = self.root
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                else:
                    print("Error: Left side is already taken.")

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                else:
                    print("Error: Right side is already taken.")

            else:
                print("Error: Choose left or right.")

            return True

        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("The team directory is empty.")
            return

        print("  " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here

test_tree = TeamTree()
test_tree.root = EmployeeNode("Jordan")

test_tree.insert("Jordan", "Riley", "left")
test_tree.insert("Jordan", "Taylor", "right")
test_tree.insert("Riley", "Morgan", "left")
test_tree.insert("Riley", "Dana", "right")

print("\nTest Team Structure:")
test_tree.print_tree()



# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            if tree.insert(manager, employee, side) is False:
                print(f"Error: Manager '{manager}' was not found.")

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    company_directory()

**Design Memo – Company Directory Tree**

For this assignment, I used a binary tree to organize employees based on who they report to. Every employee is represented by a node that stores their name and has two possible connections, one on the left and one on the right. The first employee is the root of the tree, and everyone else is added underneath an existing manager.

Recursive insertion starts at the top of the tree and checks if the employee it's looking at is the manager we want to add someone under. If it finds the right manager, it checks whether the left or right side is open and adds the new employee there. If it's not the right manager, the program keeps looking through both sides of the tree until it finds them or runs out of places to check.

One thing I had to pay attention to was making sure the program actually checked the whole tree instead of stopping too early or adding someone under the wrong manager. I also had to make sure it wouldn't add an employee to a spot that was already taken. Having the function return a value when it found the manager helped with this because it told the program when it could stop searching.

I think trees make the most sense when you're working with information that has different levels or some kind of chain of command. A company is a good example because employees report to managers, who might report to other managers. Computer folders and websites are other examples. Compared to using a regular list, a tree makes it easier to see how everything connects. The downside is that finding one specific person can still take some time if the program has to search through most of the tree.
