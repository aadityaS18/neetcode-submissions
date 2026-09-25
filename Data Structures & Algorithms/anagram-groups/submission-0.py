class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)# hashmap: key = tuple(count), value = list of anagrams
        for word in strs:
            count=[0]*26 #create frequency array for 'a' to 'z'
            for char in word:
                count[ord(char) - ord('a')] += 1   # increment count for each letter


            anagrams[tuple(count)].append(word)#convert list to tuple because lists can't be used as hashmap keys

        return list(anagrams.values())    
        