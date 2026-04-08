# LinkedList.py

class LinkedList:
    pass

# ----------------------------
# Empty Linked List
# ----------------------------
class LinkedListEmpty(LinkedList):
    def __init__(self):
        pass

    # Convert to string
    def toString(self):
        return ""

    # Add value to front
    def addFirst(self, value):
        from LinkedList import LinkedListPopulated
        return LinkedListPopulated(value, self)

    # Remove value (nothing to remove)
    def remove(self, value):
        return self

    # Smallest element
    def smallest(self):
        raise Exception("Empty list has no smallest element")

    # Recursive simple sort
    def sortSimple(self):
        return self

    # Count unique elements in sorted list
    def uniq(self):
        return 0


# ----------------------------
# Non-empty Linked List
# ----------------------------
class LinkedListPopulated(LinkedList):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    # Convert to string
    def toString(self):
        return str(self.value) + " " + self.next.toString()

    # Add value to front
    def addFirst(self, value):
        return LinkedListPopulated(value, self)

    # Remove first occurrence of value
    def remove(self, value):
        if self.value == value:
            return self.next
        else:
            return LinkedListPopulated(self.value, self.next.remove(value))

    # Find smallest value recursively
    def smallest(self):
        if isinstance(self.next, LinkedListEmpty):
            return self.value
        else:
            return min(self.value, self.next.smallest())

    # Recursive selection sort
    def sortSimple(self):
        smallest_value = self.smallest()
        rest = self.remove(smallest_value)
        sorted_rest = rest.sortSimple()
        return sorted_rest.addFirst(smallest_value)

    # Count unique elements in sorted list
    def uniq(self):
        if isinstance(self.next, LinkedListEmpty):
            return 1
        if self.value == self.next.value:
            return self.next.uniq()
        else:
            return 1 + self.next.uniq()
