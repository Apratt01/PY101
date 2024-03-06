import re

def clean_up(sentence):
    new = re.sub(r'[^a-zA-Z\s]', ' ', sentence) # removes punctuation
    new = re.sub(r'[^\x00-\x7F]', '', new) # removes non-ascii characters
    new = re.sub(r' +', ' ', new) # removes consecutive spaces
    return new
        

print(clean_up("---what's my +*& line?") == " what s my line ") # True
print(clean_up("Καλωσήρθες") == " ")   # True