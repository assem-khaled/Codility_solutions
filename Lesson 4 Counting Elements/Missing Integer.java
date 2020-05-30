import java.util.*;


class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 11
        boolean flag = false;
        Arrays.sort(A);
        int i = 0;
        for (int s = 1; s<A.length+2 ;s++)
        {
            
            for(;i<A.length;i++)
            {
                if (s == A[i])
                {
                    flag = true;
                    break;
                }
            }
            if (flag ==false)
            {
                return s;
            }
            flag = false;
        }
        //if not found
        return -1;
    }
}