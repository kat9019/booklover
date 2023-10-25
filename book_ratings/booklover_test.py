import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        user1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        user1.add_book("War of the Worlds", 4)
     
        self.assertTrue(user1.has_read("War of the Worlds"))
        
        # add a book and test if it is in `book_list`.

    def test_2_add_book(self):
        #add the same book twice. Test if it's in `book_list` only once.

        user1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        user1.add_book("War of the Worlds", 4)
        user1.add_book("War of the Worlds", 4)
        expected = 1
        self.assertEqual(len(user1.book_list[user1.book_list.book_name=="War of the Worlds"]), expected)
            
        #self.assertTrue(count("War of the Worlds")==1)
        
       # self.assertTrue("already in list!")
        
                
    def test_3_has_read(self): 
        user1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        user1.add_book("War of the Worlds", 4)
        user1.add_book("Fight Club", 3)
        book = "War of the Worlds" 
        self.assertTrue(user1.has_read(book))
        
        # pass a book in the list and test if the answer is `True`.
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`

        user1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        user1.add_book("War of the Worlds", 4)
        user1.add_book("Fight Club", 3)
        
        book = "Cats are Cool" 
        
        self.assertFalse(user1.has_read(book))
        
    def test_5_num_books_read(self): 
        user1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        user1.add_book("War of the Worlds", 4)
        user1.add_book("Fight Club", 3)
        user1.add_book("Jane Eyre", 4)
        
        expected = 3        
        self.assertEqual(user1.num_books_read(), expected) 
        
        # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        user1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        user1.add_book("War of the Worlds", 4)
        user1.add_book("Fight Club", 3)
        user1.add_book("Jane Eyre", 5)
        user1.add_book("Janes Love", 2)
        #fav = user1.fav_books()
        
        expected = 3
        rates = user1.fav_books().book_rating 
        self.assertTrue(lambda x : x > 3 for x in rates)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
    

