#customizable_alphabet_encoder-decoder_with_tkinter_GUI_and_dictionar_import_export_function
#version 1.0.1
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import winreg
import os
import traceback
import ast

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def creat_popup_menu():
    global popup_menu
    popup_menu = tk.Menu(root, tearoff=0)
    popup_menu.add_command(label="Cut         Ctrl+X")
    popup_menu.add_command(label="Copy      Ctrl+C")
    popup_menu.add_command(label="Paste      Ctrl+V")
    root.bind_class("Text", "<Button-3><ButtonRelease-3>", show_popup_menu)
    root.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_popup_menu)

def show_popup_menu(target):
    n = target.widget
    popup_menu.entryconfigure("Cut         Ctrl+X",command=lambda: n.event_generate("<<Cut>>"))
    popup_menu.entryconfigure("Copy      Ctrl+C",command=lambda: n.event_generate("<<Copy>>"))
    popup_menu.entryconfigure("Paste      Ctrl+V",command=lambda: n.event_generate("<<Paste>>"))
    popup_menu.tk.call("tk_popup", popup_menu, target.x_root, target.y_root)

def show_error_method_1(self, *args):
    error = "There is/are invalid input(s) in method 1 setting."
    messagebox.showerror('Exception', error)

def check_if_valid_method_1():
    global tamp_dictionary_encryption
    global error_code
    global dictionary_encryption
    list_check_if_valid = []
    tamp_dictionary_encryption = {}
    tamp_dictionary_encryption = dictionary_encryption
    for n in dictionary_encryption:
        get_tamp = change_dictionary_entry[n].get()
        tk.Tk.report_callback_exception = show_error_method_1
        #error not in below coding will be count as error in show_error_method_1
        get_tamp = list(get_tamp)
        if get_tamp[0] == " ":
            error_code = 1      #error for enter " ", space only
            return False
        elif get_tamp[0] in list_check_if_valid:
            error_code = 2      #error for enter repetitive character
            return False
        elif get_tamp[0].isalpha() == False:
            error_code = 3      #error for enter non-character
            return False
        else:
            tamp_dictionary_encryption[n] = get_tamp[0]
            list_check_if_valid.append(get_tamp[0])
    return True

