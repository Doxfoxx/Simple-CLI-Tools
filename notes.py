print("Enter a note: ")
note = input()
open("PyNotes.txt", "a").write(note + "\n")
print("Note saved.")
