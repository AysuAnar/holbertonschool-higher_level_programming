class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print(f"Popped {item} from the list.")
        else:
            item = super().pop(index)
            print(f"Popped {item} from the list at index {index}.")
        return item

# Testing the implementation
vlist = VerboseList()

# Testing append
vlist.append(1)
vlist.append(2)

# Testing extend
vlist.extend([3, 4, 5])

# Testing remove
vlist.remove(3)

# Testing pop
vlist.pop()
vlist.pop(0)

