class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        assert 0 <= x <= 2**31 - 1
        #if x==0:
          #  return 0
        #guess=x
        #while True:
         #   new_guess=(guess+x/guess)/2
          #  if abs(new_guess-guess)<1e-6:
           #     return int(new_guess)
            #guess=new_guess
        if x == 0:
            return 0
        
        guess = x
        
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        
        return guess
