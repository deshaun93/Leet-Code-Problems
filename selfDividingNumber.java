class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> output =  new ArrayList<Integer>();
        int currentNumber; 
        int lastDigit;
        boolean numberIsSelfDividing;
        
        while(left <= right){
            currentNumber = left;
            numberIsSelfDividing = true;
            
            while (currentNumber != 0){
                lastDigit = currentNumber % 10;
                currentNumber/=10;
                
                if(lastDigit == 0 || !(left % lastDigit  == 0)){
                   numberIsSelfDividing = false;
                    break;
                   }
                                      
            }
            
            if(numberIsSelfDividing){
            output.add(left);    
            }
            
            left++;
            
        }
        return output;
    }
}


