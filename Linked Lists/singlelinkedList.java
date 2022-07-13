public class SinglyLinkedListTest {
    public static void main(String[] args) {
        SinglyLinkedList linkedList = new SinglyLinkedList();
 
        linkedList.addToEnd("1");
        linkedList.addToEnd("2");
        linkedList.addToEnd("3");
        linkedList.addToEnd("4");
        linkedList.addToEnd("5");
        
        System.out.println("linkedlist: " + linkedList);
        System.out.println("linkedlist size: " + linkedList.size());
        
        linkedList.reverse();
        System.out.println("linkedList.reverse(): " + linkedList);
        
        linkedList.reverse();
        System.out.println("linkedList.reverse(): " + linkedList);
        
        linkedList.add(10, 0);
        System.out.println("linkedList.add(10, 0): " + linkedList);
        
        linkedList.add(20, 1);
        System.out.println("linkedList.add(20, 1): " + linkedList);
        
        linkedList.add(30, 5);
        System.out.println("linkedList.add(30, 5): " + linkedList);
        
        System.out.println("lList.nthNodeFromEnd(3): " + linkedList.nthNodeFromEnd(3).toString());
    }
}
 
class SinglyLinkedList {
    // reference to the head node.
    private Node head;
    private int listCount;
    
    public Node getHead() {
    	return head;
    }
 
    // LinkedList constructor
    public SinglyLinkedList() {
        // this is an empty list, so the reference to the head node
        // is set to a new node with no data
//        head = new Node(null);
    	head = null;
        listCount = 0;
    }
 
    public void add(Object data)
    // appends the specified element to the end of this list.
    {
	if (head == null) {
		head = new Node(data);
	}
	else {
		Node newNode = new Node(data);
		Node current = head;
		
		while (current.getNext() != null) {
			current = current.getNext();
		}
		
		current.setNext(newNode);
	}
	
        listCount++;// increment the number of elements variable
    }
    
    public void addToFront(Object data) {
    	Node newNode = new Node(data);
    	
    	if (head == null) {
    		head = newNode;
    	}
    	else {
    		newNode.setNext(head);
    		head = newNode;
    	}
    	
    	listCount++;
    }
    
    public void addToEnd(Object data) {
    	Node newNode = new Node(data);
    	
    	if (head == null) {
    		head = newNode;
    	}
    	else {
	    	Node current = head;
	    	
	    	// traverse to a node pointing to null
	    	while (current.getNext() != null) {
	    		current = current.getNext();
	    	}
	    	
	    	current.setNext(newNode);
    	}
    	
    	listCount++;
    }
    
    public void reverse() {
    	Node current = head;
    	Node previous = null;
    	
    	while (current != null) {
    		Node next = current.getNext();
    		current.setNext(previous); // reverse the link
    		
    		// move current and previous node by 1 node
    		previous = current;
    		current = next;
    	}
    	
    	head = previous;
    }
 
    public void add(Object data, int index)
    // inserts the specified element at the specified position in this list
    // index is 0 based.
    {
        Node newNode = new Node(data);
        
        // insert to front
        if (index == 0) {
        	newNode.setNext(head);
        	head = newNode;
        }
        else {
        	// traverse to prior to index
        	Node current = head;
        	
        	for (int i = 0; i < index - 1; i ++) {
        		current = current.getNext();
        	}
        	
        	newNode.setNext(current.getNext());
        	current.setNext(newNode);
        }
        
        listCount++;// increment the number of elements variable
    }
 
    public Object get(int index)
    // returns the element at the specified position in this list.
    {
        // index must be 1 or higher
        if (index <= 0)
            return null;
 
        Node current = head.getNext();
        for (int i = 1; i < index; i++) {
            if (current.getNext() == null)
                return null;
 
            current = current.getNext();
        }
        return current.getData();
    }
 
    public boolean remove(int index)
    // removes the element at the specified position in this list.
    {
        // if the index is out of range, exit
        if (index < 1 || index > size())
            return false;
 
        Node current = head;
        for (int i = 1; i < index; i++) {
            if (current.getNext() == null)
                return false;
 
            current = current.getNext();
        }
        current.setNext(current.getNext().getNext());
        listCount--; // decrement the number of elements variable
        return true;
    }
 
    public int size()
    // returns the number of elements in this list.
    {
        return listCount;
    }
 
    public String toString() {
        Node current = head;
        String output = "";
        
        while (current != null) {
            output += "[" + current.getData().toString() + "]";
            current = current.getNext();
        }
        
        return output;
    }
    
    // http://www.algo-faq.com/Linked-List/Find-the-nth-node-from-end-of-a-linked-list.php
    public Object nthNodeFromEnd( int n )
    {
    	// First we determine the length of the linked list
    	int length = 0 ;
    	
    	Node iterator = head;
    	
    	while( iterator != null )
    	{
    		length++;
    		iterator = iterator.next;
    	}
    	
    	if ( length < n )
    	{
    		// n is larger than the length of linked list 
    		return null ;
    	}
    		
    	// Now we determine the required position 
    	
    	int position = length - n + 1 ; 
    	
    	// Now we start iterating the linked list again 
    	// this time till we reach the required position
    	
    	iterator = head;
    	
    	int count = 1;
    	
    	while ( count < position )
    	{
    		iterator = iterator.next; 
    		count++ ;
    	}
    	
    	return iterator.getData();
    }
    
    // http://www.algo-faq.com/Linked-List/Find-the-nth-node-from-end-of-a-linked-list.php
    // find nth node based on distance between pointer1 and pointer2
    public Object nthNodeFromEndSingleIteration(int n)
    {
    	Node pointer1 = head;
    	Node pointer2 = head;
    	int count = 0;
    	
    	while(count < n) {
    		if (pointer2 == null) {
    			// Not enough nodes , n greater than size of linked list
    			return null;
    		}
    		else {
    			pointer2 = pointer2.getNext();
    			count++;
    		}
    	}
    	
    	while (pointer2 != null) {
    		pointer1 = pointer1.getNext();
    		pointer2 = pointer2.getNext();
    	}
    	
    	// returning the required node
    	return pointer1;
    }
 
    class Node {
        // reference to the next node in the chain,
        // or null if there isn't one.
        Node next;
        // data carried by this node.
        // could be of any type you need.
        Object data;
 
        // Node constructor
        public Node(Object dataValue) {
            next = null;
            data = dataValue;
        }
 
        // another Node constructor if we want to
        // specify the node to point to.
        public Node(Object dataValue, Node nextValue) {
            next = nextValue;
            data = dataValue;
        }
 
        // these methods should be self-explanatory
        public Object getData() {
            return data;
        }
 
        public void setData(Object dataValue) {
            data = dataValue;
        }
 
        public Node getNext() {
            return next;
        }
 
        public void setNext(Node nextValue) {
            next = nextValue;
        }
    }
}
