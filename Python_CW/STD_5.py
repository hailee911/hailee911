class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval  # The data value stored
        self.nextval = None  # Next node in the linked list.


class SLinkedList:
    def __init__(self):
        self.headval = None  # Start(head) of the linked list.

    def listprint(self):
        printval = self.headval
        while printval is not None:  # While nodes in the linked list to traverse
            print(printval.dataval)  # Print the data value.
            printval = printval.nextval  # Put the next node to print.

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)  # Create a new node with the given node data.

    def AtEnd(self, newdata):
        NewNode = Node(newdata)  # Create a new node with the given node data.
        if self.headval is None:  # If the linked list is empty
            self.headval = NewNode  # Set the new node as the head value.
            return
        last = self.headval
        while (last.nextval):  # Traverse through the list to find the last node.
            last = last.nextval
        last.nextval = NewNode  # Put the next value of the last node to the new node.

    def Insert(self, val_before, newdata):
        if val_before is None: # if there are no new node data to insert after
            print("No node to insert after")
            return
        else:
            new_node = Node(newdata)  # Create a new node with the given node data.
            new_node.nextval = val_before.nextval  # Put the next new node to the next value (given node).
            val_before.nextval = new_node  # Put the next value (given node) to the new node.


# Create a new linked list
list = SLinkedList()

# Set the head of the linked list
list.headval = Node("Mon")

# Create new nodes and link them to the head
e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

# Add a new node at the end of the linked list
list.AtEnd("Sun")

# Insert a new node after the second node
list.Insert(e2, "Wed")

# Print the linked list
list.listprint()
