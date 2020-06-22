import os
# letters = "ਓ ਅ ੲ ਸ ਹ ਕ ਖ ਗ ਘ ਙ ਚ ਛ ਜ ਝ ਞ ਟ ਠ ਡ ਢ ਣ ਤ ਥ ਦ ਧ ਨ ਪ ਫ ਬ ਭ ਮ ਯ ਰ ਲ ਵ ੜ ਸ਼ ਖ ਗ਼ ਜ਼ ਫ਼ ਲ਼"
lettersModified = "а б в г д ђ е ж з и ј к л љ м н њ о п р с т ћ у ф х ц ч џ ш 0 1 2 3 4 5 6 7 8 9 ( )"
print(len(lettersModified.split(" ")))
for element in lettersModified.split(" "):
    os.makedirs(element)
