class MinStack {
    private MinNode head;
    /** initialize your data structure here. */
    public MinStack() {
        head = null;
    }
    
    public void push(int val) {
        if(head == null) {
            head = new MinNode(val, null, val);
        } else {
            if(val < getMin()) {
                MinNode newNode = new MinNode(val, head, val);     
                head = newNode;
            } else {
                MinNode newNode = new MinNode(val, head, getMin());
                head = newNode;
            }
        }
    }
    
    public void pop() {
        head = head.getNext();
    }
    
    public int top() {
        return head.getVal();   
    }
    
    public int getMin() {
        return head.getMin();
    }
}

class MinNode {
    private int val;
    private int min; // smallest val in the MinStack when this node was inserted
    private MinNode next;
    
    public MinNode(int val, MinNode next, int min) {
        this.val = val;
        this.next = next;
        this.min = min;
    }
    
    public int getVal() {
        return this.val;
    }
    
    public MinNode getNext() {
        return this.next;
    }
    
    public int getMin() {
        return this.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
