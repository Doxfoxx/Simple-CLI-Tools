import datetime
print("Enter a note: ")
note = input()
timestamp = datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")
open("notes.txt", "a").write(timestamp + note + "\n")
print("Note saved.")
