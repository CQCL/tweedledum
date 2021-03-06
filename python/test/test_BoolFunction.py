#-------------------------------------------------------------------------------
# Part of Tweedledum Project.  This file is distributed under the MIT License.
# See accompanying file /LICENSE for details.
#-------------------------------------------------------------------------------
import unittest

from tweedledum.BoolFunctionCompiler import BitVec, BoolFunction
from . import examples

class TestBoolFunction(unittest.TestCase):
        def test_constant_3bit(self):
            function = BoolFunction(examples.constant_3bit)
            self.assertEqual(function.signature_, [])
            result = examples.constant_3bit()
            self.assertEqual(result, BitVec(3, '101'))

        def test_id(self):
            function = BoolFunction(examples.identity)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1]])
            result = examples.identity(BitVec(1, '0'))
            self.assertEqual(result, BitVec(1, '0'))
            result = examples.identity(BitVec(1, '1'))
            self.assertEqual(result, BitVec(1, '1'))

        def test_id_2bit(self):
            function = BoolFunction(examples.identity_2bit)
            self.assertEqual(function.signature_, [[type(BitVec(2)), 2]])
            for a in range(4):
                tmp = BitVec(2, a)
                result = examples.identity(tmp)
                self.assertEqual(result, tmp)

        def test_bool_not(self):
            function = BoolFunction(examples.bool_not)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1]])
            for a in range(2):
                tmp = BitVec(1, a)
                result = examples.bool_not(tmp)
                self.assertEqual(result, not bool(tmp))

        def test_bit_not(self):
            function = BoolFunction(examples.bit_not)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1]])
            for a in range(2):
                tmp = BitVec(1, a)
                result = examples.bit_not(tmp)
                self.assertEqual(result, ~tmp)

        def test_bit_not_2bit(self):
            function = BoolFunction(examples.bit_not_2bit)
            self.assertEqual(function.signature_, [[type(BitVec(2)), 2]])
            for a in range(4):
                tmp = BitVec(2, a)
                result = examples.bit_not_2bit(tmp)
                self.assertEqual(result, ~tmp)

        def test_bool_and(self):
            function = BoolFunction(examples.bool_and)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1], 
                                                   [type(BitVec(1)), 1]])
            for a in range(2):
                for b in range(2):
                    result = examples.bool_and(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) and BitVec(1, b)
                    self.assertEqual(result, tmp)

        def test_bit_and(self):
            function = BoolFunction(examples.bit_and)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1], 
                                                   [type(BitVec(1)), 1]])
            for a in range(2):
                for b in range(2):
                    result = examples.bit_and(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) & BitVec(1, b)
                    self.assertEqual(result, tmp)

        def test_bit_and_2bit(self):
            function = BoolFunction(examples.bit_and_2bit)
            self.assertEqual(function.signature_, [[type(BitVec(2)), 2], 
                                                   [type(BitVec(2)), 2]])
            for a in range(4):
                for b in range(4):
                    result = examples.bit_and_2bit(BitVec(2, a), BitVec(2, b))
                    tmp = BitVec(2, a) & BitVec(2, b)
                    self.assertEqual(result, tmp)

        def test_bool_or(self):
            function = BoolFunction(examples.bool_or)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1], 
                                                   [type(BitVec(1)), 1]])
            for a in range(2):
                for b in range(2):
                    result = examples.bool_or(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) or BitVec(1, b)
                    self.assertEqual(result, tmp)

        def test_bit_or(self):
            function = BoolFunction(examples.bit_or)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1], 
                                                   [type(BitVec(1)), 1]])
            for a in range(2):
                for b in range(2):
                    result = examples.bit_or(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) | BitVec(1, b)
                    self.assertEqual(result, tmp)

        def test_bit_or_2bit(self):
            function = BoolFunction(examples.bit_or_2bit)
            self.assertEqual(function.signature_, [[type(BitVec(2)), 2], 
                                                   [type(BitVec(2)), 2]])
            for a in range(4):
                for b in range(4):
                    result = examples.bit_or_2bit(BitVec(2, a), BitVec(2, b))
                    tmp = BitVec(2, a) | BitVec(2, b)
                    self.assertEqual(result, tmp)

        def test_bit_xor(self):
            function = BoolFunction(examples.bit_xor)
            self.assertEqual(function.signature_, [[type(BitVec(1)), 1], 
                                                   [type(BitVec(1)), 1]])
            for a in range(2):
                for b in range(2):
                    result = examples.bit_xor(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) ^ BitVec(1, b)
                    self.assertEqual(result, tmp)

        def test_bit_xor_2bit(self):
            function = BoolFunction(examples.bit_xor_2bit)
            self.assertEqual(function.signature_, [[type(BitVec(2)), 2], 
                                                   [type(BitVec(2)), 2]])
            for a in range(4):
                for b in range(4):
                    result = examples.bit_xor_2bit(BitVec(2, a), BitVec(2, b))
                    tmp = BitVec(2, a) ^ BitVec(2, b)
                    self.assertEqual(result, tmp)

