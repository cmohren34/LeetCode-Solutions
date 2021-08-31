def reverseWords(s: str) -> str:
    # note that split will auto seperate words in a string

    result = []
    final_str = ''

    for x in s.split():
        # reverse every word in s and append it in order to 
        # maintain its order
        result.append(x[::-1])

    final_str = ' '.join(result)
    
    return final_str

s = "Apple's and Oranges"

print("\n",reverseWords(s),"\n")

    