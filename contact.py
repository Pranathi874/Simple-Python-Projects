import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


contacts = []


def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")

    if name and phone and email and address:
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")
        display_contacts()
    else:
        messagebox.showerror("Error", "All fields are required!")


def display_contacts():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def search_contact():
    search_term = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    if search_term:
        found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term.lower() in contact['phone']]
        if found_contacts:
            contact_listbox.delete(0, tk.END)
            for contact in found_contacts:
                contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        else:
            messagebox.showinfo("No Results", "No contacts found with that name or phone number.")


def update_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        selected_contact = contacts[selected_contact_index[0]]
        new_name = simpledialog.askstring("Update", f"Enter new name (current: {selected_contact['name']}):")
        new_phone = simpledialog.askstring("Update", f"Enter new phone number (current: {selected_contact['phone']}):")
        new_email = simpledialog.askstring("Update", f"Enter new email (current: {selected_contact['email']}):")
        new_address = simpledialog.askstring("Update", f"Enter new address (current: {selected_contact['address']}):")

        
        if new_name and new_phone and new_email and new_address:
            selected_contact['name'] = new_name
            selected_contact['phone'] = new_phone
            selected_contact['email'] = new_email
            selected_contact['address'] = new_address
            messagebox.showinfo("Success", "Contact updated successfully!")
            display_contacts()
        else:
            messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")


def delete_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
        if confirm:
            contacts.pop(selected_contact_index[0])
            messagebox.showinfo("Success", "Contact deleted successfully!")
            display_contacts()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")


root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")


frame = tk.Frame(root)
frame.pack(pady=10)

add_button = tk.Button(frame, text="Add Contact", width=20, command=add_contact)
add_button.grid(row=0, column=0, padx=10)

search_button = tk.Button(frame, text="Search Contact", width=20, command=search_contact)
search_button.grid(row=0, column=1, padx=10)

update_button = tk.Button(frame, text="Update Contact", width=20, command=update_contact)
update_button.grid(row=0, column=2, padx=10)

delete_button = tk.Button(frame, text="Delete Contact", width=20, command=delete_contact)
delete_button.grid(row=0, column=3, padx=10)


contact_listbox = tk.Listbox(root, width=70, height=15)
contact_listbox.pack(pady=20)


root.mainloop()
