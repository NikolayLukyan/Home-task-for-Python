print('Enter your string for writing in a file.\nIf You want to close the file enter empty string.')
with open('my_file.txt', 'w', encoding="utf-8") as favorite_file:
    while line := input() != ' ':
      favorite_file.write(f"{line}\n")
