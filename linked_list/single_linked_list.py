
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False



class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        
        if self.head is None:
            self.head = item
            
        else:
            self.tail.next = item

        
        self.tail = item

        return

    def add_list_item_by_id(self, item, item_id):

        if item_id > self.list_length():
            print('узел добавлен в конец списка')
            self.add_list_item(item)
            return
        else:
            if not isinstance(item, ListNode):
                item = ListNode(item)

            current_id = 1
            current_node = self.head
            
            if item_id <=1:
                item.next = current_node
                self.head = item
                return
            else:
                
                while current_node is not None:
                    if current_id == item_id:
                        previous_node.next = item
                        item.next = current_node
                        return
                    previous_node = current_node
                    current_node = current_node.next
                    current_id += 1
        return

        
        

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def output_list(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def unordered_search(self, value):
        current_node = self.head
        node_id = 1
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id += 1
        return results

    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next
            current_id += 1
        return



    
    

