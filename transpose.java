class Solution {
    public int[][] transpose(int[][] A) {
        // Case when the length is 1
        // each row may not be the same lenght?
        int[][] finalMatrix = new int[A[0].length][A.length];
        int columnIndex = 0;
        for(int[] row:A){
            for(int rowIndex = 0;rowIndex<row.length;rowIndex++){
                finalMatrix[rowIndex][columnIndex] = row[rowIndex];
            }
            columnIndex++;
        }
        
        return finalMatrix;
        
        
    }
}