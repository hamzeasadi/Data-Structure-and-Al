package sortingSearching;

import java.util.Random;
import java.util.Arrays;

class BubbleSort{
	int arr_size;
	
	BubbleSort(int arr_size){
		this.arr_size = arr_size;
		
	}
	
	
	void buublesort() {
		int[] my_arr = new int[this.arr_size];
		Random random = new Random();
		for(int i=0; i<arr_size; i++)
			my_arr[i] = random.nextInt(100);
		System.out.println(Arrays.toString(my_arr));
		
		int tmp = 0;
		for(int i=0; i<this.arr_size; i++) {

			for(int j=0; j<this.arr_size-i-1; j++) {
				
				if(my_arr[j]>my_arr[j+1]) {
					tmp = my_arr[j];
					my_arr[j] = my_arr[j+1];
					my_arr[j+1] = tmp;
				}
			}
		}
		System.out.println(Arrays.toString(my_arr));
	}
	
}









public class Sort {
	
	
	public static void main(String[] args) {
		System.out.println("main function of main class");
		BubbleSort arr = new BubbleSort(5);
		arr.buublesort();
		
	}

}
