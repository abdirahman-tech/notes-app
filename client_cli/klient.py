import sys
import json
import urllib.request
import urllib.error

API = "http://127.0.0.1:8000"

def request(method, path, data=None):
    url = API + path
    body = json.dumps(data).encode() if data else None
    headers = {"Content-Type": "application/json"} if body else {}
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"Error {e.code}: {e.read().decode()}")
        return None

def print_notes(notes):
    if not notes:
        print("  (no notes)")
    for n in notes:
        print(f"  [{n['id']}] {n['title']}: {n['content']}")

def print_todos(todos):
    if not todos:
        print("  (no todo lists)")
    for t in todos:
        print(f"  [{t['id']}] {t['title']}")
        for task in t.get("tasks", []):
            done = "✓" if task["completed"] else "○"
            print(f"       {done} {task['text']}")

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python klient.py list notes")
        print("  python klient.py list todos")
        print("  python klient.py add note <title> <content>")
        print("  python klient.py add todo <title> <task1> [task2 ...]")
        return

    if args[0] == "list":
        if args[1] == "notes":
            print_notes(request("GET", "/notes"))
        elif args[1] == "todos":
            print_todos(request("GET", "/todos"))

    elif args[0] == "add":
        if args[1] == "note" and len(args) >= 4:
            result = request("POST", "/notes", {"title": args[2], "content": args[3]})
            if result:
                print(f"Note created: id={result['id']}")
        elif args[1] == "todo" and len(args) >= 3:
            tasks = [{"text": t, "completed": False} for t in args[3:]]
            result = request("POST", "/todos", {"title": args[2], "tasks": tasks})
            if result:
                print(f"Todo list created: id={result['id']}")
        else:
            print("Missing arguments.")
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
