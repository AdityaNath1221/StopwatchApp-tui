from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Static, Button

class TimeDisplay(Static):
    """Custom time display widget"""


class Stopwatch(Static):
    """Custom stopwatch widget"""

    def compose(self):
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", classes="hidden", variant="error")
        yield Button("Reset", id="reset", classes="hidden")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):

    BINDINGS = [("d", "toggle_dark_mode", "Toggle Dark Mode")]

    CSS_PATH = "stopwatch.css"

    def compose(self):
        """What widgets are there in the app"""
        yield Header(show_clock=True)
        yield Footer()
        with ScrollableContainer(id="stopwatches"):
            yield Stopwatch()
            yield Stopwatch()
            yield Stopwatch()

    # This is an action method.
    # Defines what a keybinding actually does
    def action_toggle_dark_mode(self):
        self.theme="textual-dark" if self.theme=="textual-light" else "textual-light"
    

if __name__ == "__main__":
    StopwatchApp().run()