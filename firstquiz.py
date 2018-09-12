import unittest
import random
import itertools
#1
def input_nput_put_ut_t(input_str: str) -> list:
    ret_list = []
    new_string = input_str
    while len(new_string) > 0: 
        ret_list.append(new_string)
        new_string = new_string[0:len(new_string)-1]
    return ret_list
print(input_nput_put_ut_t('What the hell'))




#2
def vector_addition(v1: list, v2: list) -> list:
    listt=[]
    for i in range(0,len(v1)):
        c = v1[i] + v2[i]
        listt.append(c)
    return listt
print(vector_addition([1, 2, 3], [4, 5, 6]))

#3
def find_equal_sum_slice(list1,list2):
    for a in range(len(list1)):
        for b in range(len(list1)):
            x=list1[a:b]
            for c in range(len(list2)):
                for d in range(len(list2)):
                    y=list2[c:d]
                    if x!=[] and y!=[] and sum(x)==sum(y):
                        return a,b-1,c,d-1


#4
def basic_sort(int_list):
    for a in range(len(int_list)):
        for b in range(a, len(int_list)):
            if int_list[a] > int_list[b]:
                int_list[a], int_list[b] = int_list[b], int_list[a]
    return int_list



class UnitTest(unittest.TestCase):
    def test_input(self):
        self.assertEqual(input_nput_put_ut_t("What the hell?"),
                         ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',
                          'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']
                         )
    def test_eq_sum_slice(self):
        for i in range(10):
            list1 = [random.randint(0, 150) for i in range(150)]
            list2 = [random.randint(0, 60) for i in range(75)]
            a, b, c, d = find_equal_sum_slice(list1, list2)
            s1, s2 = sum(list1[a:b + 1]), sum(list2[c:d + 1])
            self.assertEqual(s1, s2)
    def test_add_vectors(self):
        self.assertEqual(vector_addition([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(vector_addition([1], [-1]), [0])
    def test_basic_sort(self):
        self.assertEqual([1,3,5,7,9,11,13,15,17,10000], basic_sort([3,1,5,7,9,11,15,17,10000,13]))

    def test_subset_sum(self):
        s={random.randint(-200, 200) for i in range(random.randint(0, 100))}
        k = random.randint(-50, 50)
        subset = subset_sum(s, k)
        self.assertTrue(set(subset).issubset(s))
        self.assertEqual(sum(subset), k)
if __name__ == "__main__":
    unittest.main()