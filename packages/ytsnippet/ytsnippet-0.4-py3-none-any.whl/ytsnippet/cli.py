# snippet_manager/cli.py
import argparse
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from .database import add_snippet, search_snippets, view_snippet, delete_snippet

def interactive_cli():
    commands = ['add', 'search', 'view', 'delete', 'exit']
    command_completer = WordCompleter(commands, ignore_case=True)

    while True:
        command = prompt('Command: ', completer=command_completer).strip()

        if command == 'add':
            title = prompt('Title: ').strip()
            content = prompt('Content: ').strip()
            tags = prompt('Tags (comma-separated): ').strip()
            add_snippet(title, content, tags)
        
        elif command == 'search':
            query = prompt('Search query: ').strip()
            results = search_snippets(query)
            for result in results:
                print(f'ID: {result[0]}, Title: {result[1]}, Tags: {result[3]}')
        
        elif command == 'view':
            snippet_id = prompt('Snippet ID: ').strip()
            snippet = view_snippet(int(snippet_id))
            if snippet:
                print(f'ID: {snippet[0]}\nTitle: {snippet[1]}\nContent:\n{snippet[2]}\nTags: {snippet[3]}')
            else:
                print(f'Snippet with ID {snippet_id} not found.')
        
        elif command == 'delete':
            snippet_id = prompt('Snippet ID: ').strip()
            delete_snippet(int(snippet_id))
        
        elif command == 'exit':
            break
        
        else:
            print('Unknown command. Available commands: add, search, view, delete, exit.')

def main():
    parser = argparse.ArgumentParser(description='Code Snippet Manager')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    args = parser.parse_args()

    if args.interactive:
        interactive_cli()
    else:
        subparsers = parser.add_subparsers(dest='command')

        add_parser = subparsers.add_parser('add', help='Add a new snippet')
        add_parser.add_argument('title', help='Title of the snippet')
        add_parser.add_argument('content', help='Content of the snippet')
        add_parser.add_argument('tags', help='Tags for the snippet (comma-separated)')

        search_parser = subparsers.add_parser('search', help='Search snippets by title or tags')
        search_parser.add_argument('query', help='Search query')

        view_parser = subparsers.add_parser('view', help='View a snippet by ID')
        view_parser.add_argument('id', type=int, help='ID of the snippet')

        delete_parser = subparsers.add_parser('delete', help='Delete a snippet by ID')
        delete_parser.add_argument('id', type=int, help='ID of the snippet')

        args = parser.parse_args()

        if args.command == 'add':
            add_snippet(args.title, args.content, args.tags)
        elif args.command == 'search':
            results = search_snippets(args.query)
            for result in results:
                print(f'ID: {result[0]}, Title: {result[1]}, Tags: {result[3]}')
        elif args.command == 'view':
            snippet = view_snippet(args.id)
            if snippet:
                print(f'ID: {snippet[0]}\nTitle: {snippet[1]}\nContent:\n{snippet[2]}\nTags: {snippet[3]}')
            else:
                print(f'Snippet with ID {args.id} not found.')
        elif args.command == 'delete':
            delete_snippet(args.id)
        else:
            parser.print_help()

if __name__ == '__main__':
    main()