def method_1_apply():
    global dictionary_decryption
    global dictionary_encryption
    global tamp_dictionary_encryption
    if check_if_valid_method_1() == True:
        dictionary_encryption = tamp_dictionary_encryption
        dictionary_decryption = {v: k for k, v in dictionary_encryption.items()}

        dict_row_position = 0 
        dict_column_position = 0
        for n in dictionary_encryption:
            dictionary_label[n].destroy()
            dictionary_label[n] = tk.Label(frame_dict, font=("Arial",  14), text= n + "→" + dictionary_encryption[n][0])
            dictionary_label[n].grid(row=dict_row_position, column=dict_column_position, sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(frame_dict, dict_row_position, weight=1)
            tk.Grid.columnconfigure(frame_dict, dict_column_position, weight=1)
            dict_column_position += 1
            if dict_column_position == 10:
                dict_column_position=0
                dict_row_position += 1

        c_dict_row_position = 0 
        c_dict_column_position = 0
        for n in dictionary_encryption:
            change_dictionary_entry[n].destroy()
            change_dictionary_entry[n] = tk.Entry(frame_change_dict_main_1, font=("Arial",  14), width =1)
            change_dictionary_entry[n].insert(0, dictionary_encryption[n][0])
            change_dictionary_entry[n].grid(row=c_dict_row_position, column=c_dict_column_position+1, sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(frame_change_dict_main_1, c_dict_row_position, weight=1)
            tk.Grid.columnconfigure(frame_change_dict_main_1, c_dict_column_position+1, weight=1)
            c_dict_column_position += 2
            if c_dict_column_position == 20:
                c_dict_column_position = 0
                c_dict_row_position += 1

    elif error_code == 1:
        messagebox.showinfo("Error", "There is/are null input in method 1 setting.")
    elif error_code == 2:
        messagebox.showinfo("Error", "There is/are repetitive input in method 1 setting.")
    elif error_code == 3:
        messagebox.showinfo("Error", "Please input alpha letter only in method 1 setting.")
    
def method_2_apply():
    get_tamp_swap = swap_no_entry.get()
    if get_tamp_swap.isdigit() == True:
        swap_no = int(get_tamp_swap)
        if swap_no > 26:
            messagebox.showinfo("Error", "Please input interger within -26 to 26 in method 2 setting.")
        else:
            dictionary_positive_rearrange(swap_no) 
    elif get_tamp_swap.startswith('-') or get_tamp_swap.startswith('+') and get_tamp_swap[1:].isdigit() == True:
        if get_tamp_swap.startswith('+') == True:
            swap_no = int(get_tamp_swap[1:])
            if swap_no > 26:
                messagebox.showinfo("Error", "Please input interger within -26 to 26 in method 2 setting.")
            else:   
                dictionary_positive_rearrange(swap_no) 
        if get_tamp_swap.startswith('-') == True:
            swap_no = 26 - int(get_tamp_swap[1:])
            if swap_no < -26:
                messagebox.showinfo("Error", "Please input interger within -26 to 26 in method 2 setting.")
            else:   
                dictionary_positive_rearrange(swap_no)
              
    else:
        messagebox.showinfo("Error", "Please input '+' or '-' interger only in method 2 setting.")


def dictionary_positive_rearrange(swap_no): 
    global dictionary_decryption
    global dictionary_encryption
    dictionary_encryption = {}
    for n,v in zip(range(26-swap_no), range(swap_no,26)):
            swapped_a_to_z[n] = a_to_z[v]
    for n,v in zip(range(-swap_no,0), range(0,swap_no)):
        swapped_a_to_z[n] = a_to_z[v]
    for n,v in zip(a_to_z, range(26)):
        dictionary_encryption[n] = swapped_a_to_z[v]
    dictionary_encryption.update(dict((k.upper(), v.upper()) for k,v in dictionary_encryption.items()))
    dictionary_decryption = {v: k for k, v in dictionary_encryption.items()}

    dict_row_position = 0 
    dict_column_position = 0
    for n in dictionary_encryption:
        dictionary_label[n].destroy()
        dictionary_label[n] = tk.Label(frame_dict, font=("Arial",  14), text= n + "→" + dictionary_encryption[n][0])
        dictionary_label[n].grid(row=dict_row_position, column=dict_column_position, sticky=tk.N+tk.S+tk.E+tk.W)
        tk.Grid.rowconfigure(frame_dict, dict_row_position, weight=1)
        tk.Grid.columnconfigure(frame_dict, dict_column_position, weight=1)
        dict_column_position += 1
        if dict_column_position == 10:
            dict_column_position=0
            dict_row_position += 1

    c_dict_row_position = 0 
    c_dict_column_position = 0
    for n in dictionary_encryption:
        change_dictionary_entry[n].destroy()
        change_dictionary_entry[n] = tk.Entry(frame_change_dict_main_1, font=("Arial",  14), width =1)
        change_dictionary_entry[n].insert(0, dictionary_encryption[n][0])
        change_dictionary_entry[n].grid(row=c_dict_row_position, column=c_dict_column_position+1, sticky=tk.N+tk.S+tk.E+tk.W)
        tk.Grid.rowconfigure(frame_change_dict_main_1, c_dict_row_position, weight=1)
        tk.Grid.columnconfigure(frame_change_dict_main_1, c_dict_column_position+1, weight=1)
        c_dict_column_position += 2
        if c_dict_column_position == 20:
            c_dict_column_position = 0
            c_dict_row_position += 1

def process():
    mode = current_decrypt_or_encrypt.get()
    if mode == "encrypt":
        text_chipher_local = []
        text_plain = text_original_text.get("1.0", tk.END) 
        text_plain = list(text_plain)
        for n in text_plain:
                if n.isalpha() == True:
                    text_chipher_local.append(dictionary_encryption[n][0])
                else:
                    text_chipher_local.append(n)

        text_chipher_local = ''.join(text_chipher_local)
        processed_text_update(text_chipher_local)

    if mode == "decrypt":
        text_plain_local = []
        text_chipher = text_original_text.get("1.0", tk.END) 
        text_chipher = list(text_chipher)
        for n in text_chipher:
                if n.isalpha() == True:
                    text_plain_local.append(dictionary_decryption[n][0])
                else:
                    text_plain_local.append(n)

        text_plain_local = ''.join(text_plain_local)
        processed_text_update(text_plain_local)

def processed_text_update(result):
    text_processed_text.delete("1.0",tk.END)
    text_processed_text.insert(tk.END, result)

def export():
    global dictionary_encryption
    global dictionary_filename
    export_directory = filedialog.asksaveasfilename(initialdir=dictionary_filename, title="Choose export directory.",
                                                    filetypes=(("txt files", "*.txt"), ("All file tpyes", "*.*")))
    dict_txt_export = open(export_directory, "w")
    dict_txt_export.write(str(dictionary_encryption))
    dict_txt_export.close()
    export_directory = os.path.dirname(export_directory)
    os.system("start "+export_directory)

def import_txt_and_apply():
    global dictionary_filename
    global tamp_dictionary_encryption
    dictionary_filename = filedialog.askopenfilename(initialdir=dictionary_filename, title="Choose existing encryption dictionary.",
                                                    filetypes=(("txt files", "*.txt"), ("All file tpyes", "*.*")))
    try:
        dict_txt_import = open(dictionary_filename, "r")
    except:
        tk.Tk.report_callback_exception = show_error_import
    dict_txt_import = open(dictionary_filename, "r")
    tamp_dictionary_encryption = dict_txt_import.readline(10000)
    dict_txt_import.close()

    dictionary_len = tamp_dictionary_encryption.count("': '")
    dictionary_len_2 = tamp_dictionary_encryption.count("':'")
    dictionary_len_3 = tamp_dictionary_encryption.count('": "')
    dictionary_len_4 = tamp_dictionary_encryption.count('":"')
    dictionary_len = dictionary_len + dictionary_len_2 + dictionary_len_3 + dictionary_len_4
    if dictionary_len != 52:
        messagebox.showerror("Error", "There dictionary in import .txt has bad format.")
        return
    import_apply()

def show_error_import(self, *args):
    error = "There is/are invalid data in import .txt. or import cancelled."
    messagebox.showerror("Exception", error)

def check_if_valid_import():
    #general check for any bad format in dict in import .txt, like '', ' ' repetitive on key value
    global tamp_dictionary_encryption
    global error_code
    global dictionary_encryption
    tamp_tamp_dictionary_encryption = {}
    try:                  
        tamp_dictionary_encryption = ast.literal_eval(tamp_dictionary_encryption)
        assert type(tamp_dictionary_encryption) is dict
    except:
        tk.Tk.report_callback_exception = show_error_import

    for n in tamp_dictionary_encryption:            #read only 1 letter on key and apply back to dictionary
        check_n = list(n)
        tamp_tamp_dictionary_encryption.update({check_n[0]: tamp_dictionary_encryption[n]})
    tamp_dictionary_encryption = tamp_tamp_dictionary_encryption

    reverse_tamp_dictionary_encryption = {}
    reverse_tamp_dictionary_encryption = {v: k for k, v in tamp_dictionary_encryption.items()}

    #if key is repetitive, error code given
    if len(reverse_tamp_dictionary_encryption) != 52:
        error_code = 7
        return False
            
    list_check_if_valid = []
    list_check_if_valid_reverse = []
    for n,v in zip(tamp_dictionary_encryption, reverse_tamp_dictionary_encryption):
        tk.Tk.report_callback_exception = show_error_import
        #error not in below coding will be count as error in show_error_import
        get_tamp = tamp_dictionary_encryption[n]
        get_tamp = list(get_tamp)
        get_tamp_reverse = reverse_tamp_dictionary_encryption[v]
        get_tamp_reverse = list(get_tamp_reverse)
        #below is check value in dictionary imported
        if get_tamp[0] == " " or get_tamp_reverse[0] == " ":
            error_code = 4      #error for enter " ", space only
            return False
        elif get_tamp[0] in list_check_if_valid:
            error_code = 5      #error for enter repetitive character(value)
            return False
        elif get_tamp[0].isalpha() == False:
            error_code = 6      #error for enter non-character
            return False
        #Then below is check key in dictionary imported
        elif get_tamp_reverse[0].isalpha() == False:
            error_code = 6      #error for enter non-character
            return False
        elif get_tamp_reverse[0] in list_check_if_valid_reverse:
            error_code = 9      #check repetitive key
            return False
        else:
            tamp_dictionary_encryption[n] = get_tamp[0]
            list_check_if_valid.append(get_tamp[0])
            list_check_if_valid_reverse.append(get_tamp_reverse[0])
    return True

def import_apply():
    global dictionary_decryption
    global dictionary_encryption
    global tamp_dictionary_encryption
    global error_code

    if check_if_valid_import() == True:
        dictionary_encryption = tamp_dictionary_encryption
        dictionary_decryption = {v: k for k, v in dictionary_encryption.items()}
        
        dict_row_position = 0 
        dict_column_position = 0
        for n in dictionary_encryption:
            dictionary_label[n].destroy()
            dictionary_label[n] = tk.Label(frame_dict, font=("Arial",  14), text= n + "→" + dictionary_encryption[n][0])
            dictionary_label[n].grid(row=dict_row_position, column=dict_column_position, sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(frame_dict, dict_row_position, weight=1)
            tk.Grid.columnconfigure(frame_dict, dict_column_position, weight=1)
            dict_column_position += 1
            if dict_column_position == 10:
                dict_column_position=0
                dict_row_position += 1

        c_dict_row_position = 0 
        c_dict_column_position = 0
        for n in dictionary_encryption:
            change_dictionary_entry[n].destroy()
            change_dictionary_entry[n] = tk.Entry(frame_change_dict_main_1, font=("Arial",  14), width =1)
            change_dictionary_entry[n].insert(0, dictionary_encryption[n][0])
            change_dictionary_entry[n].grid(row=c_dict_row_position, column=c_dict_column_position+1, sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(frame_change_dict_main_1, c_dict_row_position, weight=1)
            tk.Grid.columnconfigure(frame_change_dict_main_1, c_dict_column_position+1, weight=1)
            c_dict_column_position += 2
            if c_dict_column_position == 20:
                c_dict_column_position = 0
                c_dict_row_position += 1

    elif error_code == 4:
        messagebox.showinfo("Error", "There is/are null data in import .txt.")
    elif error_code == 5:
        messagebox.showinfo("Error", "There is/are repetitive data (dictionary value) in import .txt.")
    elif error_code == 6:
        messagebox.showinfo("Error", "Please input alpha letter only in import .txt.")
    elif error_code == 7:
        messagebox.showinfo("Error", "There is/are repetitive data (dictionary key) in import .txt.")    
    #elif error_code == 8:
    #    messagebox.showinfo("Error", "Dictionary key(s) in import .txt is/are not in single alpha letter.")
    elif error_code == 9:
        messagebox.showinfo("Error", "There is/are repetitive data (dictionary key) in import .txt.") 
    else:
        messagebox.showinfo("Error", "Unexpected error")


#symbol for copy: →

dictionary_filename = ""
export_directory = ""
error_code = 0

a_to_z = string.ascii_lowercase[:26]
a_to_z = list(a_to_z)
swapped_a_to_z = list(a_to_z)
dictionary_encryption = {}
dictionary_decryption = {}

swap_no = 1

for n,v in zip(range(26-swap_no), range(swap_no,26)):
    swapped_a_to_z[n] = a_to_z[v]
for n,v in zip(range(-swap_no,0), range(0,swap_no)):
    swapped_a_to_z[n] = a_to_z[v]

for n,v in zip(a_to_z, range(26)):
    dictionary_encryption[n] = swapped_a_to_z[v]

dictionary_encryption.update(dict((k.upper(), v.upper()) for k,v in dictionary_encryption.items()))
dictionary_decryption = {v: k for k, v in dictionary_encryption.items()}

root = tk.Tk()
root.title("Alphabet Encryptor and Decryptor")
root.minsize(1300, 810)
root.geometry("800x800")
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)


creat_popup_menu()


frame_1 = tk.Frame(root)


label_title = tk.Label(frame_1, font=("Arial",  14), text="English alphabet Encryptor and Decryptor")
label_ask_mode = tk.Label(frame_1, font=("Arial",  14), text="Please choose a mode:")
label_dict_title = tk.Label(frame_1, font=("Arial",  14), text="Current Encrypt Dictionary:")

current_decrypt_or_encrypt = tk.StringVar()
current_decrypt_or_encrypt.set("encrypt")
radio_button_encode = tk.Radiobutton(frame_1, font=("Arial",  14), text="Encrypt mode", anchor=tk.CENTER, 
                                    variable=current_decrypt_or_encrypt, value="encrypt")
radio_button_decode = tk.Radiobutton(frame_1, font=("Arial",  14), text="Decrypt mode", anchor=tk.CENTER, 
                                    variable=current_decrypt_or_encrypt, value="decrypt")

tk.Grid.rowconfigure(frame_1, 0, weight=1)
tk.Grid.rowconfigure(frame_1, 2, weight=1)
tk.Grid.columnconfigure(frame_1, 0, weight=1)
tk.Grid.columnconfigure(frame_1, 1, weight=1)
tk.Grid.columnconfigure(frame_1, 2, weight=1)

frame_1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
label_title.grid(row=0, column=0, columnspan=3, sticky=tk.N+tk.S+tk.E+tk.W)
label_ask_mode.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
radio_button_encode.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
radio_button_decode.grid(row=2, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
label_dict_title.grid(row=3, column=0, columnspan=3, sticky=tk.N+tk.S+tk.E+tk.W)


frame_dict = tk.Frame(root)
frame_dict.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

dictionary_label = {}
dict_row_position = 0 
dict_column_position = 0
for n in dictionary_encryption:
    dictionary_label[n] = tk.Label(frame_dict, font=("Arial",  14), text= n + "→" + dictionary_encryption[n][0])
    dictionary_label[n].grid(row=dict_row_position, column=dict_column_position, sticky=tk.N+tk.S+tk.E+tk.W)
    tk.Grid.rowconfigure(frame_dict, dict_row_position, weight=1)
    tk.Grid.columnconfigure(frame_dict, dict_column_position, weight=1)
    dict_column_position += 1
    if dict_column_position == 10:
        dict_column_position=0
        dict_row_position += 1


label_change_dict_title = tk.Label(root, font=("Arial",  14) ,text="Method 1: Custome Encrypt Dictionary, Press 'Apply' at left side to apply change (1 alphabet only, input other than first letter will not be read):")
label_change_dict_title.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)


frame_change_dict_main = tk.Frame(root)
frame_change_dict_main.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

frame_change_dict_main_1 = tk.Frame(frame_change_dict_main)
frame_change_dict_main_2 = tk.Frame(frame_change_dict_main, bd=2, bg="#8D90FF")
label_blank_change_dict_main = tk.Label(frame_change_dict_main, text="   ")
frame_change_dict_main_1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
label_blank_change_dict_main.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
frame_change_dict_main_2.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

tk.Grid.columnconfigure(frame_change_dict_main, 0, weight=6)
tk.Grid.columnconfigure(frame_change_dict_main, 1, weight=1)
tk.Grid.columnconfigure(frame_change_dict_main, 2, weight=2)
tk.Grid.rowconfigure(frame_change_dict_main, 0, weight=1)

change_dictionary_label = {}
change_dictionary_entry = {}

c_dict_row_position = 0 
c_dict_column_position = 0
for n in dictionary_encryption:
    change_dictionary_label[n] = tk.Label(frame_change_dict_main_1, font=("Arial",  14), text= n + "→")
    change_dictionary_entry[n] = tk.Entry(frame_change_dict_main_1, font=("Arial",  14), width =1)
    change_dictionary_entry[n].insert(0, dictionary_encryption[n][0])
    change_dictionary_label[n].grid(row=c_dict_row_position, column=c_dict_column_position, sticky=tk.N+tk.S+tk.E+tk.W)
    change_dictionary_entry[n].grid(row=c_dict_row_position, column=c_dict_column_position+1, sticky=tk.N+tk.S+tk.E+tk.W)
    tk.Grid.rowconfigure(frame_change_dict_main_1, c_dict_row_position, weight=1)
    tk.Grid.columnconfigure(frame_change_dict_main_1, c_dict_column_position, weight=1)
    tk.Grid.columnconfigure(frame_change_dict_main_1, c_dict_column_position+1, weight=1)
    c_dict_column_position += 2
    if c_dict_column_position == 20:
        c_dict_column_position = 0
        c_dict_column_position_2 = 1
        c_dict_row_position += 1

label_apply_1 = tk.Button(frame_change_dict_main_2, font=("Arial",  14) ,text="Apply\nMethod 1", bd=3, activebackground="#AEFAFF", command=lambda:method_1_apply())
label_apply_1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
tk.Grid.rowconfigure(frame_change_dict_main_2, 0, weight=1)
tk.Grid.columnconfigure(frame_change_dict_main_2, 0, weight=1)

label_change_dict_title_2 = tk.Label(root, font=("Arial",  14) ,text="Method 2: Enter how many Alphabet to shift for normal a-z sequence.")
label_change_dict_title_2.grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W)


frame_change_dict_method_2 = tk.Frame(root)
frame_change_dict_method_2.grid(row=5, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

label_ask_swap_no = tk.Label(frame_change_dict_method_2, font=("Arial",  14) ,
    text="Method 2: Enter how many charater place to shift form normal a-z sequence.(-26 to 26)\n→ '-' for shift forward, '+' for backward, default is +1")
swap_no_entry = tk.Entry(frame_change_dict_method_2, font=("Arial",  14), width =2)
label_blank_frame_change_dict_method_2 = tk.Label(frame_change_dict_method_2, text="   ")
frame_button_apply_2 = tk.Frame(frame_change_dict_method_2, bd=2, bg="#8D90FF")
button_apply_2 = tk.Button(frame_button_apply_2, font=("Arial",  14) ,text="Apply\nMethod 2", bd=3, activebackground="#AEFAFF", command=lambda:method_2_apply())
label_blank_frame_change_dict_method_2 = tk.Label(frame_change_dict_method_2)

label_ask_swap_no.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
swap_no_entry.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
label_blank_frame_change_dict_method_2.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
frame_button_apply_2.grid(row=0, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
label_blank_frame_change_dict_method_2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
button_apply_2.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

tk.Grid.columnconfigure(frame_change_dict_method_2, 0, weight=3)
tk.Grid.columnconfigure(frame_change_dict_method_2, 1, weight=1)
tk.Grid.columnconfigure(frame_change_dict_method_2, 2, weight=3)


frame_original_text = tk.Frame(root)
frame_original_text.grid(row=6, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

label_original_text = tk.Label(frame_original_text, font=("Arial",  14), text="Original text:")
text_original_text = tk.Text(frame_original_text, font=("Arial",  14), height=5)
frame_button_process = tk.Frame(frame_original_text, bd=2, bg="#FF4141")
button_process = tk.Button(frame_button_process, font=("Arial",  14) ,text="Process", bd=3, activebackground="#FF4141", command=lambda:process())
frame_blank_original_text = tk.Label(frame_original_text, font=("Arial",  14), text="   ")
scrollbar_original_text_v = tk.Scrollbar(frame_original_text, orient=tk.VERTICAL)
scrollbar_original_text_v.config(command=text_original_text.yview)
text_original_text.configure(yscrollcommand = scrollbar_original_text_v.set)

label_processed_text = tk.Label(frame_original_text, font=("Arial",  14), text="Processed text:\n(Under current encryptor dictionary)")
text_processed_text = tk.Text(frame_original_text, font=("Arial",  14), height=5)
scrollbar_processed_text_v = tk.Scrollbar(frame_original_text, orient=tk.VERTICAL)
scrollbar_processed_text_v.config(command=text_processed_text.yview)
text_processed_text.configure(yscrollcommand = scrollbar_processed_text_v.set)
blank_processed_text = tk.Label(frame_original_text)
blank_processed_text_2 = tk.Label(frame_original_text)

label_original_text.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
text_original_text.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
scrollbar_original_text_v.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
frame_blank_original_text.grid(row=0, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
frame_button_process.grid(row=0, column=4)
button_process.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

tk.Grid.columnconfigure(frame_button_process, 0, weight=1)
tk.Grid.rowconfigure(frame_button_process, 0, weight=1)
tk.Grid.columnconfigure(frame_original_text, 0, weight=1)
tk.Grid.columnconfigure(frame_original_text, 1, weight=1)
tk.Grid.columnconfigure(frame_original_text, 2, weight=1)
tk.Grid.columnconfigure(frame_original_text, 3, weight=1)

blank_processed_text.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
blank_processed_text_2.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
label_processed_text.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
text_processed_text.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
scrollbar_processed_text_v.grid(row=2, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

tk.Grid.rowconfigure(frame_button_process, 1, weight=1)


frame_export_and_import = tk.Frame(root, bd=2, bg="#F8A700")
frame_export_and_import.grid(row=7, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
Button_import = tk.Button(frame_export_and_import, font=("Arial",  14), text="Import existing encryption dictionary (.txt)", command=lambda:import_txt_and_apply())
Button_export = tk.Button(frame_export_and_import, font=("Arial",  14), text="Export current decryption dictionary as .txt", command=lambda:export())

Button_import.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
Button_export.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

tk.Grid.columnconfigure(frame_export_and_import, 0, weight=1)
tk.Grid.columnconfigure(frame_export_and_import, 1, weight=1)
tk.Grid.rowconfigure(frame_export_and_import, 0, weight=1)

tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.rowconfigure(root, 1, weight=1)
tk.Grid.rowconfigure(root, 2, weight=1)
tk.Grid.rowconfigure(root, 3, weight=1)
tk.Grid.rowconfigure(root, 4, weight=1)
tk.Grid.rowconfigure(root, 5, weight=1)
tk.Grid.rowconfigure(root, 6, weight=1)
tk.Grid.rowconfigure(root, 7, weight=1)


#root.bind("<Configure>", font_resize)
root.iconbitmap('icon.ico')
root.mainloop()
