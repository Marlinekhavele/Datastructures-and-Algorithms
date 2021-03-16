"""Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0."""


import collections
class Solution:
    def bfs(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        q.append(start)
        visited = set()
        while q:
            index = q.popleft()
            visited.add(index)
            if arr[index] == 0:
                return True
            pos1 = index + arr[index]
            if pos1 not in visited and pos1 < len(arr):
                q.append(pos1)
            pos2 = index - arr[index]
            if pos2 not in visited and pos2 >= 0:
                q.append(pos2)
        return False

    def dfs(self, arr: List[int], start: int) -> bool:
        q = list()
        q.append(start)
        visited = set()
        while q:
            index = q.pop()
            visited.add(index)
            if arr[index] == 0:
                return True
            pos1 = index + arr[index]
            if pos1 not in visited and pos1 < len(arr):
                q.append(pos1)
            pos2 = index - arr[index]
            if pos2 not in visited and pos2 >= 0:
                q.append(pos2)
        return False

    def canReach(self, arr: List[int], start: int) -> bool:
        return self.bfs(arr, start)
