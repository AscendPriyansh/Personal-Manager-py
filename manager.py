import sys
import json
from datetime import datetime

if len(sys.argv) < 2 :
    print("Please Provide a command")
    sys.exit()

command = sys.argv[1]

def load_tasks() :
    with open('tasks.json', 'r') as f:
        return json.load(f)
    

def save_tasks(tasks) :
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def add_tasks(task) :
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task Added!")

def view_tasks() :
    tasks = load_tasks()
    
    for i, task in enumerate(tasks, 1) :
        print(f"{i}, {task}")

def delete_tasks(index) :
    tasks = load_tasks()

    try :
        tasks.pop(index-1)
        save_tasks(tasks)
        print("Task Deleted!")
    except :
        print("Invalid task number")

# CONTACT-CODE

def load_contacts() :
    with open("contacts.json", "r") as f:
        return json.load(f)
    
def save_contacts(contacts) :
    with open("contacts.json", "w") as f:
        json.dump(contacts ,f)

def add_contacts(name, number) :
    contacts = load_contacts()
    contacts[name] = number
    save_contacts(contacts)
    print("Contact Added!")

def view_contacts() :
    contacts = load_contacts()

    for name in contacts :
        print(f"{name} - {contacts[name]}") 

def search_contact(name) :
    contacts = load_contacts()

    if name in contacts :
        print(f"{name} - {contacts[name]}")
    else :
        print("Contact not found")

def delete_contact(name) :
    contacts = load_contacts()

    if name in contacts :
        del contacts[name]
        save_contacts(contacts)
        print("Contact Deleted!")
    else :
        print("Contact not found")

# NOTES-CODE

def load_notes() :
    with open("notes.json", "r") as f:
        return json.load(f)
    
def save_notes(notes) :
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def add_notes(note) :
    notes = load_notes()
    
    data = {
        "notes" : note,
        "created" : str(datetime.now())
    }

    notes.append(data)
    save_notes(notes)
    print("Note added")

def view_notes():
    notes = load_notes()

    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['notes']} ({note['created']})")

def delete_note(index) :
    notes = load_notes()

    try :
        del notes[index-1]
        save_notes(notes)
        print("Note deleted")
    except :
        print("Cannot find notes") 

if command == "add-task" :
    task = sys.argv[2]
    add_tasks(task)

elif command == "view-task" :
    view_tasks()

elif command == "delete-task" :
    index = int(sys.argv[2])
    delete_tasks(index)

elif command == "add-contact" :
    name = sys.argv[2]
    number = sys.argv[3]
    add_contacts(name, number)

elif command == "view-contact" :
    view_contacts()

elif command == "delete-contact" :
    name = sys.argv[2]
    delete_contact(name)

elif command == "search-contact" :
    name = sys.argv[2]
    search_contact(name)

elif command == "view-note" :
    view_notes()

elif command == "delete-note" :
    arg = int(sys.argv[2])
    delete_note(arg)

elif command == "add-note" :
    arg = sys.argv[2]
    add_notes(arg)

else :
    print("Unknown Command")
    print("""
Commands:
add-task
view-tasks
delete-task

add-contact
view-contacts
search-contact
delete-contact
""")
    

