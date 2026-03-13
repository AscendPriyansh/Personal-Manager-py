# 📒 Personal Manager CLI (Python)

A simple **Command Line Personal Manager** built with Python that allows you to manage **tasks, contacts, and notes** directly from the terminal.

This project was built to practice Python fundamentals such as **file handling, dictionaries, lists, functions, CLI arguments, and JSON data storage**.

---

# 🚀 Features

### ✅ Task Manager

* Add tasks
* View all tasks
* Delete tasks

### 📇 Contact Manager

* Add contacts
* View contacts
* Search contacts
* Delete contacts

### 📝 Notes Manager

* Add notes
* View notes
* Delete notes
* Automatically stores note creation time

---

# 📂 Project Structure

```
personal-manager/
│
├── manager.py
├── tasks.json
├── contacts.json
├── notes.json
```

* **manager.py** → Main CLI application
* **tasks.json** → Stores tasks
* **contacts.json** → Stores contacts
* **notes.json** → Stores notes

---

# ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/yourusername/personal-manager.git
```

2. Navigate to the project folder

```
cd personal-manager
```

3. Make sure Python is installed.

Check version:

```
python --version
```

---

# ▶️ Usage

Run commands using:

```
python manager.py <command>
```

---

# 📌 Task Commands

Add a task:

```
python manager.py add-task "Finish Python practice"
```

View tasks:

```
python manager.py view-task
```

Delete a task:

```
python manager.py delete-task 1
```

---

# 📌 Contact Commands

Add a contact:

```
python manager.py add-contact Kevin 9876543210
```

View contacts:

```
python manager.py view-contact
```

Search contact:

```
python manager.py search-contact Kevin
```

Delete contact:

```
python manager.py delete-contact Kevin
```

---

# 📌 Notes Commands

Add note:

```
python manager.py add-note "Learn Python dictionaries"
```

View notes:

```
python manager.py view-note
```

Delete note:

```
python manager.py delete-note 1
```

---

# 💾 Data Storage

All data is stored locally using **JSON files**:

* `tasks.json`
* `contacts.json`
* `notes.json`

This allows the program to **persist data between runs**.

---

# 🧠 Concepts Practiced

This project demonstrates core Python fundamentals:

* Variables & Data Types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* File Handling
* JSON Data Storage
* Command Line Arguments (`sys.argv`)
* Error Handling
* Working with `datetime`

---

# 📈 Future Improvements

Possible upgrades:

* Edit tasks or notes
* Mark tasks as completed
* Better CLI command parser
* Export data
* Build a GUI version
* Convert into a REST API using Python frameworks

---

# 👨‍💻 Author

**Priyansh Tiwari**

Built as a practice project while revisiting Python fundamentals.
