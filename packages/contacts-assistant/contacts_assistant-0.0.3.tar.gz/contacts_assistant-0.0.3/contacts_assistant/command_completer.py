from prompt_toolkit.completion import Completer, Completion

class CommandCompleter(Completer):
    def __init__(self, command_args, book):
        super().__init__()
        self.command_args = command_args
        self.book = book

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
        tokens = text_before_cursor.split()
        if len(tokens) == 0:
            return

        # If the user is typing the command
        if len(tokens) == 1:
            word_before_cursor = tokens[0]
            for command in self.command_args:
                if command.startswith(word_before_cursor):
                    yield Completion(command, start_position=-len(word_before_cursor))
        else:
            # User has entered a command and is now typing parameters
            command = tokens[0]
            if command in self.command_args:
                param_prefix = tokens[-1]
                for param in self.command_args[command]:
                    if param.startswith(param_prefix) and param not in tokens:
                        yield Completion(param, start_position=-len(param_prefix))
