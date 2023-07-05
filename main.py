import tkinter
import math
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- PLAY SOUND ------------------------------- #

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("ting.mp3")
    pygame.mixer.music.play()

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    window.after_cancel(timer)
    # timer text "00:00"
    canvas.itemconfig(timer_text, text="00:00")
    # timer label to say timer
    timer_label.config(text="Timer")
    # reset checkmarks
    checkmarks_label.config(text="")
    # update reps
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 60
    # work_min_sec = 14
    short_break_min_sec = SHORT_BREAK_MIN * 60
    # short_break_min_sec = 5
    long_break_min_sec = LONG_BREAK_MIN * 60
    # long_break_min_sec = 10
    if reps == 8:
        count_down(long_break_min_sec)
        timer_label.config(text="Break", fg=RED)
        print("long break")
    elif reps % 2 == 0:
        count_down(short_break_min_sec)
        timer_label.config(text="Break", fg=PINK)
        print("short break")
    else:
        count_down(work_min_sec)
        timer_label.config(text="Work", fg=GREEN)
        print("work time")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    formatted_time = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=formatted_time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        play_sound()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks_label = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
