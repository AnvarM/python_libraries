class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity <= v:
            return False
        else:
            return True

    def add(self, v):
        # положить v монет в копилку
        if(MoneyBox.can_add(self,v)):
            self.capacity -= v
            return self.capacity
            
            
m = MoneyBox(10)
print(m.can_add(3))
print(m.add(3))
print(m.can_add(3))
print(m.add(3))
print(m.can_add(3))
print(m.add(3))
print(m.can_add(3))
print(m.add(3))
print(m.can_add(3))            
print(m.can_add(3))
print(m.add(3))
print(m.can_add(3))
print(m.add(3))
print(m.can_add(3))     
            