from .import bases
from unittest import TestCase


class TestBases(TestCase):
    def test_convert_function(self):
        tests = [
            
            # conversion from base 10
            {
                'number': 2,
                'to_base': 2,
                'expected': '10',
                'from_base': 10
            },
            {
                'number': 4,
                'to_base': 3,
                'expected': '11',
                'from_base': 10
            },
            {
                'number': 11,
                'to_base': 9,
                'expected': '12',
                'from_base': 10
            },
            {
                'number': 10,
                'to_base': 11,
                'expected': 'A',
                'from_base': 10
            },
            {
                'number': 120,
                'to_base': 11,
                'expected': 'AA',
                'from_base': 10
            },
            # conversion to base 10
            {
                'number': 10,
                'from_base': 2,
                'to_base': 10,
                'expected': '2'
            },
            {
                'number': 11,
                'from_base': 3,
                'to_base': 10,
                'expected': '4'
            },
            {
                'number': 12,
                'from_base': 9,
                'to_base': 10,
                'expected': '11'
            },
            {
                'number': 'A',
                'from_base': 11,
                'to_base': 10,
                'expected': '10'
            },
            {
                'number': 'AA',
                'from_base': 11,
                'to_base': 10,
                'expected': '120'
            }
        ]
        for test in tests:
            print(test)
            self.assertEqual(
                bases.Converter().convert(
                    test['number'], test['to_base'], test['from_base']
                ),
                test['expected']
            )
    def test_base_10_to_base_2(self):
        tests = [
            {
                'number': 2,
                'base': 2,
                'expected': '10'
                
            },
            {
                'number': 4,
                'base': 3,
                'expected': '11'
            },
            {
                'number': 11,
                'base': 9,
                'expected': '12'
            },
            {
                'number': 10,
                'base': 11,
                'expected': 'A'
            },
            {
                'number': 120,
                'base': 11,
                'expected': 'AA'
            }
        ]
        for test in tests:
            self.assertEqual(
                bases.Converter().from_base_ten(test['number'], test['base']), 
                test['expected']
            )
    
    def test_to_base_2(self):
        tests = [
            {
                'number': 10,
                'base': 2,
                'expected': '2'
            },
            {
                'number': 11,
                'base': 3,
                'expected': '4'
            },
            {
                'number': 12,
                'base': 9,
                'expected': '11'
            },
            {
                'number': 'A',
                'base': 11,
                'expected': '10'
            },
            {
                'number': 'AA',
                'base': 11,
                'expected': '120'
            }
        ]
        for test in tests:
            self.assertEqual(
                bases.Converter().to_base_ten(test['number'], test['base']), 
                test['expected']
            )