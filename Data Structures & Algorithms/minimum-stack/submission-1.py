class MinStack:

    def __init__(self):
        self._store = []
        self._top = -1
        self._min_elements = []

    def push(self, val: int) -> None:
        self._store.append(val)
        self._top += 1

        if len(self._min_elements) == 0:
            self._min_elements.append(val)
        else:
            if val <= self.getMin():
                self._min_elements.append(val)

    def pop(self) -> None:
        removed = self._store.pop()
        self._top -= 1

        if removed == self.getMin():
            self._min_elements.pop()


    def top(self) -> int:
        return self._store[self._top]

    def getMin(self) -> int:
        return self._min_elements[-1]

"""
Constructor:
stack store = []
top_ptr, updated when pushed and popped
min_element- an array that contains the history of minimum elements

push()
add an element to the array 
update the top_ptr
update the min element if necesary

pop()
remove the element at thr top of the stack
update the top pointer
update the min_element history in case the stack top was the min element
"""