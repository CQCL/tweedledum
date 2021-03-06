#-------------------------------------------------------------------------------
# Part of Tweedledum Project.  This file is distributed under the MIT License.
# See accompanying file /LICENSE for details.
#-------------------------------------------------------------------------------
import operator
import random
import unittest
from random import randrange

from tweedledum.BoolFunctionCompiler import BitVec

random.seed(1337)

class TestBitVecDeclaration(unittest.TestCase):
    def setup_strings(self):
        self.strings = list()
        for i in range(1, 1024):
            v0 = randrange((1 << i), (1 << (i+1)))
            v1 = randrange((1 << i), (1 << (i+1)))
            self.strings.append([(1 << i), "{0:b}".format(v0)])
            self.strings.append([(1 << i), "{0:b}".format(v1)])

    def setup_values(self):
        self.values = list()
        for i in range(1, 1024):
            v0 = randrange((1 << i), (1 << (i+1)))
            v1 = randrange((1 << i), (1 << (i+1)))
            self.values.append([(1 << i), v0])
            self.values.append([(1 << i), v1])

    def assertExceptionMessage(self, context, message):
        self.assertTrue(message in context.exception.args[0])

    def test_one_bit_str(self):
        zero_str = BitVec(1, "0")
        self.assertEqual(zero_str.length_, 1)
        self.assertEqual(zero_str.value_, 0)

        one_str = BitVec(1, "1")
        self.assertEqual(one_str.length_, 1)
        self.assertEqual(one_str.value_, 1)

    def test_one_bit_value(self):
        zero_str = BitVec(1, 0)
        self.assertEqual(zero_str.length_, 1)
        self.assertEqual(zero_str.value_, 0)

        one_str = BitVec(1, 1)
        self.assertEqual(one_str.length_, 1)
        self.assertEqual(one_str.value_, 1)

    def test_n_bit_strings(self):
        self.setup_strings()
        for length, string in self.strings:
            bv = BitVec(length, string)
            self.assertEqual(bv.length_, length)
            self.assertEqual(bv.value_, int(string, 2))

            bv = BitVec(string)
            self.assertEqual(bv.length_, len(string))
            self.assertEqual(bv.value_, int(string, 2))

    def test_n_bit_values(self):
        self.setup_values()
        for length, value in self.values:
            bv = BitVec(length, value)
            self.assertEqual(bv.length_, length)
            self.assertEqual(bv.value_, value)

    def test_fail_value_type(self):
        with self.assertRaises(TypeError) as context:
            BitVec(1, 1.0)
        self.assertExceptionMessage(context, 
        "[BitVec] The value must be either an interger or a bit string")

    def test_fail_size_str(self):
        with self.assertRaises(TypeError) as context:
            BitVec(1, "00")
        self.assertExceptionMessage(context, 
        "[BitVec] String requires a bit vector of length 2, but BitVec has "
        "length 1")

    def test_fail_size_value(self):
        with self.assertRaises(TypeError) as context:
            BitVec(1, 10)
        self.assertExceptionMessage(context, 
        "[BitVec] Value requires a bit vector of length 4, but BitVec has "
        "length 1")

class TestBitVecIndexing(unittest.TestCase):
    def setup_strings(self):
        self.bvs = list()
        for i in range(1, 12):
            bv0 = randrange((1 << i), (1 << (i+1)))
            self.bvs.append(BitVec((1 << i), "{0:b}".format(bv0)))

    def test_getitem(self):
        self.setup_strings()
        for bv in self.bvs:
            string = str(bv)
            last = len(string) - 1
            for i in range(len(string)):
                value = bv[i].value_
                self.assertEqual(1, bv[i].length_)
                # Remember that the string is little-endian!
                self.assertEqual(value, int(string[last - i]))
    
    def test_setitem(self):
        self.setup_strings()
        for bv in self.bvs:
            string = str(bv)
            result = BitVec(bv.length_, 0)
            last = len(string) - 1
            for i in range(len(string)):
                # Remember that the string is little-endian!
                result[i] = int(string[last - i])
            self.assertEqual(bv.length_, result.length_)
            self.assertEqual(bv.value_, result.value_)

    def test_getslice(self):
        self.setup_strings()
        # Limit the length
        for bv in self.bvs[0:32]:
            string = str(bv)
            for i in range(1, len(string) + 1):
                for j in range(len(string)):
                    try:
                        result = bv[i:j]
                    except ValueError:
                        self.assertLessEqual(i, j)
                        continue
                    expected = string[len(string) - i:len(string) - j]
                    self.assertEqual(result.length_, len(expected))
                    self.assertEqual(result.value_, int(expected, 2))

    def test_setslice(self):
        self.setup_strings()
        for bv in self.bvs[3:]:
            string = str(bv)
            result = BitVec(bv.length_, (1 << bv.length_ - 1) - 1)
            n = int(bv.length_ / 4)
            for i in range(0, len(string), n):
                part = string[i:i + n]
                result[len(string) - i:len(string) - (i+n)] = BitVec(len(part), part)
            self.assertEqual(result.length_, bv.length_)
            self.assertEqual(result.value_, bv.value_)

class TestBitVecOperations(unittest.TestCase):
    def setup(self):
        self.left_ops = list()
        self.right_ops = list()
        for i in range(1, 12):
            left = randrange((1 << i), (1 << (i+1)))
            self.left_ops.append(BitVec((1 << i), left))
            right = randrange((1 << i), (1 << (i+1)))
            self.left_ops.append(BitVec((1 << i), right))

    def check_binop(self, op):
        self.setup()
        for left, right in zip(self.left_ops, self.right_ops):
            result = op(left, right)
            iresult = op(right, left)
            self.assertEqual(result.length_, left.length_)
            self.assertEqual(result.value_, op(left.value_, right.value_))
            self.assertEqual(iresult.value_, op(left.value_, right.value_))

    def test_and(self):
        self.check_binop(operator.and_)

    def test_or(self):
        self.check_binop(operator.or_)

    def test_xor(self):
        self.check_binop(operator.xor)

    def test_eq(self):
        # TODO
        pass

    def test_ne(self):
        # TODO
        pass
