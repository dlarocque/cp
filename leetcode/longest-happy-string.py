class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Return a string s, s.t.
        1. s only contains letters 'a','b','c'
        2. chars in s can not be repeated more than twice
        3. s at most a 'a's, b 'b's, c 'c's

        Ideas for building solution:
        Try inserting the characters that we have the most of at every step, until we can't insert any more characters.

        a = 0, b = 0, c = 1
        ccbccacc

        Pseudocode

        maxheap stores a,b,c
        s = ''

        max = False
        while heap is not empty
            if inserting the letter represented by the first int in the heap does not make our string unhappy
                append that character to our string
                update that counter in the heap if it's still greater than 0
                if it's 0, just remove it
                if our prev character was also the same char we just appended, set max = True, since we cant insert the character again without making the string unhappy

        return s

        """
        if a < 0 or b < 0 or c < 0:
            return ''

        heap = []
        if a: heapq.heappush(heap, (-a, 'a'))
        if b: heapq.heappush(heap, (-b, 'b'))
        if c: heapq.heappush(heap, (-c, 'c'))
        s = ''

        max_occ = False
        while len(heap) > 0:
            top = heap[0]
            # inserting top makes our string unhappy
            if s and max_occ and top[1] == s[-1]:
                if len(heap) > 1:
                    second = heap[1]
                    s += (second[1])
                    heap.remove(second)
                    if (-second[0])-1 > 0:
                        heapq.heappush(heap, (second[0]+1, second[1]))
                    max_occ = False
                else:
                    return s
            # we can happily insert top :)
            else:
                if s and s[-1] == top[1]:
                    max_occ = True
                s += top[1]
                heapq.heappop(heap)
                if (-top[0])-1 > 0:
                    heapq.heappush(heap, (top[0]+1, top[1]))

        return s
