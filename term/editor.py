from utilities import Colors, clear_screen, coltxt
from prompt_toolkit import PromptSession
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings

def editor(txtfile: str):
    clear_screen()
    path = f"files/{txtfile}.txt"

    try:
        with open(path, 'r', encoding='utf-8') as f:
            initial_text = f.read()
    except FileNotFoundError:
        initial_text = ""

    print(coltxt(f"Editing {txtfile}.txt (Ctrl+T = commands, Ctrl+Q = save and quit)\n",
                 Colors.grey))

    kb = KeyBindings()
    command_last = {"value": None} 

    @kb.add('c-c')
    def _(event):
        event.app.exit(result=event.app.current_buffer.text)

    @kb.add('c-t')
    def _(event):
        from prompt_toolkit.shortcuts import input_dialog

        cmd = input_dialog(
            title="Command mode",
            text="Tape ta commande :"
        ).run()

        if cmd is not None:
            command_last["value"] = cmd
            print(coltxt(f"\n[Commande reçue] {cmd}\n", Colors.grey))

    session = PromptSession(key_bindings=kb)


    text = session.prompt(
        default=initial_text,
        multiline=True,
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    clear_screen()
    print(coltxt(f"{txtfile}.txt saved.", Colors.grey))
    if command_last["value"]:
        print(coltxt(f"Dernière commande saisie : {command_last['value']}", Colors.grey))