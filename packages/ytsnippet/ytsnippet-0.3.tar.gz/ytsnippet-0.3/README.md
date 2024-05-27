# Snippet Manager

A simple command-line tool to manage code snippets.

## Installation

```sh
pip install ytsnippet
```

## Usage Interactive Mode

```sh
ytsnippet --interactive
```

Run the above command to start interactive mode, where you can add, search, view, and delete snippets interactively.

### Add a snippet

```sh
Command: add
Title: Example Snippet
Content: print('Hello, World!')
Tags (comma-separated): example, hello
```

Follow the prompts to add a new snippet. You will be asked for the title, content, and tags of the snippet.

### Search snippets

```sh
Command: search
Search query: hello
```

Enter a search query to find snippets matching the title or tags.

### View a snippet

```sh
Command: view
Snippet ID: 1
```

Enter the ID of the snippet you want to view.

### Delete a snippet

```sh
Command: delete
Snippet ID: 1
```

Enter the ID of the snippet you want to delete.
