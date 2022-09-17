class Node(object):
    def __init__(self, action_line: str, running_condition: str = None, running_times: int = 1):
        self._head: Node = self
        self._next: Node = None
        self._action_line: str = action_line

        self._running_times: int = running_times
        self._running_condition: str = running_condition

    def append(self, action_line: str, running_condition: str = None, running_times: int = 1):
        node = self
        while True:
            if node._next == None:
                break
            else:
                node = node._next
        node._next = Node(action_line, running_condition, running_times)
        node._next._head = node._head
        return node._next

    @property
    def head(self):
        return self._head

    @property
    def next(self):
        return self._next

    @property
    def running_times(self):
        return self._running_times

    @property
    def running_condition(self):
        return self._running_condition
