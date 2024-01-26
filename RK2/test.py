import unittest
from main import *

class TestAnswer1(unittest.TestCase):
    def data(self):
        self.progs = [Program(1, 'Photoshop', 789, 1),
                 Program(2, 'Euro Truck Simulator', 2300, 3),
                 Program(3, 'Euro Truck Simulator 2', 2566, 3),
                 Program(4, 'Internet Explorer', 2, 1),
                 Program(5, 'Microsoft To Do', 40, 2)]

        self.comps = [Computer(1, 'Домашний компьютер'),
                 Computer(2, 'Рабочий компьютер'),
                 Computer(3, 'PlayStation'),
                 Computer(4, 'Планшет'),
                 Computer(5, 'Xbox'),
                 Computer(6, 'Бабушкин пк')]

        self.comps_progs = [ProgramComputerLink(1, 1),
                       ProgramComputerLink(2, 3),
                       ProgramComputerLink(3, 3),
                       ProgramComputerLink(4, 1),
                       ProgramComputerLink(5, 2),

                       ProgramComputerLink(1, 4),
                       ProgramComputerLink(2, 5),
                       ProgramComputerLink(4, 6)]

    def test_answer_1(self):
        self.data()
        result = {i[0]: [p.name for p in self.progs if p.comp_id == i[1]] for i in filter_computers_with_word(self.comps, "компьютер")}
        self.assertEqual(result, {'Домашний компьютер': ['Photoshop', 'Internet Explorer'], 'Рабочий компьютер': ['Microsoft To Do']})

    def test_answer_2(self):
        self.data()
        result = calculate_average_program_size(self.comps, get_one_to_many_relationship(self.progs, self.comps))
        self.assertEqual(result, [('Рабочий компьютер', 40.0), ('Домашний компьютер', 395.5), ('PlayStation', 2433.0)])

    def test_answer_3(self):
        self.data()
        result = get_programs_starting_with_letter(self.progs, 'E', get_many_to_many_relationship(self.comps, self.comps_progs, self.progs))
        self.assertEqual(result, {'Euro Truck Simulator': ['PlayStation', 'Xbox'], 'Euro Truck Simulator 2': ['PlayStation']})

if __name__ == '__main__':
    unittest.main()
