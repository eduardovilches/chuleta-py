def printLinkedList(head):
    if head  is None:
        return
        
    print(head.data)
    
    return printLinkedList(head.next)
    
