print("Enter a note: ")
note = input()
open("note.txt", "a").write(note + "\n")
print("Note saved.")
