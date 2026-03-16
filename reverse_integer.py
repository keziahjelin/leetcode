class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        assert -2**31 <= x <= 2**31 - 1
        is_negative=x<0
        strg=str(abs(x))
        list1=list(strg)
        list1.reverse()
        join="".join(list1)
        op=int(join)
        if is_negative:
            op=-op
        if op < -2**31 or op > 2**31 - 1:
            return 0
        return op
