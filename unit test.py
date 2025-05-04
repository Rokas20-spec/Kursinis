import unittest
from krovinys import Krovinys
from stack import Stack
from dekoratorius import*
from valdytojas import SandėlioValdytojas
from main import apdoroti_sandėlio_objektą



class TestKrovinys(unittest.TestCase):
    def test_krovinys_creation(self):
        krovinys = Krovinys("Testinis krovinys")
        self.assertEqual(krovinys.pavadinimas, "Testinis krovinys")

    def test_krovinys_str(self):
        krovinys = Krovinys("Prekė A")
        self.assertEqual(str(krovinys), "Krovinys: Prekė A")

    def test_krovinys_repr(self):
        krovinys = Krovinys("Prekė B")
        self.assertEqual(repr(krovinys), "Krovinys(pavadinimas='Prekė B')")

class TestStack(unittest.TestCase):
    def test_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(Krovinys("Elementas"))
        self.assertFalse(stack.is_empty())

    def test_stack_push(self):
        stack = Stack()
        krovinys1 = Krovinys("Krovinys 1")
        krovinys2 = Krovinys("Krovinys 2")
        stack.push(krovinys1)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), krovinys1)
        stack.push(krovinys2)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), krovinys2)

    def test_stack_pop(self):
        stack = Stack()
        krovinys1 = Krovinys("Krovinys 1")
        krovinys2 = Krovinys("Krovinys 2")
        stack.push(krovinys1)
        stack.push(krovinys2)
        popped_item = stack.pop()
        self.assertEqual(popped_item, krovinys2)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), krovinys1)
        stack.pop()
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()

    def test_stack_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
        krovinys1 = Krovinys("Krovinys 1")
        stack.push(krovinys1)
        self.assertEqual(stack.peek(), krovinys1)
        self.assertEqual(stack.size(), 1)
        krovinys2 = Krovinys("Krovinys 2")
        stack.push(krovinys2)
        self.assertEqual(stack.peek(), krovinys2)
        self.assertEqual(stack.size(), 2)

    def test_stack_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(Krovinys("Krovinys 1"))
        self.assertEqual(stack.size(), 1)
        stack.push(Krovinys("Krovinys 2"))
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

    def test_stack_len(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        stack.push(Krovinys("Krovinys 1"))
        self.assertEqual(len(stack), 1)


    def test_stack_repr(self):
        stack = Stack()
        self.assertEqual(repr(stack), "Stack(items=[])")
        stack.push(Krovinys("C"))
        self.assertEqual(repr(stack), "Stack(items=[Krovinys(pavadinimas='C')])")



class TestUndoableStackDecorator(unittest.TestCase):
    def test_undo_push(self):
        stack = Stack()
        decorated_stack = AtšaukiamasSandėlioDekoratorius(stack)
        decorated_stack.push(Krovinys("A"))
        self.assertEqual(decorated_stack.size(), 1)
        decorated_stack.atšaukti()
        self.assertEqual(decorated_stack.size(), 0)

    def test_undo_pop(self):
        stack = Stack()
        decorated_stack = AtšaukiamasSandėlioDekoratorius(stack)
        decorated_stack.push(Krovinys("B"))
        decorated_stack.push(Krovinys("C"))
        popped = decorated_stack.pop()
        self.assertEqual(popped.pavadinimas, "C")
        self.assertEqual(decorated_stack.size(), 1)
        decorated_stack.atšaukti()
        self.assertEqual(decorated_stack.size(), 2)
        self.assertEqual(decorated_stack.peek().pavadinimas, "C") # Elementas turėtų būti grąžintas

    def test_undo_empty_stack(self):
        stack = Stack()
        decorated_stack = AtšaukiamasSandėlioDekoratorius(stack)
        decorated_stack.atšaukti() # Neturėtų įvykti klaida


if __name__ == '__main__':
    unittest.main()
