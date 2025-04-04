class Task:
    def __init__(self, task_id, title, description, due_date, priority, is_completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def update_task(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def get_task_details(self):
        status = "[Completed]" if self.is_completed else "[Pending]"
        return f"{status} {self.title} - Due: {self.due_date}, Priority: {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.sorted_tasks = []
        self.is_sorted = False
        self.first_output = True

    def add_task(self, task_id, title, description, due_date, priority):
        self.tasks.append(Task(task_id, title, description, due_date, priority))
        self.is_sorted = False

    def remove_task(self, task_id):
        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                del self.tasks[i]
                self.is_sorted = False
                return
        print(f"Task ID {task_id} not found.")

    def display_tasks(self, tasks, header):
        if header:
            if not self.first_output:
                print()
            print(f"{header}:")
            self.first_output = False
        if tasks:
            for i in range(len(tasks)):
                print(f"{tasks[i].task_id}. {tasks[i].get_task_details()}")

    def get_all_tasks(self):
        if self.is_sorted:
            self.display_tasks(self.sorted_tasks, "All Tasks")
        else:
            self.display_tasks(self.tasks, "All Tasks")

    def get_pending_tasks(self):
        source = self.sorted_tasks if self.is_sorted else self.tasks
        pending_tasks = []
        for i in range(len(source)):
            if not source[i].is_completed:
                pending_tasks.append(source[i])
        self.display_tasks(pending_tasks, "Pending Tasks")

    def get_completed_tasks(self):
        source = self.sorted_tasks if self.is_sorted else self.tasks
        completed_tasks = []
        for i in range(len(source)):
            if source[i].is_completed:
                completed_tasks.append(source[i])
        self.display_tasks(completed_tasks, "Completed Tasks")

    def sort_tasks(self, by="due_date"):
        if by == "due_date":
            self.tasks.sort(key=lambda task: task.due_date)
        elif by == "priority":
            self.tasks.sort(key=lambda task: task.priority)
        if self.is_sorted:
            self.display_tasks(self.sorted_tasks, "All Tasks")
        else:
            self.display_tasks(self.tasks, "All Tasks")

    def search_tasks(self, keyword):
        if not self.first_output:
            print()
        print(f"Search Results for: {keyword}")
        self.first_output = False
        keyword_lower = keyword.lower()
        found_tasks = []
        source = self.sorted_tasks if self.is_sorted else self.tasks
        for i in range(len(source)):
            if keyword_lower in source[i].title.lower() or keyword_lower in source[i].description.lower():
                found_tasks.append(source[i])
        self.display_tasks(found_tasks, "")

    def mark_completed(self, task_id):
        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                self.tasks[i].mark_completed()
                return
        print(f"Task ID {task_id} not found.")

    def update_task(self, task_id, title, description, due_date, priority):
        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                self.tasks[i].update_task(title, description, due_date, priority)
                self.is_sorted = False
                return
        print(f"Task ID {task_id} not found.")


def parse_input_line(line):
    line = line.strip()
    if not line.endswith(')') or '(' not in line:
        return None, None

    method_name, args_part = line.split('(', 1)
    method_name = method_name.strip()
    args_part = args_part.rsplit(')', 1)[0]

    args = []
    current_arg = []
    in_quote = False

    for char in args_part + ',':
        if char == '"':
            in_quote = not in_quote
        elif char == ',' and not in_quote:
            arg = ''.join(current_arg).strip()
            if arg.startswith('"') and arg.endswith('"'):
                arg = arg[1:-1]
            args.append(arg)
            current_arg = []
        else:
            current_arg.append(char)

    return method_name, args


def main():
    todo = ToDoList()

    while True:
        try:
            line = input()
            if line.strip() == '':
                break

            method_name, args = parse_input_line(line)
            if not method_name:
                print("Invalid command format")
                continue

            if method_name == "add_task" and len(args) == 5:
                try:
                    todo.add_task(int(args[0]), args[1], args[2], args[3], args[4])
                except ValueError:
                    print("Task ID must be an integer")

            elif method_name in ["remove_task", "mark_completed"] and len(args) == 1:
                try:
                    getattr(todo, method_name)(int(args[0]))
                except ValueError:
                    print("Task ID must be an integer")

            elif method_name == "update_task" and len(args) == 5:
                try:
                    todo.update_task(int(args[0]), args[1], args[2], args[3], args[4])
                except ValueError:
                    print("Task ID must be an integer")

            elif method_name in ["get_all_tasks", "get_pending_tasks", "get_completed_tasks"]:
                getattr(todo, method_name)()

            elif method_name == "sort_tasks" and len(args) == 1 and args[0] in ["due_date", "priority"]:
                todo.sort_tasks(args[0])

            elif method_name == "search_tasks" and len(args) == 1:
                todo.search_tasks(args[0])

            else:
                print("Unknown or invalid command")

        except :
            break


if __name__ == "__main__":
    main()
