# Домашнее задание по теме "Простые юнит-тесты"

import unittest as ut
import test_12_1 as test


class RunnerTest (ut.TestCase):

    def test_walk(self):
        person = test.Runner('Вовка')
        for i in range(10):
            person.walk()
        self.assertEqual(person.distance, 50)

    def test_run(self):
        person = test.Runner('Маша')
        for i in range(10):
            person.run()
        self.assertEqual(person.distance, 100)

    def test_challenge(self):
        person_1 = test.Runner('Гагарин')
        person_2 = test.Runner('Леонов')
        for i in range(10):
            person_1.walk()
            person_2.run()
        self.assertNotEqual(person_1.distance, person_2.distance)


if __name__ == '__main__':
    ut.main()