
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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

    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
            
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
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
                current_node.previous = item
                item.next = current_node
                self.head = item
                return
            else:
                
                while current_node is not None:
                    if current_id == item_id:
                        previous_node.next = item
                        item.previous = previous_node
                        item.next = current_node
                        current_node.previous = item
                        return
                    previous_node = current_node
                    current_node = current_node.next
                    current_id += 1
        return

    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if previous_node is not None:
                previous_node.next = next_node
                if next_node is not None:
                    next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                return

            current_node = next_node
            current_id += 1
        return
    



