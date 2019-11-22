import unittest
import coverage_calculator


class TestCoverageCalculator(unittest.TestCase):

    def test_get_data_in_dictionary(self):
        test_reads_data = ['start,length\n', '1100,120\n', '1250,130\n', '1340, 120\n', '1560,180\n', '1690,160\n', '1690,160\n', '1690,150\n']
        actual_max_read_length = 180
        actual_Reads = {1100: {120: 1}, 1250: {130: 1}, 1340: {120: 1}, 1560: {180: 1}, 1690: {160: 2, 150: 1}}
        test_max_read_length, test_Reads = coverage_calculator.get_data_in_dictionary(test_reads_data)
        self.assertEqual(actual_max_read_length, test_max_read_length)
        # print(test_Reads)
        self.assertEqual(actual_Reads[1340], test_Reads[1340])
        self.assertEqual(actual_Reads[1690], test_Reads[1690])

    def test_get_start_loci_key_index(self):
        test_loci_key = 24
        test_max_read_length = 3
        test_read_key_list = [10, 15, 18, 22, 26, 30]
        test_start_loci_index = coverage_calculator.get_start_loci_key_index(test_loci_key, test_read_key_list, test_max_read_length)
        self.assertEqual(test_start_loci_index, 3)

    def test_get_narrowed_read_keys(self):
        test_loci_key = 24
        test_max_read_length = 3
        test_read_key_list = [10, 15, 18, 22, 26, 30]
        test_start_loci_index = 3
        test_loci_keys_list = coverage_calculator.get_narrowed_read_keys(test_loci_key, test_read_key_list, test_start_loci_index, test_max_read_length)
        self.assertEqual(test_loci_keys_list, [22, 26])

    def test_get_coverage(self):
        test_loci_key = 1350
        test_reads = {1100: {120: 1}, 1250: {130: 1}, 1340: {120: 1}, 1560: {180: 1}, 1690: {160: 2, 150: 1}}
        test_loci_keys_list = [1250, 1340]
        test_key_coverage = coverage_calculator.get_coverage(test_loci_key, test_loci_keys_list, test_reads)
        self.assertEqual(test_key_coverage, 2)


if __name__ == '__main__':
    unittest.main()
