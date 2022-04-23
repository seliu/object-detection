import unittest
import iou

class TestIoU(unittest.TestCase):
    def test_normal(self):
        result = iou.iou([0, 0, 0.2, 0.2], [0.1, 0.1, 0.2, 0.2])
        self.assertTrue(abs(result - 1/7) < 1e-6)

    def test_full_w_outsite(self):
        result = iou.iou([0, 0, 0.2, 0.2], [0.1, 0.1, 0.4, 0.4])
        self.assertEqual(result, 1/4)

    def test_vertex_touched(self):
        result = iou.iou([0, 0, 0.2, 0.2], [0.2, 0.2, 0.2, 0.2])
        self.assertEqual(result, 0)

    def test_no_intersect(self):
        result = iou.iou([0, 0, 0.2, 0.2], [0.3, 0.3, 0.2, 0.2])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()