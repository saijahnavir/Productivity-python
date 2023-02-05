import tkinter as tk
import tkinter.messagebox
import customtkinter
from playsound import playsound
import time



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Productivity app.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="pomodoro", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="To-do", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Web blocker", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create todo tabview
        self.tabview = customtkinter.CTkTabview(self, width=350)
        self.tabview.grid(row=0, column=2, padx=(15, 10), pady=(20, 0), sticky="nsew")
        self.tabview.add("To - Do")
        self.tabview.tab("To - Do").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        
        # self.check_var = tkinter.StringVar("on")

        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.tabview.tab("To - Do"),text="Task 1", command=self.checkbox_event, onvalue="on", offvalue="off")
        self.checkbox_1.grid(row=0, column=0, padx=20, pady=(10, 10), sticky='n')
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.tabview.tab("To - Do"), text="Task 2", command=self.checkbox_event, onvalue="on", offvalue="off")
        self.checkbox_2.grid(row=1, column=0, padx=20, pady=(10, 10), sticky='n')
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.tabview.tab("To - Do"),text="Task 3", command=self.checkbox_event, onvalue="on", offvalue="off")
        self.checkbox_3.grid(row=2, column=0, padx=20, pady=(10, 10), sticky='n')


        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.1", "Add " + "Revision Notes here :")

        #pomodoro
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.tabview.add("Pomodoro")
        # self.tabview.add(pomodoro(tk,tk()))
        self.pbtn_start = customtkinter.CTkButton(self.tabview.tab("Pomodoro"),text="start", command=self.pomodoro_start_event)
        self.pbtn_start.grid(row=1, column=0, padx=20, pady=10)
        self.pbtn_break = customtkinter.CTkButton(self.tabview.tab("Pomodoro"),text="break", command=self.pomodoro_break_event)
        self.pbtn_break.grid(row=1, column=4, padx=(45,20), pady=10)



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def pomodoro_start_event(self):
        print("Pomo start clicked")
    
    def pomodoro_break_event(self):
        print("Pomo break clicked")
    
    def checkbox_event(self):
        print("checkbox toggled")



if __name__ == "__main__":
    app = App()
    app.mainloop()
