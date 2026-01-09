import time
from utilities import Colors, clear_screen, coltxt
from prompt_toolkit import PromptSession
from undo_redo import UndoManager
from kb_manager import get_editor_bindings
import pathlib

def editor(txtfile: str):
    clear_screen()
    term_dir = pathlib.Path(__file__).resolve().parent
    project_dir = term_dir.parent
    files_dir = project_dir / "files"
    path = f"{files_dir}/{txtfile}.txt"

    try:
        with open(path, "r", encoding="utf-8") as f:
            initial_text = f.read()
    except FileNotFoundError:
        initial_text = ""

    print(f"{coltxt(f'{txtfile}.txt', Colors.grey_bold)} {coltxt("(Ctrl+Q save and quit | Ctrl+Z undo | Ctrl+R redo)\n", Colors.grey)}")

    session = PromptSession()
    history = UndoManager(initial_text)

    last_push_time = {"t": time.time()}
    pending_state = {"text": initial_text}

    def maybe_push_state(force: bool = False):
        now = time.time()
        if force or (now - last_push_time["t"] >= 0.4):
            history.push_state(pending_state["text"])
            last_push_time["t"] = now

    def on_quit(event):
        buf = event.app.current_buffer
        pending_state["text"] = buf.text
        maybe_push_state(force=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(buf.text)

        event.app.exit(result="__QUIT__")

    def on_undo(event):
        buf = event.app.current_buffer
        pending_state["text"] = buf.text
        maybe_push_state(force=True)

        new_text = history.undo()
        buf.text = new_text
        buf.cursor_position = len(new_text)

    def on_redo(event):
        buf = event.app.current_buffer
        new_text = history.redo()
        buf.text = new_text
        buf.cursor_position = len(new_text)

    kb = get_editor_bindings(on_quit, on_undo, on_redo)

    def pre_run():
        buf = session.app.current_buffer

        def on_text_changed(_):
            pending_state["text"] = buf.text
            maybe_push_state(force=False)

        buf.on_text_changed += on_text_changed

    result = session.prompt(
        default=initial_text,
        multiline=True,
        key_bindings=kb,
        pre_run=pre_run
    )

    if result == "__QUIT__":
        return "back"

    with open(path, "w", encoding="utf-8") as f:
        f.write(pending_state["text"])
    return "back"