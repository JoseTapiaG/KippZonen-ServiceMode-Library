import unittest

from Client import Client


class MyTestCase(unittest.TestCase):
    def test_splitFileNames(self):

        response = ''.join(["ELOG0000.TXT  51 2007-06-16 13:21:06\n" ,
                                    "ELOG0001.TXT   512 2007-06-16 13:22:00\n" ,
                                    "ELOG0002.TXT   4886 2007-06-16 13:30:00\n" ,
                                    "ELOG0003.TXT   7922 2007-06-16 13:40:00\n" ,
                                    "ELOG0004.TXT   7922 2007-06-16 13:50:00\n" ,
                                    "SD card size:  127139840 Bytes"])

        client = Client()
        test = client.splitFileNames(response)
        self.assertEqual(["ELOG0000.TXT  51 2007-06-16 13:21:06" ,
                                    "ELOG0001.TXT   512 2007-06-16 13:22:00" ,
                                    "ELOG0002.TXT   4886 2007-06-16 13:30:00" ,
                                    "ELOG0003.TXT   7922 2007-06-16 13:40:00" ,
                                    "ELOG0004.TXT   7922 2007-06-16 13:50:00" ,
                                    "SD card size:  127139840 Bytes"], test)

    def test_getDateOfFileName(self):
        response = "ELOG0000.TXT  51 2007-06-16 13:21:06"
        client = Client()
        test = client.getDateOfFileName(response)
        self.assertEqual("2007-06-16", test)

    def test_splitFileName(self):
        response = "ELOG0000.TXT  51 2007-06-16 13:21:06"
        client = Client()
        test = response.split(" ")[0]
        self.assertEqual("ELOG0000.TXT", test)

    def test_getFileNumberOfFileName(self):
        response = "ELOG0001.TXT"
        client = Client()
        test = client.getFileNumberOfFileName(response)
        self.assertEqual(1, test)

    def test_parseRegister(self):
        response = "2015-12-13 23:50:03  0.011   0.079   0.252 / / / / / / / /"
        client = Client()
        test = client.parseRegister(response.split(" "))
        self.assertEqual("2015-12-13", test.date)
        self.assertEqual("23:50:03", test.time)
        self.assertEqual("0.011", test.data1)
        self.assertEqual("0.079", test.data2)
        self.assertEqual("0.252", test.data3)

if __name__ == '__main__':
    unittest.main()
