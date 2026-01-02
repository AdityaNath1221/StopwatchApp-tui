from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class Stopwatch(App):
    
    def compose(self):
        """What widgets are there in the app"""
        yield Header()
        yield Footer()

if __name__ == "__main__":
    Stopwatch().run()