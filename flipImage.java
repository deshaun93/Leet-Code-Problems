class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        for(int i = 0; i<A.length;i++){
        A[i] = reverseAndInvertArray(A[i]);
        }
        return A;
    }
    
    
    public int[]  reverseAndInvertArray(int[] array){
        if(array.length == 1){
            array[0] = invertValue(array[0]);
            return array;
        }
                
        int pocket;
        int leftPointer = 0;
        int rightPointer = array.length-1;
        int[] result = new int[array.length];
        
        while(leftPointer < rightPointer){

            pocket = array[rightPointer];
            result[rightPointer] = invertValue(array[leftPointer]); 
            rightPointer--;
            result[leftPointer] = invertValue(pocket);
            leftPointer++;

        }
        
        if(leftPointer == rightPointer){
            result[leftPointer] = invertValue(array[leftPointer]);
   
        }
        
        return result;
        
    }
    
    public int invertValue(int val){
        return val == 1 ? 0:1;
    }
    
}