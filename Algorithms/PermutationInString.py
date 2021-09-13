class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a dictionary for storing the frequency of letters in s1 (which is the smaller of the two strings)
        # NOTE: the way the dictionary is functioning is that the substring serves as the string, and everytime we add one to it that is the value
        dict = {}
        
        # iterate through the shorter string
        for i in s1:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                
        m = len(s1)
        
        # now we create a window that will compare all the possible substrings of s2 with size equal to that of s1
        window = s2[0:m]
        
        # now we create another dictionary fo storing the frequecy of all the substrings in s2 that we will compare with the frequency in dict or s1
        map = {}
        
        # iterate through window
        for x in window:
            if x not in map:
                map[x] = 1
            else:
                map[x] += 1
        # then there does exist a permutation of s1 in s2
        if map == dict:
            return True
        for i in range(1,len(s2)):
            if(m+i-1) >= len(s2):
                break
                
            # update the window array everything we iterate through
            window = s2[i:m+i]
            # if an element is only equal to 1, remove it
            if map[s2[i-1]] == 1:
                del map[s2[i-1]]
            else:
                # decrement the left out element
                map[s2[i-1]] -= 1
                
            # now we check if the next letter already exists, if it does increase the count of if not then add a new entry into the dictionary 
            if s2[m+i-1] not in map:
                map[s2[m+i-1]] = 1
            else:
                map[s2[m+i-1]] += 1
                
            # check that each substring of s2 and see if they are equal if so then return true
            if map == dict:
                return True
        return False
        
        