class LinkedList{
    constructor(val){
        this.head = {
            val:val,
            next:null
        }
        this.tail = this.head;
        this.length = 1;
    }
    append(val){
        this.head = {
            val:val,
            next:this.head
        }
        
    }
}