import asyncio
import unittest
from spiral_matrix.spiral_matrix import get_matrix


class MatrixTest(unittest.TestCase):
    def test_primary(self):
        SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
        TRAVERSAL = [
            10, 50, 90, 130,
            140, 150, 160, 120,
            80, 40, 30, 20,
            60, 100, 110, 70,
        ]
        self.assertEqual(TRAVERSAL, asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL)))
    
    def test_1_dimension(self):
        SOURCE_URL = 'https://raw.githubusercontent.com/jetsnake/spiral_matrix/main/tests/dimension1.txt'
        TRAVERSAL = [7]
        self.assertEqual(TRAVERSAL, asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL)))
    
    def test_3_dimension(self):
        SOURCE_URL = 'https://raw.githubusercontent.com/jetsnake/spiral_matrix/main/tests/dimension3.txt'
        TRAVERSAL = [
            12, 543, 23,
            432, 250, 1,
            64, 324, 25
        ]
        self.assertEqual(TRAVERSAL, asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL)))
    
    def test_9_dimension(self):
        SOURCE_URL = 'https://raw.githubusercontent.com/jetsnake/spiral_matrix/main/tests/dimension9.txt'
        TRAVERSAL = [
            320, 180, 422, 39, 486, 464, 500, 199, 94, 
            429, 45, 88, 235, 120, 381, 6, 186, 382, 
            303, 347, 526, 444, 506, 303, 322, 446, 151, 
            278, 364, 282, 485, 457, 368, 479, 465, 224, 
            450, 324, 314, 305, 142, 526, 325, 319, 175, 
            408, 63, 348, 425, 74, 381, 470, 478, 307, 
            190, 429, 515, 465, 419, 69, 32, 417, 286, 
            222, 208, 139, 329, 178, 10, 77, 170, 29, 
            437, 366, 176, 359, 213, 362, 344, 132, 168, 

            
        ]
        self.assertEqual(TRAVERSAL, asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL)))

if __name__ == '__main__':
    unittest.main()