class TestBoolFunctionSimulation(unittest.TestCase):
        def test_constant(self):
            function = BoolFunction(examples.constant)
            result = function.simulate()
            self.assertEqual(result, [True])

        def test_constant_2bit(self):
            function = BoolFunction(examples.constant_2bit)
            result = function.simulate()
            self.assertEqual(result, [False, True])

        def test_id(self):
            function = BoolFunction(examples.identity)
            result = function.simulate(BitVec(1, '0'))
            self.assertEqual(result, [False])
            result = function.simulate(BitVec(1, '1'))
            self.assertEqual(result, [True])

        def test_id_2bit(self):
            function = BoolFunction(examples.identity_2bit)
            for a in range(4):
                tmp = BitVec(2, a)
                result = function.simulate(tmp)
                self.assertEqual(result, [bool(tmp[0]), bool(tmp[1])])

        def test_bool_not(self):
            function = BoolFunction(examples.bool_not)
            result = function.simulate(BitVec(1, '0'))
            self.assertEqual(result, [True])
            result = function.simulate(BitVec(1, '1'))
            self.assertEqual(result, [False])

        def test_bit_not(self):
            function = BoolFunction(examples.bit_not)
            result = function.simulate(BitVec(1, '0'))
            self.assertEqual(result, [True])
            result = function.simulate(BitVec(1, '1'))
            self.assertEqual(result, [False])

        def test_bit_not_2bit(self):
            function = BoolFunction(examples.bit_not_2bit)
            for a in range(4):
                tmp = BitVec(2, a)
                result = function.simulate(tmp)
                self.assertEqual(result, [not tmp[0], not tmp[1]])

        def test_bool_and(self):
            function = BoolFunction(examples.bool_and)
            for a in range(2):
                for b in range(2):
                    result = function.simulate(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) and BitVec(1, b)
                    self.assertEqual(result, [bool(tmp[0])])

        def test_bit_and(self):
            function = BoolFunction(examples.bit_and)
            for a in range(2):
                for b in range(2):
                    result = function.simulate(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) & BitVec(1, b)
                    self.assertEqual(result, [bool(tmp[0])])

        def test_bit_and_2bit(self):
            function = BoolFunction(examples.bit_and_2bit)
            for a in range(4):
                for b in range(4):
                    result = function.simulate(BitVec(2, a), BitVec(2, b))
                    tmp = BitVec(2, a) & BitVec(2, b)
                    self.assertEqual(result, [bool(tmp[0]), bool(tmp[1])])

        def test_bool_or(self):
            function = BoolFunction(examples.bool_or)
            for a in range(2):
                for b in range(2):
                    result = function.simulate(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) or BitVec(1, b)
                    self.assertEqual(result, [bool(tmp[0])])

        def test_bit_or(self):
            function = BoolFunction(examples.bit_or)
            for a in range(2):
                for b in range(2):
                    result = function.simulate(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) | BitVec(1, b)
                    self.assertEqual(result, [bool(tmp[0])])

        def test_bit_or_2bit(self):
            function = BoolFunction(examples.bit_or_2bit)
            for a in range(4):
                for b in range(4):
                    result = function.simulate(BitVec(2, a), BitVec(2, b))
                    tmp = BitVec(2, a) | BitVec(2, b)
                    self.assertEqual(result, [bool(tmp[0]), bool(tmp[1])])

        def test_bit_xor(self):
            function = BoolFunction(examples.bit_xor)
            for a in range(2):
                for b in range(2):
                    result = function.simulate(BitVec(1, a), BitVec(1, b))
                    tmp = BitVec(1, a) ^ BitVec(1, b)
                    self.assertEqual(result, [bool(tmp[0])])

        def test_bit_xor_2bit(self):
            function = BoolFunction(examples.bit_xor_2bit)
            for a in range(4):
                for b in range(4):
                    result = function.simulate(BitVec(2, a), BitVec(2, b))
                    tmp = BitVec(2, a) ^ BitVec(2, b)
                    self.assertEqual(result, [bool(tmp[0]), bool(tmp[1])])

