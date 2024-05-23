import unicodedata

def SansUtfDict(splchar=False):
    
    """Generates a dictionary mapping Sanskrit characters to their corresponding UTF-16 code points.

    Args:
        splchar (bool, optional): Whether to include special characters
            (space, digits, colon, semicolon, and characters from U+0041 to U+005A)
            in the dictionary. Defaults to False.

    Returns:
        dict: A dictionary mapping Sanskrit characters to their UTF-16 code points.
    """
    sansdict = {}

    for i in range(0x900, 0x97F): 
        character = chr(i) 
        name = unicodedata.name(character, "") 
        if len(name) > 0: 
            sansdict[str(f"{character}")] = str(f"{i:04X}") 
    if splchar:
        for i in list(range(0x0020, 0x0030))+list(range(0x003A, 0x0041)): 
            character = chr(i) 
            name = unicodedata.name(character, "") 
            if len(name) > 0: 
                sansdict[str(f"{character}")] = str(f"{i:04X}") 
    return sansdict


# Define function transliterating text
def Transliterate(text, translit_dict):
    """Transliterates text from one character set to another.

    Args:
        text (str): The text to transliterate. Text should be in sanskrit
        translit_dict (dict): A dictionary mapping characters in the source language to characters in the target language.

    Returns:
        list: A list of characters in the target language.

    """
    new_word = []
    for letter in text:
        new_letter = ''
        if letter in translit_dict:
            new_letter = translit_dict[letter]
            new_word.append(new_letter)
        else:
            print(f"chr:{letter} not found in the dictionary")
    return new_word
    

def UtfListDecoder(utf_list, sep="space"):
    """Decodes a list of UTF-8 code points into a Unicode string.

    Args:
        utf_list: A list of integers representing UTF-8 code points.
        sep: The separator to use between code points in the output string.
              Defaults to "space" or "plus".

    Returns:
        A Unicode string decoded from the code points.

    Raises:
        ValueError: If the separator is not a valid Unicode code point.
    """
    seps = {"space":"0020","plus":"002b"}
    if sep=="space":
        if len(utf_list)>0:
            conn = "\\u" + "\\u".join(utf_list)
        else:
            conn = "\\u{seps[sep]}"
        return conn.encode().decode("unicode-escape")
    else:
        print("select space or plus as separator")
    
