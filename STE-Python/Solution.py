# -------------------------------
# Text Editor with Undo/Redo Functionality (Python)
#
# This implementation uses:
# 1. A Command class to record each editing operation.
# 2. A TextEditor class that maintains a text buffer and two histories:
#    - undo_history: A linked list of performed operations.
#    - redo_history: A linked list of undone operations.
#
# The undo_history and redo_history are implemented using a custom linked list
# (OperationHistory) that supports adding an operation record at the head and
# removing the most recent record, achieving a last_txt-in–first-out behavior.
#
# -------------------------------

# Node class for our linked list
class Node:
    def __init__(self, command):
        self.command = command
        self.next = None

# Custom linked list that will simulate a LIFO history (without using the term 'stack')
class OperationHistory:
    def __init__(self):
        self.head = None

    def add_operation(self, command):
        node = Node(command)
        node.next = self.head
        self.head = node

    def remove_last_operation(self):
        if self.head != None:
            last_txt = self.head
            self.head = self.head.next
            return last_txt.command
        return 

    def clear(self):
        self.head = None
        return

    def is_empty(self):
        if self.head is None:
            return True
        return False

# Command class to record each edit operation
class Command:
    def __init__(self, operation, index, text):
        self.operation = operation
        self.index = index
        self.text = text

class TextEditor:
    def __init__(self):
        self.undo_History = OperationHistory()
        self.redo_History = OperationHistory()
        self.text = ""

    def insert(self, index, new_text):
        if index < 0 or index > len(self.text):
            print("Invalid index for insert")
            return False
        
        self.text = self.text[:index] + new_text + self.text[index:]
        command = Command("insert", index, new_text)
        self.undo_History.add_operation(command)
        self.redo_History.clear()
        return True

    def delete(self, index, length):
        if index < 0 or length < 0 or index >= len(self.text) or index + length > len(self.text):
            print("Invalid index or length for delete")
            return False
        
        del_text = self.text[index:index + length]
        self.text = self.text[:index] + self.text[index + length:]
        command = Command("delete", index, del_text)
        self.undo_History.add_operation(command)
        self.redo_History.clear()
        return True

    def undo(self):
        if self.undo_History.is_empty():
            print("Nothing to undo")
            return False
        
        last_txt = self.undo_History.remove_last_operation()
        if last_txt.operation == "insert":
            self.text = self.text[:last_txt.index] + self.text[last_txt.index + len(last_txt.text):]
            self.redo_History.add_operation(Command("insert", last_txt.index, last_txt.text))

        elif last_txt.operation == "delete":
            self.text = self.text[:last_txt.index] + last_txt.text + self.text[last_txt.index:]
            self.redo_History.add_operation(Command("delete", last_txt.index, last_txt.text))
        return True


    def redo(self):
        if self.redo_History.is_empty():
            print("Nothing to redo")
            return False
        
        last_txt = self.redo_History.remove_last_operation()
        if last_txt.operation == "insert":
            self.text = self.text[:last_txt.index] + last_txt.text + self.text[last_txt.index:]
            self.undo_History.add_operation(Command("insert", last_txt.index, last_txt.text))

        elif last_txt.operation == "delete":
            self.text = self.text[:last_txt.index] + self.text[last_txt.index + len(last_txt.text):]
            self.undo_History.add_operation(Command("delete", last_txt.index, last_txt.text))
        return True

    def get_text(self):
        """Returns the current state of the text buffer."""
        return self.text