# Simulate full truth table
class TestBoolFunctionFullSimulation(unittest.TestCase):
        def test_id(self):
            function = BoolFunction(examples.identity)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '10')

        def test_id_str(self):
            function = BoolFunction("x")
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '10')

        def test_id_2bit(self):
            function = BoolFunction(examples.identity_2bit)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 2)
            self.assertEqual(str(truth_table[0]), '1010')
            self.assertEqual(str(truth_table[1]), '1100')

        def test_not(self):
            function = BoolFunction(examples.bool_not)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '01')

        def test_not_str(self):
            function = BoolFunction("~x")
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '01')

        def test_not_2bit(self):
            function = BoolFunction(examples.bit_not_2bit)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 2)
            self.assertEqual(str(truth_table[0]), '0101')
            self.assertEqual(str(truth_table[1]), '0011')

        def test_and(self):
            function = BoolFunction(examples.bool_and)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '1000')

        def test_and_str(self):
            function = BoolFunction("x & b")
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '1000')

        def test_and_2bit(self):
            function = BoolFunction(examples.bit_and_2bit)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 2)
            output0 = BitVec(16, 0xaaaa) & BitVec(16, 0xf0f0)
            output1 = BitVec(16, 0xcccc) & BitVec(16, 0xff00)
            self.assertEqual(str(truth_table[0]), str(output0))
            self.assertEqual(str(truth_table[1]), str(output1))

        def test_or(self):
            function = BoolFunction(examples.bool_or)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '1110')

        def test_or_str(self):
            function = BoolFunction("x | b")
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '1110')

        def test_or_2bit(self):
            function = BoolFunction(examples.bit_or_2bit)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 2)
            output0 = BitVec(16, 0xaaaa) | BitVec(16, 0xf0f0)
            output1 = BitVec(16, 0xcccc) | BitVec(16, 0xff00)
            self.assertEqual(str(truth_table[0]), str(output0))
            self.assertEqual(str(truth_table[1]), str(output1))

        def test_xor_str(self):
            function = BoolFunction("x ^ b")
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 1)
            self.assertEqual(str(truth_table[0]), '0110')

        def test_xor_2bit(self):
            function = BoolFunction(examples.bit_xor_2bit)
            truth_table = function.simulate_all()
            self.assertEqual(len(truth_table), 2)
            output0 = BitVec(16, 0xaaaa) ^ BitVec(16, 0xf0f0)
            output1 = BitVec(16, 0xcccc) ^ BitVec(16, 0xff00)
            self.assertEqual(str(truth_table[0]), str(output0))
            self.assertEqual(str(truth_table[1]), str(output1))
