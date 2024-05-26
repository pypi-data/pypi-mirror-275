import os

todo_file = 'todo_list.txt'

# todo_list.txtからToDoリストを読み込む関数
def load_todos():
    if os.path.exists(todo_file):
        with open(todo_file, 'r') as file:
            todos = file.readlines()
        todos = [todo.strip() for todo in todos]
    else:
        todos = []
    return todos

# todo_list.txtにタスクを書き込んで保存する関数
def save_todos(todos):
    with open(todo_file, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

# todoを追加→save_todos呼び出し
def add_todo(todos, item):
    todos.append(item)
    save_todos(todos)

# todoを削除→save_todos呼び出し
def delete_todo(todos, index):
    if 0 <= index < len(todos):
        todos.pop(index)
        save_todos(todos)

def main():
    todos = load_todos()

    while True:
        command = input("コマンドを入力してください（追加、表示、削除、終了）: ")
        if command == '終了':
            break
        elif command == '追加':
            item = input("ToDo項目を入力してください: ")
            add_todo(todos, item)
        elif command == '表示':
            for i, todo in enumerate(todos):
                print(f"{i}: {todo}")
        elif command == '削除':
            index = int(input("削除するToDoの番号を入力してください: "))
            delete_todo(todos, index)
        else:
            print("無効なコマンドです。")

if __name__ == '__main__':
    main()