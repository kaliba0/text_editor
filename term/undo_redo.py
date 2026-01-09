class UndoManager:
    def __init__(self, initial_state: str = ""):
        self.undo_stack = [initial_state]
        self.redo_stack = []

    def push_state(self, state: str):
        if self.undo_stack and state == self.undo_stack[-1]:
            return
        self.undo_stack.append(state)
        self.redo_stack = []

    def can_undo(self) -> bool:
        return len(self.undo_stack) > 1

    def can_redo(self) -> bool:
        return len(self.redo_stack) > 0

    def undo(self) -> str:
        if not self.can_undo():
            return self.undo_stack[-1]
        current = self.undo_stack.pop()
        self.redo_stack.append(current)
        return self.undo_stack[-1]

    def redo(self) -> str:
        if not self.can_redo():
            return self.undo_stack[-1]
        state = self.redo_stack.pop()
        self.undo_stack.append(state)
        return state