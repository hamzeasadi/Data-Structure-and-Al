package sortingSearching;
import java.util.*;


interface Polygon{
	
	void getArea();
	
	default void getPerimeter(int ...sides) {
		int sum = 0;
		for(int side:sides)
			sum += side;
		
		System.out.println("perimeter is: "+sum);
	}
	
}



class Triangle implements Polygon{
	
	private int a, b, c;
	private double s, area;
	   
	Triangle(int a, int b, int c){
		this.a = a;
		this.b = b;
		this.c = c;	
	}
	
	
	
	public void getArea() {
		s = (double) (a + b + c)/2;
		area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
		System.out.println("Area: " + area);
	}
}

class SelectSort {
	
public static void main(String[] args) {
	
	Triangle teri = new Triangle(1, 2, 3);
	teri.getArea();
	teri.getPerimeter(1, 2, 3);		
}

}
