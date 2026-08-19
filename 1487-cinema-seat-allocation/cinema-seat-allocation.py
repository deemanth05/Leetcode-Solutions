class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reservedSeats.sort()

        max_groups = 0
        processed_rows = 0

        i = 0
        m = len(reservedSeats)

        while i<m:
            current_row = reservedSeats[i][0]
            processed_rows +=1

            left_valid = True
            right_valid = True
            middle_valid = True

            while i<m and reservedSeats[i][0] == current_row:
                seat = reservedSeats[i][1]

                if 2<= seat <= 5:
                    left_valid = False
                if 4 <= seat <= 7:
                    middle_valid = False
                if 6 <= seat <= 9 :
                    right_valid = False

                i+=1

            if left_valid and right_valid:
                max_groups +=2
            elif left_valid or middle_valid or right_valid :
                max_groups +=1

        max_groups += (n- processed_rows) * 2
        return max_groups

        
        
