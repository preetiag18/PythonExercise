import json
data = json.load(open("dictionary.json"))
def translate(w):
  w = w.lower()
  if w in data:
    return data[w]
  else:
    return "The word doesn't exist.please double check it"  


word = input("Enter word:")
print(translate(word))