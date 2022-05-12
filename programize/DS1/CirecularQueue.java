import javax.lang.model.util.ElementScanner14;

public class CirecularQueue{
    int q_size = 5;
    int front, rear;
    int queue[] = new int[q_size];

    CirecularQueue(){
        front = -1;
        rear = -1;
    }

    boolean isFull(){
        if (front == 0 && rear == q_size -1){
            if (front==rear+1)
                return true;
        }
        return false;
    }

    boolean isEmpty(){
        if (front==-1){
            return true;
        }
        return false;
    }

    void enqueue(int element){
        if (isFull()){
            System.out.println("Queue is full");
        }
        else{
            if (front==-1)
                front=0;
            rear = (rear + 1)%q_size;
            queue[rear] = element;
            System.out.println("Inseretd " + element);
        }
    }

    int dequeue(){
        int element;
        if (isEmpty()){
            System.out.println("Queue is empty");
            return -1;
        }
        else{
            element = queue[front];
            if (front==rear){
                rear=-1;
                front=-1;
            }

            else
            front = (front+1)%q_size;

        return element;

        }
    
    }

   public static void main(String[] args) {
    CirecularQueue q = new CirecularQueue();
    q.enqueue(10);
    q.enqueue(4);
    q.enqueue(5);

    for(int i=0; i< 5; i++){
        q.dequeue();
    }

    }



}