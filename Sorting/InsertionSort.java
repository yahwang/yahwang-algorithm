// 백준알고리즘 1427번
// https://www.acmicpc.net/problem/1427
import java.util.Scanner;

public class InsertionSort{
    public static void main(String[] args){
        String input;
        int temp, index;

        Scanner sc = new Scanner(System.in);
        input = sc.next();
        sc.close();
        int[] nums = new int[input.length()];
        for(int i=0;i<input.length();i++){
            nums[i] = Integer.parseInt(input.charAt(i)+"");
        }
        // 삽입 정렬 알고리즘
        for(int i=1;i<nums.length;i++){
            temp = nums[i];
            index = i-1;
            while(index>=0){
                if(nums[index] > temp){
                    nums[index+1] = nums[index];
                    index--;
                }
                else{
                    break;
                }
            }
            nums[index+1]=temp;

        }
        // 결과 출력
        for(int k=nums.length-1;k>-1;k--){
           System.out.print(nums[k]);
        }
    }
}