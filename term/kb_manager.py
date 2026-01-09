from prompt_toolkit.key_binding import KeyBindings

def get_editor_bindings(on_quit, on_undo, on_redo):
    kb = KeyBindings()

    @kb.add("c-q")
    def _(event):
        on_quit(event)

    @kb.add("c-z")
    def _(event):
        on_undo(event)

    @kb.add("c-r")
    def _(event):
        on_redo(event)

    return kb