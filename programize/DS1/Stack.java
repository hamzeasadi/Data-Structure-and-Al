class Stack{
    int[] stack;
    int top = -1;
    int ssize;
    Stack(int ss){
        stack = new int[ss];
        ssize = ss;
    }

    boolean isEmpty(){
        return this.top<0;
    }

    boolean isFull(){
        return this.top>=this.ssize-1;
    }

    void push(int x){
        if(this.isFull())
            System.out.println("stack is full");
        else{
            this.top ++;
            this.stack[this.top] = x;
            System.out.println(x + " was added to stack successfully!");
        }
    }

    int pop(){
        if(this.isEmpty()){
            System.out.println("stack is empty");
            return -1;
        }
        else{
            int elem = this.stack[this.top];
            this.top -= 1;
            return elem;
            }
    }

    public static void main(String[] args){
        Stack mystack = new Stack(5);
        for(int i=0; i<7; i++)
            mystack.push(i);

        for(int i=0; i<mystack.ssize+2; i++){
            int item = mystack.pop();
            System.out.println(item);
        }

    }
}