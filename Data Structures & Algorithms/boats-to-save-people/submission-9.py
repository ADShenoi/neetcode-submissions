class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0 
        l, r = 0, len(people)-1

        while l <= r:
            print(people[l], people[r])
            if people[l] + people[r] > limit:
                print('greater')
                count += 1
                r -=1
            else:
                print('lower or equal')
                count += 1
                l += 1
                r -= 1
            print(l, r, count)
        return count