class LinkedList:
    def __init__(self) -> None:
        self._list = dict()
        self._head_addr = None
        self._next_addr = 0

    def insert(self, item, addr: int = None):
        if self._head_addr is None:
            self._head_addr = self._next_addr

        does_addr_exist = self._list.get(addr, False)
        if addr is None or not does_addr_exist:
            addr = self._next_addr
            self._next_addr += 1
            self._list[addr] = (item, self._next_addr)
        else:
            prev_item, _ = self._list[addr]
            self._list[addr] = (item, self._next_addr)
            self._list[self._next_addr] = (prev_item, self._next_addr + 1)
            self._next_addr += 1

    def delete(self, addr: int):
        does_addr_exist = self._list.get(addr, False)
        if does_addr_exist:
            removed_item, removed_addr = self._list.pop(addr)

        if self._head_addr == addr:
            self._head_addr = removed_addr

        print(f"Removed item '{removed_item}' at address <{removed_addr}>.")

    def read(self, item):
        current_addr = self._head_addr
        current_item, next_addr = self._list[self._head_addr]
        while True:
            if current_item == item:
                print(
                    f"Found item '{item}' at address <{'{:02X}'.format(current_addr)}>."
                )
                break

            next_data = self._list.get(next_addr, None)
            if next_data is None:
                print(f"Item '{item}' is not in linked list.")
                break
            current_addr = next_addr
            current_item, next_addr = next_data

    def display(self):
        current_addr = self._head_addr
        current_item, next_addr = self._list[self._head_addr]
        while True:
            print(f"<{'{:02X}'.format(current_addr)}> ~ {current_item}")
            next_data = self._list.get(next_addr, None)
            if next_data is None:
                break
            current_addr = next_addr
            current_item, next_addr = next_data


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(100)
    ll.insert(200)
    ll.insert(300)
    ll.insert(400)
    ll.insert(500)

    ll.read(500)
    ll.read(99)
