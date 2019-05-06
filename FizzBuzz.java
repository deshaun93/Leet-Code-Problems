class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> outputStrings = new ArrayList<String>();
        String outputString;
        
        for(int i = 1;i<=n;i++){
            if(i % 5 == 0 && i % 3 == 0){
                outputString = "FizzBuzz";
            }
            
            else if(i % 5 == 0){
                 outputString = "Buzz";
      
            }
            
            else if(i % 3 == 0){
                outputString = "Fizz";
            }
            
            else{
                outputString = String.valueOf(i);
            }
            
            outputStrings.add(outputString);
        }
          return outputStrings;
    }
  
}

