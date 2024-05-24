import sys

class ToDoList:
    def __init__(self):
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"タスク '{task}' を追加しました。")

    def view_tasks(self):
        if not self.tasks:
            print("タスクはありません。")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "完了" if task["completed"] else "未完了"
                print(f"{idx}. {task['task']} [{status}]")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"タスク '{self.tasks[task_index]['task']}' を完了しました。")
        else:
            print("無効なタスク番号です。")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            print(f"タスク '{task['task']}' を削除しました。")
        else:
            print("無効なタスク番号です。")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Doリスト管理アプリ")
        print("1. タスクを追加")
        print("2. タスクを表示")
        print("3. タスクを完了")
        print("4. タスクを削除")
        print("5. 終了")
        
        choice = input("選択肢を入力してください: ")
        
        if choice == "1":
            task = input("追加するタスクを入力してください: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("完了するタスクの番号を入力してください: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "4":
            task_index = int(input("削除するタスクの番号を入力してください: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("アプリを終了します。")
            sys.exit()
        else:
            print("無効な選択です。もう一度試してください。")

if __name__ == "__main__":
    main()