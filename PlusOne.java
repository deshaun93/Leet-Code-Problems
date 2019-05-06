import java.util.ArrayList;
class Solution {
    
    public int[] plusOne(int[] digits) {
        int index = digits.length - 1;
        int val = digits[index];
    
        if(val == 9){
                 
            while(val == 9){
                   if(index == 0 && val == 9){
                       List<Integer> digitsArrayList = Arrays.stream(digits)                                                        .boxed()         
                                    .collect(Collectors.toList());
                     digitsArrayList.set(index,0);
                       val = 0;
                        digitsArrayList.add(0,0);
                       digits =  digitsArrayList.stream().mapToInt(x -> x).toArray();
                    }
            
                    else if(val == 9){
                        digits[index] = 0;
                        index--;
                        val = digits[index];
                            continue;
                    }
            
            }
                   
        }
        
        digits[index]++;
        
        return digits;
        }
           
    }

