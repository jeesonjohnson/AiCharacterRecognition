letters = "абвгдђежзијклљмнњопрстћуфхцчџш0123456789()"
alphabetMapper={}
for letterIndex in range(len(letters)):
    alphabetMapper[letters[letterIndex]] = letterIndex
print(alphabetMapper)