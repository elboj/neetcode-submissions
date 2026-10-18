class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) #{key:[]}
        for str in strs:
            #sort the word
            key = "".join(sorted(str))
            groups[key].append(str)
        return list(groups.values())


# create an empty holder array
# Run a loop for the dataset
# for the first iteration if a keep
# 
#
# */

#[{a:1, c:1, t:1}]
        # {p:1, o:1, t:1, s:1}
#check inner loop to see if there's a match append to another, else add to holder
#[{a:1, c:1, t:1}, {p:1, o:1, t:1, s:1},]
        # {t:1, o:1, p:1, s:1}
#check inner loop to see if there's a match append to another, else add to holder
#[{a:1, c:1, t:1}, {p:1, o:1, t:1, s:1},{t:1, o:1, p:1, s:1}]


#result = [[{p:1, o:1, t:1, s:1},{t:1, o:1, p:1, s:1}]]
        