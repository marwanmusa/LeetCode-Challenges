class Solution:
    """
    Task:
        A binary watch has 4 LEDs on the top to represent the hours (0-11),
        and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one,
        with the least significant bit on the right.

        For example, the below binary watch reads "4:51".

        Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM),
        return all possible times the watch could represent. You may return the answer in any order.

        The hour must not contain a leading zero.

        For example, "01:00" is not valid. It should be "1:00".
        
        The minute must consist of two digits and may contain a leading zero.

        For example, "10:2" is not valid. It should be "10:02".
    """
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        kq = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1')+bin(j).count('1') == turnedOn:
                    if j < 10:
                        kq.append(str(i)+":0"+str(j))
                    else:
                        kq.append(str(i)+":"+str(j))
        return kq