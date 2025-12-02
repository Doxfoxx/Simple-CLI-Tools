import datetime
print("Do you want to view or add notes? (view/add)")
choice = input()
if choice == "add":
    print("Enter a note: ")
    note = input()
    timestamp = datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")
    open("notes.txt", "a").write(timestamp + note + "\n")
    print("Note saved.")
elif choice == "view":
    print("Your notes:")
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            for note in notes:
                print(note.strip())
    except FileNotFoundError:
        print("No notes found.")
else:
    print("Invalid choice.")