import argparse

def main():
    parser = argparse.ArgumentParser(description='Command line interface for snippet manager')
    parser.add_argument('--interactive', action='store_true', help='Start interactive mode')
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    else:
        parser.print_help()

def interactive_mode():
    print("Welcome to Interactive Mode! Type 'help' for a list of available commands.")
    while True:
        command = input(">> ")
        if command == 'help':
            print("Available commands:")
            print("add: Add a new snippet")
            print("search: Search for snippets")
            print("view: View a snippet")
            print("delete: Delete a snippet")
            print("exit: Exit interactive mode")
        elif command == 'add':
            title = input("Enter snippet title: ")
            content = input("Enter snippet content: ")
            add_snippet(title, content)
        elif command == 'search':
            keyword = input("Enter search keyword: ")
            search_snippets(keyword)
        elif command == 'view':
            id = input("Enter snippet ID: ")
            view_snippet(id)
        elif command == 'delete':
            id = input("Enter snippet ID to delete: ")
            delete_snippet(id)
        elif command == 'exit':
            print("Exiting interactive mode.")
            break
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    main()
