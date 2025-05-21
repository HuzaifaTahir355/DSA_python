import unittest
from assignment_3_again2 import SLL

class TestSLL(unittest.TestCase):

    def setUp(self):
        self.sll = SLL()

    def test_is_empty_on_empty_list(self):
        self.assertTrue(self.sll.is_empty())

    def test_insert_at_start(self):
        self.sll.insert_at_start(10)
        self.assertEqual(self.sll.start.item, 10)

    def test_insert_at_last(self):
        self.sll.insert_at_start(10)
        self.sll.insert_at_last(20)
        self.assertEqual(self.sll.start.next.item, 20)

    def test_search_existing_item(self):
        self.sll.insert_at_start(10)
        self.sll.insert_at_last(20)
        found_node = self.sll.search(20)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.item, 20)

    def test_search_non_existing_item(self):
        self.sll.insert_at_start(10)
        self.assertIsNone(self.sll.search(30))

    def test_insert_after_existing_item(self):
        self.sll.insert_at_start(10)
        self.sll.insert_at_last(20)
        result = self.sll.insert_after(10, 15)
        self.assertEqual(result, "Added Successfully")
        self.assertEqual(self.sll.start.next.item, 15)

    def test_insert_after_non_existing_item(self):
        self.sll.insert_at_start(10)
        result = self.sll.insert_after(30, 15)
        self.assertEqual(result, "Existing Item Not Found")

    def test_delete_first(self):
        self.sll.insert_at_start(10)
        self.sll.insert_at_start(20)
        self.sll.delete_first()
        self.assertEqual(self.sll.start.item, 10)

    def test_delete_last(self):
        self.sll.insert_at_start(10)
        self.sll.insert_at_last(20)
        self.sll.delete_last()
        self.assertIsNone(self.sll.start.next)

    # def test_delete_item_existing(self):
    #     self.sll.insert_at_start(10)
    #     self.sll.insert_at_last(20)
    #     self.sll.insert_at_last(30)
    #     self.sll.delete_item(20)
    #     self.assertEqual(self.sll.start.next.item, 30)
    #
    # def test_delete_item_non_existing(self):
    #     self.sll.insert_at_start(10)
    #     self.sll.insert_at_last(20)
    #     self.sll.delete_item(30)
    #     self.assertEqual(self.sll.start.next.item, 20)

    # def test_delete_item_from_empty_list(self):
    #     self.sll.delete_item(10)
    #     self.assertTrue(self.sll.is_empty())

    def test_iterable(self):
        self.sll.insert_at_start(10)
        self.sll.insert_at_last(20)
        self.sll.insert_at_last(30)
        items = list(self.sll)
        self.assertEqual(items, [10, 20, 30])

if __name__ == "__main__":
    unittest.main()
