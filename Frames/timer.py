import tkinter as tk
from tkinter import ttk
from collections import deque
from windows import dpi
dpi()

class Timer(ttk.Frame):
    def __init__(self,parent,controller,show_settings):
        super().__init__(parent)

        self["style"]="Background.TFrame"

        self.controller=controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        pomodoro_time=int(controller.pomodoro.get())
        self.current_timer_label=tk.StringVar(value=controller.timer_schedule[0])
        self.current_timer_label = tk.StringVar(value=self.controller.timer_schedule[0])
        self.current_time=tk.StringVar(value=f"{pomodoro_time:02d}:00")
        # self.current_time = tk.StringVar(value=f"{controller.pomodoro.get()}:00")
        self.timer_running=False
        self.time_decrement_job=None

        settings_button = ttk.Button(self, text="Settings", command=show_settings,
                                     style="PomodoroButton.TButton", cursor="hand2"
                                     )
        settings_button.grid(row=0, column=1, sticky="E", padx=10, pady=(10, 0))

        timer_description=ttk.Label(self,textvariable=self.current_timer_label,style="LightText.TLabel")
        timer_description.grid(row=0,column=0,sticky="W",padx=(10,0),pady=(10,0))

        timer_frame=ttk.Frame(self,height="100",style="Timer.TFrame")
        timer_frame.grid(row=1,column=0,pady=(10,0),columnspan=2,sticky="NSEW")

        timer_counter=ttk.Label(timer_frame,textvariable=self.current_time,style="TimerText.TLabel")
        timer_counter.place(relx=0.5,rely=0.5,anchor="center")

        button_container=ttk.Frame(self,padding=10,style="Background.TFrame")
        button_container.grid(row=2,column=0,columnspan=2, sticky="EW")
        button_container.columnconfigure((0,1),weight=1)

        self.start_button=ttk.Button(button_container,text="start",style="PomodoroButton.TButton",command=self.start_timer)
        self.start_button.grid(row=0,column=0,sticky="EW")

        self.stop_button=ttk.Button(button_container,text="stop",command=self.stop_timer,
                state="disabled",
                        cursor="hand2" )
        self.stop_button.grid(row=0,column=1,padx=5)

        reset_button=ttk.Button(button_container,text="reset",style="PomodoroButton.TButton",command=self.reset_timer,
                                cursor="hand2")
        reset_button.grid(row=0,column=2,sticky="EW")


    def start_timer(self):
        self.timer_running=True
        self.start_button["state"]="disabled"
        self.stop_button["state"]="enabled"
        self.decrement_time()

    def stop_timer(self):
        self.timer_running=False
        self.start_button["state"]="enabled"
        self.stop_button["state"]="disabled"

        if self.time_decrement_job:
            self.after_cancel(self.time_decrement_job)
            self.time_decrement_job=None

    def reset_timer(self):
        self.stop_timer()
        pomodoro_time=int(self.controller.pomodoro.get())
        self.current_time.set(f"{pomodoro_time:02d}:00")
        self.controller.timer_schedule=deque(self.controller.timer_order)
        self.current_timer_label.set(self.controller.timer_schedule[0])

    def decrement_time(self):
        current_time=self.current_time.get()

        if self.timer_running and current_time !="00:00":
            minutes,seconds=current_time.split(":")

            if int(seconds)>0:
                seconds=int(seconds)-1
                minutes=int(minutes)
            else:
                seconds=59
                minutes=int(minutes)-1
            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self.time_decrement_job=self.after(1000,self.decrement_time)

        elif self.timer_running and current_time=="00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up=self.controller.timer_schedule[0]
            self.current_timer_label.set(next_up)

            if next_up=="Pomodoro":
                pomodoro_time=int(self.controller.pomodoro.get())
                self.current_time.set(f"{pomodoro_time:02d}:00")
            elif next_up=="Short Break":
                short_break = int(self.controller.pomodoro.get())
                self.current_time.set(f"{short_break:02d}:00")
            elif next_up=="Long Break":
                long_break = int(self.controller.pomodoro.get())
                self.current_time.set(f"{long_break:02d}:00")
            self.time_decrement_job=self.after(1000, self.decrement_time)

