import tkinter as tk
from AutocompleteProvider import AutocompleteProvider

"""
Build our autocomplete GUI using tkinter, consisting of:
    - An entry box for word fragments
    - An output entry box for word candidates
    - A text box for adding passages to be trained
    - A submission button for adding new passages
    - A text box for displaying trained passages
"""

# ----- Event handlers -----


def submit_passage_command():
    """
    Event handler for submitting new passages
    retrieve all new passages from text widget and train
    """
    multiline_passage = text_passages.get("1.0", tk.END)
    auto_instance.train(multiline_passage)

    # add new passages to trained passages
    text_trained_passages.config(state="normal")
    text_trained_passages.insert(tk.END, multiline_passage)
    text_trained_passages.config(state="disabled")
    text_passages.delete("1.0", tk.END)


def handle_keypress(event):
    """
    Event handler for modifying our sentence fragment, new candidates are
    generated and inserted into the textbox output widget
    """
    fragment = input_entry.get()
    # remove previous results
    # insert new results
    candidates = auto_instance.getWords(fragment)
    # format candidate output
    c = [str(can) for can in candidates]
    c = ', '.join(c)
    candidate_label["text"] = c


# ----- Widgets for displaying content within window -----
window = tk.Tk()
# entry widget for user input
label = tk.Label(text="Input word fragment")
input_entry = tk.Entry()
label.pack()
input_entry.pack()

# entry widget for displaying candidates for sentence fragment
candidate_label = tk.Label()
candidate_label.pack()


# text widget and frame for passage submission
label_text = tk.Label(text="Enter training passages")
text_passages = tk.Text(height=6)
label_text.pack()
text_passages.pack()


# button widget for passage submission
btn_submit = tk.Button(text="Submit passage", command=submit_passage_command)
btn_submit.pack()

# message widget to display trained passages
label_trained_passages = tk.Label(text="Previously trained passages")
text_trained_passages = tk.Text(height=6)
label_trained_passages.pack()
text_trained_passages.pack()


# Whenever a key is pressed, the handle_keypress method is called
input_entry.bind("<Key>", handle_keypress)

auto_instance = AutocompleteProvider()
window.mainloop()
