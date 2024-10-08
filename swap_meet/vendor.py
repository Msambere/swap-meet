class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id is item_id:
                return item
        return None

    #Wave 3

    def swap_items(self, other_vendor, my_item, their_item):
        '''
        1.Check if both items are in the each inventories
        2.Remove my_item from this vendor and add it to other_vendor
        3.Remove their_item from other_vendor and add it to this vendor
        '''
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        other_vendor.add(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        self.remove(my_item)
        return True

    #Wave 4

    def swap_first_item(self, other_vender):
        if not self.inventory or not other_vender.inventory:
            return False
        self.inventory[0], other_vender.inventory[0] = other_vender.inventory[0], self.inventory[0]
        return True

    #Wave 6
    def get_by_category(self, category):
        items = []
        items = [item for item in self.inventory if item.get_category() is category]
        # for item in self.inventory:
        #     if item.get_category() is category:
        #         items.append(item)
        return items
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None
        best = items[0]
        for item in items:
            if item.condition > best.condition:
                best = item
        return best
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        return self.swap_items(
            other_vendor, 
            self.get_best_by_category(their_priority), 
            other_vendor.get_best_by_category(my_priority)
            )
    # Enhancements

    def get_by_age(self):
        if len(self.inventory) == 0:
            return False
        newest = self.inventory[0]
        for item in self.inventory:
            if item.age < newest.age:
                newest= item
        return newest
    
    def get_newest_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return False
        newest = items[0]
        for item in items:
            if item.age < newest.age:
                newest=item
        return newest

    def swap_by_newest(self, other_vendor):
        return self.swap_items(other_vendor, self.get_by_age(), other_vendor.get_by_age())
        
    def swap_newest_by_category(self, other_vendor, my_priority, their_priority):
        my_options = self.get_newest_by_category(their_priority)
        their_options = other_vendor.get_newest_by_category(my_priority)
        if not my_options or not their_options:
            return False
        return self.swap_items(other_vendor, my_options, their_options)
        