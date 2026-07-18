import customtkinter as ctk
import tkinter as tk

from analyzer import analyze_password
from generator import generate_password
from config import APP_NAME, APP_VERSION


# -----------------------------
# App Configuration
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# -----------------------------
# Functions
# -----------------------------

def analyze_button_clicked():

    password = password_entry.get()

    result = analyze_password(password)

    score = result["score"]
    strength = result["strength"]
    suggestions = result["suggestions"]
    length = result["length"]

    # Update score
    score_label.configure(
        text=f"Security Score: {score}/5"
    )

    # Update length
    length_label.configure(
        text=f"Password Length: {length} characters"
    )

    # Update progress bar
    progress_bar.set(score / 5)

    # Update strength status
    if strength == "Very Strong":

        status_label.configure(
            text="🟢 VERY STRONG",
            text_color="#00FF88"
        )

    elif strength == "Medium":

        status_label.configure(
            text="🟠 MEDIUM",
            text_color="#FFA500"
        )

    elif strength == "Weak" or strength == "Very Weak":

        status_label.configure(
            text="🔴 WEAK",
            text_color="#FF4444"
        )

    else:

        status_label.configure(
            text="⚪ NO PASSWORD",
            text_color="white"
        )

    # Security suggestions
    suggestion_text = "Security Suggestions:\n\n"

    for suggestion in suggestions:

        suggestion_text += f"• {suggestion}\n"

    suggestion_label.configure(
        text=suggestion_text
    )


def generate_button_clicked():

    password = generate_password(16)

    password_entry.delete(0, "end")

    password_entry.insert(0, password)

    analyze_button_clicked()


def copy_button_clicked():

    password = password_entry.get()

    if password:

        window.clipboard_clear()

        window.clipboard_append(password)

        status_label.configure(
            text="✓ PASSWORD COPIED",
            text_color="#00FF88"
        )


def toggle_password():

    if show_password.get():

        password_entry.configure(
            show=""
        )

    else:

        password_entry.configure(
            show="*"
        )


# -----------------------------
# Main Window
# -----------------------------

window = ctk.CTk()

window.title(
    f"{APP_NAME} v{APP_VERSION}"
)

window.geometry("750x750")

window.resizable(False, False)


# -----------------------------
# Header
# -----------------------------

title_label = ctk.CTkLabel(
    window,

    text="🔐 PASSWORD SECURITY ANALYZER",

    font=("Arial", 28, "bold")
)

title_label.pack(
    pady=(30, 5)
)


subtitle_label = ctk.CTkLabel(
    window,

    text="Analyze • Generate • Improve Your Password Security",

    font=("Arial", 15)
)

subtitle_label.pack(
    pady=(0, 25)
)


# -----------------------------
# Password Input
# -----------------------------

password_entry = ctk.CTkEntry(

    window,

    width=550,

    height=50,

    placeholder_text="Enter password to analyze",

    show="*",

    font=("Arial", 16)
)

password_entry.pack(
    pady=10
)


# -----------------------------
# Show Password
# -----------------------------

show_password = tk.BooleanVar()

show_checkbox = ctk.CTkCheckBox(

    window,

    text="👁 Show Password",

    variable=show_password,

    command=toggle_password
)

show_checkbox.pack(
    pady=5
)


# -----------------------------
# Buttons
# -----------------------------

button_frame = ctk.CTkFrame(

    window,

    fg_color="transparent"
)

button_frame.pack(
    pady=20
)


analyze_button = ctk.CTkButton(

    button_frame,

    text="🔍 Analyze Password",

    width=210,

    height=45,

    command=analyze_button_clicked
)

analyze_button.grid(

    row=0,

    column=0,

    padx=8
)


generate_button = ctk.CTkButton(

    button_frame,

    text="🔄 Generate Password",

    width=210,

    height=45,

    command=generate_button_clicked
)

generate_button.grid(

    row=0,

    column=1,

    padx=8
)


copy_button = ctk.CTkButton(

    button_frame,

    text="📋 Copy Password",

    width=210,

    height=45,

    command=copy_button_clicked
)

copy_button.grid(

    row=1,

    column=0,

    columnspan=2,

    pady=12
)


# -----------------------------
# Strength Status
# -----------------------------

status_label = ctk.CTkLabel(

    window,

    text="Enter a password to begin",

    font=("Arial", 24, "bold")
)

status_label.pack(
    pady=15
)


# -----------------------------
# Progress Bar
# -----------------------------

progress_bar = ctk.CTkProgressBar(

    window,

    width=550,

    height=20
)

progress_bar.set(0)

progress_bar.pack(
    pady=10
)


# -----------------------------
# Score
# -----------------------------

score_label = ctk.CTkLabel(

    window,

    text="Security Score: 0/5",

    font=("Arial", 18)
)

score_label.pack(
    pady=5
)


# -----------------------------
# Password Length
# -----------------------------

length_label = ctk.CTkLabel(

    window,

    text="Password Length: 0 characters",

    font=("Arial", 18)
)

length_label.pack(
    pady=5
)


# -----------------------------
# Suggestions
# -----------------------------

suggestion_label = ctk.CTkLabel(

    window,

    text="Security suggestions will appear here",

    font=("Arial", 15),

    justify="left",

    anchor="w"
)

suggestion_label.pack(

    pady=25,

    padx=50,

    anchor="w"
)


# -----------------------------
# Run Application
# -----------------------------

window.mainloop()