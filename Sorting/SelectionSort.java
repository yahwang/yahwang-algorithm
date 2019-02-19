// 백준알고리즘 1427번
// https://www.acmicpc.net/problem/1427
import java.util.Scanner;

public class SelectionSort{
    public static void main(String[] args){
        String input;
        int minVal, minIndex;

        Scanner sc = new Scanner(System.in);
        input = sc.next();
        sc.close();
        int[] nums = new int[input.length()];
        for(int i=0;i<input.length();i++){
            nums[i] = Integer.parseInt(input.charAt(i)+"");
        }
        // 선택 정렬 알고리즘
        for(int j=0;j<nums.length-1;j++){
            minVal = nums[j];
            minIndex=j;
            for(int k=j+1;k<nums.length;k++){
                if(nums[k]<minVal){
                    minVal=nums[k];
                    minIndex = k;
                }
            }
            nums[minIndex] = nums[j];
            nums[j] = minVal;
        }
        // 결과 출력
        for(int k=nums.length-1;k>-1;k--){
            System.out.print(nums[k]);
        }
    }
}