''' Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid 
(2010) and After Earth (2013). Jaden is also known for some of his philosophy
 that he delivers via Twitter. When writing on Twitter, he is known for almost
  always capitalizing every word. For simplicity, you'll have to capitalize each 
  word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized in 
the same way he originally typed them.
'''


def to_jaden_case(string):
    # make list words across spaces 
    x = string.split()
    # change first letter on big
    x1 = []
    for i in x:
        i = i[0].upper() + i[1:]
        x1.append(i)
    # make string from list
    mystr = ' '.join(x1)
    # return string
    return mystr
    # watch another decision