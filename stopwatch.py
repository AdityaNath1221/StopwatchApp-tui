from textual.app import App
from textual.widgets import Header, Footer


class Stopwatch(App):

    BINDINGS = [("d", "toggle_dark_mode", "Toggle Dark Mode")]

    def compose(self):
        """What widgets are there in the app"""
        yield Header(show_clock=True)
        yield Footer()

    # This is an action method.
    # Defines what a keybinding actually does
    def action_toggle_dark_mode(self):
        self.theme="textual-dark" if self.theme=="textual-light" else "textual-light"
    

if __name__ == "__main__":
    Stopwatch().run()