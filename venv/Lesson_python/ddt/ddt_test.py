# coding:utf-8

import ddt
import unittest

data1 = [1,2,3,4,5]
data2 = [[11,22],[22,33]]

@ddt.ddt
class test_ddt(unittest.TestCase):

    # @ddt.data(*data1)
    # def test_print(self,a):
    #
    #     print(a)

    # @ddt.data(*data2)
    # def test_add(self,a):
    #
    #     print(a[0],a[1])
    #     print(a[0]+a[1])

    @ddt.data(*data2)
    @ddt.unpack
    def test_add_1(self,a,b):

        print(a,b)
        print(a+b)

if __name__ == "__main__":

    unittest.main()