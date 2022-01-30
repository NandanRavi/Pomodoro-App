import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent,controller, show_timer):
        super().__init__(parent)

        self["style"]="Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        settings_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )
        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1,weight=1)

        pomodoro_label = ttk.Label(settings_container,text="Pomodoro:",style="LightText.TLabel")
        pomodoro_label.grid(column=0, row=0, sticky="W")

        pomodoro_input = tk.Spinbox(settings_container,from_=0,to=120,increment=1,
                                    justify="center",
                                    textvariable=controller.pomodoro,
                                    width=10
        )
        pomodoro_input.grid(row=0,column=1,sticky="EW")
        pomodoro_input.focus()

        long_break= ttk.Label(settings_container,text="Long break time",style="LightText.TLabel")
        long_break.grid(row=1,column=0,sticky="W")

        long_input = tk.Spinbox(settings_container,from_=0,to=60,
            increment=1,
            justify="center",
            textvariable=controller.long_break,
            width=10
        )
        long_input.grid(row=1,column=1,sticky="EW")

        short_break= ttk.Label(settings_container,text="Short break time",style="LightText.TLabel")
        short_break.grid(row=2,column=0,sticky="W")

        short_input = tk.Spinbox(settings_container,from_=0,to=30,increment=1,
            justify="center",
            textvariable=controller.short_break,
            width=10
        )
        short_input.grid(column=1, row=2, sticky="EW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self,style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        timer_button = ttk.Button(button_container,text="Back",
            command=show_timer,
            style="PomodoroButton.TButton",
            cursor="hand2"
        )
        timer_button.grid(row=0,column=0,sticky="EW", padx=2)

        made_by=ttk.Label(button_container,text="Made By Ravi Nandan",font=("Helvetica",14),style="TimerText.TLabel")
        made_by.grid(row=1,column=0,columnspan=2,sticky="EW",pady=10)
