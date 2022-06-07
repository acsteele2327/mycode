#! /usr/bin/env python3

#save a users input to the variable char_name

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

char_name=input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n")
char_name.lower()
char_name.capitalize()
char_stats=input("What statistics do you want to know about? (real name, powers, archenemy)\n")
char_stats.lower()

#print(f"{char_name}'s {char_stats} is: {marvelchars[char_name][char_stats]}")
print(char_name)
