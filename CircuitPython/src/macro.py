import os


class Action_Node(object):
    def __init__(self, action_line: str):
        self._head: Action_Node = self
        self._next: Action_Node = None
        self._action_line: str = action_line
        self._loop_start_node: Action_Node = None
        self._loop_times: int = 0
        self._current_loop_times: int = 0

    def push(self, action_line: str):
        node = self
        while True:
            if node._next == None:
                break
            else:
                node = node._next
        node._next = Action_Node(action_line)
        node._next._head = node._head
        return node._next

    def set_loop(self, start_nod, times: int):
        self._loop_start_node = start_nod
        self._loop_times = times
        self._current_loop_times = times


class Action_Process(object):
    def __init__(self, action: Action_Node):
        self._current: Action_Node = action._head

    def dequeue(self) -> Action_Node:
        node = self._current
        if self._current._loop_start_node != None:
            if self._current._current_loop_times < 0 or self._current._current_loop_times > 1:
                self._current = self._current._loop_start_node
                self._current._current_loop_times = self._current._current_loop_times - 1
                return node
        self._current = self._current._next
        return node


S_IFDIR = const(16384)


def get_marcos(base="macros"):
    ret = []
    for p in os.listdir(base):
        path = "{}/{}".format(base, p)
        if p.startswith('.'):
            continue
        elif p.lower().endswith(".m"):
            ret.append(path)
        elif (os.stat(path)[0] & S_IFDIR):
            ret.extend(get_marcos(path))
    return ret


macros = get_marcos()
for macro in macros:
    f = open(macro, "rt")
    while True:
        try:
            row = f.readline()
            print(row.strip())
            break
        except:
            break
    f.close()


f = open("/macros/common.macro", "rt")
