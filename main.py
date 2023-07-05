class Stack:

    def __init__(self):
        self._innerList = []

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self._innerList.append(item)

    def pop(self):
        if self.is_empty():
            return None
        index = self.size() - 1
        item = self._innerList[index]
        self._innerList.__delitem__(index)
        return item

    def peek(self):
        if self.is_empty():
            return None
        index = self.size() - 1
        return self._innerList[index]

    def size(self):
        return len(self._innerList)


def is_open_brace(c):
    return c == "[" or c == "(" or c == "{"


def is_closed_brace(o, c):
    if o == "[" and c == "]":
        return True
    if o == "(" and c == ")":
        return True
    if o == "{" and c == "}":
        return True
    return False


def check_balance(text):
    s = Stack()
    for c in text:
        if s.is_empty() and not is_open_brace(c):
            return False
        if is_open_brace(c):
            s.push(c)
        else:
            if is_closed_brace(s.peek(), c):
                s.pop()
            else:
                return False

    return s.is_empty()


def self_test():
    items = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}", "}{}", "{{[(])]}}", "[[{())}]"]
    for item in items:
        print("Последовательность скобок: " + item)
        if check_balance(item):
            print("Сбалансированно")
        else:
            print("Несбалансированно")


if __name__ == "__main__":
    # self_test()
    txt = input("Введите последовательность скобок:")
    if check_balance(txt):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
