import string
def pig_it(text):
    position = []
    character = []

    for idx, letter in enumerate(text):
        if(letter in string.punctuation):
            position.append(idx)
            character.append(letter)
            text = text[:idx]+""+text[idx+1:]

    words = []
    cur_pos = 0
    end_pos = 0
    for word in text.split(" "):
        cur_pos += len(word)+1
        if len(word) > 0:
            word = word[1:]+word[0]+'ay'
            end_pos += len(word)+1
            words.append(word)

        else:
            words.append(word)
            end_pos += len(word)+1

        for idx, pos in enumerate(position):
            if pos == cur_pos:
                position[idx]= end_pos

    text = " ".join(words)
    for idx, pos in enumerate(position):
        text = text[:pos]+ character[idx]+ text[pos+1:]

    return(text)
