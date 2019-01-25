import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    """
    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)
        

    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : pyramid3")
        self.assertEqual(str(answer[2]), "?X : pyramid4")
        

    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")
    """
    """
    def setUp(self):
        # Assert starter facts
        file = 'statements_kb2.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)
        

    def test1(self):
        ask1 = read.parse_input("fact: (possesses Ai Loot)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)
     
    def test3(self):
        ask1 = read.parse_input("fact: ((diamonds ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Loot")

    def test4(self):
        ask1 = read.parse_input("fact: (needs ?Y Loot)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : Sarorah")

    def test5(self):
        ask1 = read.parse_input("fact: (inst ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Sarorah, ?Y : Sorceress")
        self.assertEqual(str(answer[1]), "?X : Nosliw, ?Y : Dragon")
    """
    def setUp(self):
        # Assert starter facts
        file = 'statements_kb3.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)
        

    def test1(self):
        ask1 = read.parse_input("fact: (friendly Ai)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (inst Caspa dragon)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)
     
    def test3(self):
        ask1 = read.parse_input("fact: ((inst ?X dragon)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Nosliw")
        self.assertEqual(str(answer[1]), "?X : Uzna")

    def test4(self):
        ask1 = read.parse_input("fact: ((evil ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : Nosliw")
        self.assertEqual(str(answer[1]), "?Y : Caspa")

    def test5(self):
        ask1 = read.parse_input("fact: (isa ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : dragon, ?Y : monster")
        self.assertEqual(str(answer[1]), "?X : giant, ?Y : monster")
        self.assertEqual(str(answer[2]), "?X : dog, ?Y : animal")

if __name__ == '__main__':
    unittest.main()
