# import tkinter as tk
# from tkinter import filedialog

# class TextEditor:
#     def __init__(self, master):
#         self.master = master
#         master.title("Text Editor")

#         self.text_box = tk.Text(master, height=20, width=50)
#         self.text_box.pack()

#         self.save_button = tk.Button(master, text="Save", command=self.save_file)
#         self.save_button.pack()

#     def save_file(self):
#         text = self.text_box.get("1.0", "end-1c")

#         with open("text.txt", 'w') as file:
#             file.write(text)

# root = tk.Tk()
# text_editor = TextEditor(root)
# root.mainloop()

from tkinter.font import Font
import tkinter as tk
from tkinter import filedialog


class ListEditor:
    """
    A GUI program for editing and saving a list of items.

    Attributes:
        master (tk.Tk): The root tkinter window of the application.
        text_box (tk.Entry): The textbox for inputting new items.
        add_button (tk.Button): The button for adding new items to the list.
        list_box (tk.Listbox): The listbox for displaying the items.
        save_button (tk.Button): The button for saving the selected item to a file.
    """

    def __init__(self, master: tk.Tk) -> None:
        """
        Initializes the ListEditor object and sets up the tkinter interface.

        Args:
            master (tk.Tk): The root tkinter window of the application.
        """
        self.master = master
        master.title("Editor de texto para OBS")


        utf8_font = Font(family="Helvetica", size=12)
        utf8_font_title = Font(family="Helvetica", size=14)

        # create a label
        self.label = tk.Label(master, text="Actualizador texto para OBS", font=utf8_font_title)
        self.label.pack()

        # create a label
        self.label = tk.Label(master, text="Texto a registrar", font=utf8_font)
        self.label.pack()

        # create the text box to input new items
        self.text_box = tk.Entry(master, font=utf8_font)
        self.text_box.pack(fill=tk.BOTH)

        # create the button to add new items to the list
        self.add_button = tk.Button(master, text="Agregar Texto", command=self.add_item, font=utf8_font)
        self.add_button.pack()

        # create the button to load items from a file
        self.load_button = tk.Button(master, text="Cargar Archivo", command=self.load_list, font=utf8_font)
        self.load_button.pack()
        
        # create a label
        self.label = tk.Label(master, text="Seleccionar el texto para publicar", font=utf8_font)
        self.label.pack()

        # create the list box to display items
        self.list_box = tk.Listbox(master, selectmode='single', exportselection=0, font=utf8_font)
        self.list_box.pack(fill=tk.BOTH, expand=-1)

        # create the button to delete selected item(s) from the list
        self.delete_button = tk.Button(master, text="Borrar Selección", command=self.delete_item, font=utf8_font)
        self.delete_button.pack()

        # create the button to save the selected item to a file
        self.save_button = tk.Button(master, text="Publicar archivo de texto con la selección", command=self.save_item, font=utf8_font)
        self.save_button.pack()

    def add_item(self) -> None:
        """
        Adds the item in the text box to the list box.
        """
        item = self.text_box.get()

        # only add the item to the list if it's not already there
        if item not in self.list_box.get(0, "end"):
            self.list_box.insert("end", item)
            self.clear_text()

    def save_item(self) -> None:
        """
        Saves the selected item from the list box to a file.
        """
        selected_item = self.list_box.get(self.list_box.curselection())
        if selected_item:
            with open("text.txt", "w") as file:
                file.write(selected_item)

    def delete_item(self) -> None:
        """
        Deletes the selected item(s) from the list box.
        """
        selected_indices = self.list_box.curselection()

        # only delete the item(s) from the list if there is at least one item selected
        if selected_indices:
            for i in reversed(selected_indices):
                self.list_box.delete(i)

    def load_list(self) -> None:
        """
        Loads a list of items from a file into the list box.
        """
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            with open(file_path, 'r', encoding="utf-8") as file:
                for item in file:
                    # only add the item to the list if it's not already there
                    if item not in self.list_box.get(0, "end"):
                        self.list_box.insert("end", item.strip())

    #Define a function to clear the Entry Widget Content
    def clear_text(self):
        self.text_box.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    list_editor = ListEditor(root)
    root.mainloop()
