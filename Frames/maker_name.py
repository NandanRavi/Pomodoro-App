import tkinter as tk
from tkinter import ttk

class Maker(ttk.Frame):
    def __init__(self,parent,previous_frame):
        super().__init__(parent)
        self["style"]="Background.TFrame"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        maker_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )
        maker_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        maker_container.columnconfigure(0, weight=1)
        maker_container.rowconfigure(1, weight=1)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        settings_button = ttk.Button(button_container, text="Back",
                                  command=previous_frame,
                                  style="PomodoroButton.TButton",
                                  cursor="hand2"
                                  )
        settings_button.grid(row=1, column=0, sticky="EW", padx=2)
