import unittest
import time
from configinterface import read_config
from LocalDatabase import create_database
from LocalDatabase import drop_database
from LocalDatabase import read_from_database
from LocalDatabase import add_to_database
from LocalDatabase import change_channel_name


class TestLocalDatabase(unittest.TestCase):

    def test_create_database(self):
        exp = read_config(file='config.cfg', section='Test')
        res1 = create_database(exp)
        self.assertEqual(res1, True)
        self.assertRaises(TypeError, lambda: create_database, 'Wrong type')
        drop_database(exp)


    def test_add_to_database(self):
        exp = read_config(file='config.cfg', section='Test')
        create_database(exp)
        list = {}
        for ii in range(1, 3):
            for i in range(1, 61):
                list[i] = [i, 'Kg', 'tolerant']
                res = add_to_database(dbvalues=exp, list_of_items=list)
                self.assertEqual(res, True)
        drop_database(exp)

    def test_read_from_database(self):
        exp = read_config(file='config.cfg', section='Test')
        create_database(exp)
        list = {}
        fromtime = time.strftime('%H:%M:%S')
        fromdate = time.strftime('%Y-%m-%d')
        for ii in range(1, 3):
            for i in range(1, 61):
                list[i] = [i, 'Kg', 'tolerant']
                add_to_database(list_of_items=list, dbvalues=exp)
        totime = time.strftime('%H:%M:%S')
        todate = time.strftime('%Y-%m-%d')
        parameterlist = {'fromtime': fromtime, 'fromdate': fromdate, 'totime': totime, 'todate': todate}
        for index in range(1, 61):
            parameterlist['id'] = index
            res = read_from_database(dbvalues=exp, readparameters=parameterlist)
            self.assertIsNotNone(res)
        drop_database(exp)
    '''
    def test_change_channel_name(self):
        exp = read_config(file='config.cfg', section='Test')
        create_database(exp)
        newname = 'Whatever'
        for i in range(1, 61):
            sql = "update channels set name = %s where id = %d" % (newname, i)

        change_channel_name()
    '''


if __name__ == '__main__':
    unittest.main()