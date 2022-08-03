

from typing import List

class Solution:

    def find_area(self, w:int, h:int) -> int:
        return w*h

    def maxArea(self, H:List[int]) -> int:
        left = 0
        right = len(H) - 1
        maxx = 0
        c = 0

        while left < right:
            c += 1
            w = right - left
            h = min([H[left], H[right]])
            area = self.find_area(w, h)
            
            print(c , left, right, [H[left], H[right]],  w, h, area)
            
            if area > maxx: 
                maxx = area
            
            if H[left] < H[right]: 
                left += 1
            else:
                right -= 1
        print(c) 
        return maxx


if __name__ == '__main__':
    H = [1, 8, 6, 2, 5, 4, 8, 3, 7] 
    
    s = Solution()
    maxx = s.maxArea(H=H)
    print( maxx)
