from collections import defaultdict
from collections.abc import dict_values
from typing import List, Any


class Solution:
    def groupAnagrams(self, strs: List[str]) -> dict_values[Any, list]:
        # m * nlog(n) --> sort and traverser
        # hashmap
        # key: count , value: list result
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

            # list cannot be key
            res[tuple(count)].append(str)
        return res.values()
