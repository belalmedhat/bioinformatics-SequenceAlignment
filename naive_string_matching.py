#naive string matching algorithm
def match(text, pattern):
    #list of occurences for the patter we are searching for inside text
    result = [];
    #loop iterator refer to current character in text
    i = 0;
    #loop over text character by character
    while i < len(text) - len(pattern):
        #if first character of both text and pattern matches then check the rest of the pattern
        if pattern[0] == text[i]:
            '''loop over all characters inside text starting from 
            index i to index i + len(patter) - 1
            to make sure that all characters of pattern 
            exist inside text starting at index i
            '''
            for j in range(0, len(pattern)):
                '''if single character mismatches 
                then break and search for the pattern 
                starting from next character inside text
                '''
                if pattern[j] != text[i+j]:
                    break;
                if j == len(pattern) - 1:
                    '''if all characters matches then 
                    append to result the starting 
                    position of the found pattern inside text
                    '''
                    result.append([i, i+len(pattern) - 1]);
        #increment i
        i+= 1;
    #if nothing is found then set length to zero
    if len(result) == 0:
        result.insert(0, 0);
    else:
        #add number of found patterns to the start of list "result"
        result.insert(0, len(result));
    #add the string pattern at the start of list "result"
    result.insert(0, pattern);
    return result;

sequence = "ggccggcatcgtgtttacctagtctgatcgtagtcgatgct";
result = match(sequence, "gg");
print(result);
