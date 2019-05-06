class Solution {
    public int[] sortArrayByParity(int[] A) {
        
        int evenIndex = 0;
        int oddIndex = A.length - 1;
        int[] resultArray  = new int[A.length];
        
        for(int integer:A){
            if(integer % 2 == 0){
                resultArray[evenIndex++] = integer;
            }
            
            else{
                resultArray[oddIndex--] = integer;
            }
        }
        return resultArray;
    }
}