import argparse
from manager import StudentManager

def main():
    manager = StudentManager()
    parser = argparse.ArgumentParser(description="🎓 Student Management System")
    sub = parser.add_subparsers(dest="command")

    # Add
    add = sub.add_parser("add", help="Add a new student")
    add.add_argument("id", help="Student ID (unique)")
    add.add_argument("name", help="Student Name")
    add.add_argument("grade", help="Student Grade (e.g. A, B+)")

    # Update
    update = sub.add_parser("update", help="Update a student record")
    update.add_argument("id", help="Student ID")
    update.add_argument("--name", help="New name")
    update.add_argument("--grade", help="New grade")

    # Delete
    delete = sub.add_parser("delete", help="Delete a student")
    delete.add_argument("id", help="Student ID")

    # List
    sub.add_parser("list", help="List all students")

    args = parser.parse_args()

    if args.command == "add":
        manager.add(args.id, args.name, args.grade)
    elif args.command == "update":
        manager.update(args.id, args.name, args.grade)
    elif args.command == "delete":
        manager.delete(args.id)
    elif args.command == "list":
        manager.list_all()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()