import unittest

from domain.Discipline import Discipline
from domain.Grade import Grade
from domain.Student import Student
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from repository.StudentRepository import StudentRepository
from services.DisciplinesService import DisciplinesService
from services.UndoService import UndoService
from services.UndoExceptions import UndoServiceException
from services.UndoActionAssembler import UndoActionAssembler
from services.StudentsService import StudentsService
from services.GradesService import GradesService
from repository.UndoRepository import UndoRepository





class TestUndoService(unittest.TestCase):

    def setUp(self) -> None:
        self.__undo_repository = UndoRepository()
        self.__undo_service = UndoService(self.__undo_repository)
        self.__student_repository = StudentRepository()
        self.__grade_repository = GradeRepository()
        self.__student_services = StudentsService(self.__student_repository, self.__grade_repository)
        self.__discipline_repository = DisciplineRepository()
        self.__discipline_services = DisciplinesService(self.__discipline_repository, self.__grade_repository)
        self.__grade_services = GradesService(self.__student_repository, self.__discipline_repository, self.__grade_repository)

    def tearDown(self) -> None:
        pass

    def test_add_student_undo__with_valid_data__is_going_to_be_added_in_the_class_and_then_removed(self):
        self.__student_services.add_a_student("17","Alin")
        self.__undo_service.add(UndoActionAssembler.create_add_student_undo_action(self.__student_services, "17", "Alin"))
        self.__undo_service.undo()
        self.assertEqual(self.__student_services.list_of_students(), [])
        self.__undo_service.redo()
        list_of_expected_students = []
        list_of_expected_students.append(Student(17,"Alin"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)



    def test_remove_student_undo__with_valid_data__is_going_to_be_removed_from_the_class_and_then_added_back(self):
        self.__student_services.add_a_student("17", "Alin")
        self.__student_services.add_a_student("19", "Dani")
        self.__student_services.add_a_student("20", "Florin")
        self.__student_services.add_a_student("21", "George")
        self.__student_services.add_a_student("22", "Mihai")
        self.__discipline_services.add_a_discipline("1","Math")
        self.__discipline_services.add_a_discipline("2","English")
        self.__discipline_services.add_a_discipline("3","French")
        self.__grade_services.add_a_grade("21", "1", "10")
        self.__grade_services.add_a_grade("21", "1", "9")
        self.__grade_services.add_a_grade("21", "2", "9")
        self.__grade_services.add_a_grade("22", "3", "7")
        student = self.__student_services.search_a_student_by_student_ID("21")[0]
        grades = self.__grade_services.get_all_grades_for_a_given_student("21")
        self.__student_services.remove_a_student("21")
        self.__undo_service.add(UndoActionAssembler.create_remove_student_undo_action(self.__student_services, self.__grade_services, student, grades))
        self.__undo_service.undo()
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(22, 3, 7))
        list_of_expected_grades.append(Grade(21, 1, 10))
        list_of_expected_grades.append(Grade(21, 1, 9))
        list_of_expected_grades.append(Grade(21, 2, 9))

        self.assertEqual(self.__grade_services.list_of_grades(), list_of_expected_grades)
        list_of_expected_students = []
        list_of_expected_students.append(Student(17, "Alin"))
        list_of_expected_students.append(Student(19, "Dani"))
        list_of_expected_students.append(Student(20, "Florin"))
        list_of_expected_students.append(Student(22, "Mihai"))
        list_of_expected_students.append(Student(21, "George"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)

        self.__undo_service.redo()
        list_of_expected_students = []
        list_of_expected_students.append(Student(17, "Alin"))
        list_of_expected_students.append(Student(19, "Dani"))
        list_of_expected_students.append(Student(20, "Florin"))
        list_of_expected_students.append(Student(22, "Mihai"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(22, 3, 7))
        list_of_expected_grades.append(Grade(21, 1, 10))
        list_of_expected_grades.append(Grade(21, 1, 9))
        list_of_expected_grades.append(Grade(21, 2, 9))


    def test_update_student_by_id_undo__with_valid_data__is_going_to_update_the_objects_from_the_class(self):
        self.__student_services.add_a_student("17", "Alin")
        self.__student_services.add_a_student("19", "Dani")
        self.__student_services.add_a_student("20", "Florin")
        self.__student_services.add_a_student("21", "George")
        self.__student_services.add_a_student("22", "Mihai")
        old_student_name = self.__student_services.search_a_student_by_student_ID("17")[0].name

        self.__student_services.update_a_student_by_id("17","Marcel")
        self.__undo_service.add(UndoActionAssembler.create_update_student_by_id_undo_action(self.__student_services, "17", "Marcel", old_student_name))


        list_of_expected_students = []
        list_of_expected_students.append(Student(17, "Alin"))
        list_of_expected_students.append(Student(19, "Dani"))
        list_of_expected_students.append(Student(20, "Florin"))
        list_of_expected_students.append(Student(21, "George"))
        list_of_expected_students.append(Student(22, "Mihai"))
        self.__undo_service.undo()
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)
        self.__undo_service.redo()
        list_of_expected_students = []
        list_of_expected_students.append(Student(17, "Marcel"))
        list_of_expected_students.append(Student(19, "Dani"))
        list_of_expected_students.append(Student(20, "Florin"))
        list_of_expected_students.append(Student(21, "George"))
        list_of_expected_students.append(Student(22, "Mihai"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)

    def test_update_student_by_name_undo__with_valid_data__is_going_to_update_the_objects_from_the_class(self):
        self.__student_services.add_a_student("17", "Alin")
        self.__student_services.add_a_student("19", "Dani")
        self.__student_services.add_a_student("20", "Florin")
        self.__student_services.add_a_student("21", "George")
        self.__student_services.add_a_student("22", "Mihai")

        old_student_id = self.__student_services.search_a_student_by_name("Florin")[0].student_id
        self.__student_services.update_a_student_by_name("Florin", "30")
        self.__undo_service.add(UndoActionAssembler.create_update_student_by_name_undo_action(self.__student_services, "Florin", "30", old_student_id))
        self.__undo_service.undo()
        list_of_expected_students = []
        list_of_expected_students.append(Student(17, "Alin"))
        list_of_expected_students.append(Student(19, "Dani"))
        list_of_expected_students.append(Student(20, "Florin"))
        list_of_expected_students.append(Student(21, "George"))
        list_of_expected_students.append(Student(22, "Mihai"))
        self.assertEqual(list_of_expected_students, self.__student_services.list_of_students())
        self.__undo_service.redo()
        list_of_expected_students = []
        list_of_expected_students.append(Student(17, "Alin"))
        list_of_expected_students.append(Student(19, "Dani"))
        list_of_expected_students.append(Student(30, "Florin"))
        list_of_expected_students.append(Student(21, "George"))
        list_of_expected_students.append(Student(22, "Mihai"))
        self.assertEqual(list_of_expected_students, self.__student_services.list_of_students())

    def test_add_discipline_undo__with_valid_data__is_going_to_be_added_in_the_class_and_then_removed(self):
        self.__discipline_services.add_a_discipline("17","PE")
        self.__undo_service.add(UndoActionAssembler.create_add_discipline_undo_action(self.__discipline_services, "17", "PE"))
        self.__undo_service.undo()
        self.assertEqual(self.__discipline_services.list_of_disciplines(), [])
        self.__undo_service.redo()
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(17,"PE"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    def test_remove_discipline_undo__with_valid_data__is_going_to_be_removed_from_the_class_and_then_added_back(self):
        self.__student_services.add_a_student("17", "Alin")
        self.__student_services.add_a_student("19", "Dani")
        self.__student_services.add_a_student("20", "Florin")
        self.__student_services.add_a_student("21", "George")
        self.__student_services.add_a_student("22", "Mihai")
        self.__discipline_services.add_a_discipline("1", "Math")
        self.__discipline_services.add_a_discipline("2", "English")
        self.__discipline_services.add_a_discipline("3", "French")
        self.__grade_services.add_a_grade("21", "1", "10")
        self.__grade_services.add_a_grade("21", "1", "9")
        self.__grade_services.add_a_grade("21", "2", "9")
        self.__grade_services.add_a_grade("22", "3", "7")

        discipline = self.__discipline_services.search_a_discipline_by_discipline_ID("1")[0]
        grades = self.__grade_services.get_all_grades_for_a_given_discipline("1")
        self.__discipline_services.remove_a_discipline("1")
        self.__undo_service.add( UndoActionAssembler.create_remove_discipline_undo_action(self.__discipline_services, self.__grade_services, discipline, grades))
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(2, "English"))
        list_of_expected_disciplines.append(Discipline(3, "French"))
        list_of_expected_disciplines.append(Discipline(1, "Math"))
        self.__undo_service.undo()
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(21, 2, 9))
        list_of_expected_grades.append(Grade(22, 3, 7))
        list_of_expected_grades.append(Grade(21, 1, 10))
        list_of_expected_grades.append(Grade(21, 1, 9))
        self.assertEqual(self.__grade_services.list_of_grades(), list_of_expected_grades)
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(2, "English"))
        list_of_expected_disciplines.append(Discipline(3, "French"))
        self.__undo_service.redo()
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(21, 2, 9))
        list_of_expected_grades.append(Grade(22, 3, 7))
        self.assertEqual(self.__grade_services.list_of_grades(), list_of_expected_grades)


    def test_update_discipline_by_id_undo__with_valid_data__is_going_to_update_the_objects_from_the_class(self):
        self.__discipline_services.add_a_discipline("17", "PE")
        self.__discipline_services.add_a_discipline("18", "Music")
        self.__discipline_services.add_a_discipline("19", "FP")
        self.__discipline_services.add_a_discipline("20", "Logic")
        self.__discipline_services.add_a_discipline("21", "English")
        old_discipline_name = self.__discipline_services.search_a_discipline_by_discipline_ID("18")[0].name
        self.__discipline_services.update_a_discipline_by_id("18", "Russian")
        self.__undo_service.add( UndoActionAssembler.create_update_discipline_by_id_undo_action(self.__discipline_services, "18", "Russian", old_discipline_name))
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(17, "PE"))
        list_of_expected_disciplines.append(Discipline(18, "Music"))
        list_of_expected_disciplines.append(Discipline(19, "FP"))
        list_of_expected_disciplines.append(Discipline(20, "Logic"))
        list_of_expected_disciplines.append(Discipline(21, "English"))
        self.__undo_service.undo()
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)
        self.__undo_service.redo()
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(17, "PE"))
        list_of_expected_disciplines.append(Discipline(18, "Russian"))
        list_of_expected_disciplines.append(Discipline(19, "FP"))
        list_of_expected_disciplines.append(Discipline(20, "Logic"))
        list_of_expected_disciplines.append(Discipline(21, "English"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    def test_update_discipline_by_name_undo__with_valid_data__is_going_to_update_the_objects_from_the_class(self):
        self.__discipline_services.add_a_discipline("17", "PE")
        self.__discipline_services.add_a_discipline("18", "Music")
        self.__discipline_services.add_a_discipline("19", "FP")
        self.__discipline_services.add_a_discipline("20", "Logic")
        self.__discipline_services.add_a_discipline("21", "English")
        old_discipline_id = self.__discipline_services.search_a_discipline_by_name("Logic")[0].discipline_id
        self.__discipline_services.update_a_discipline_by_name("Logic", "30")
        self.__undo_service.add(UndoActionAssembler.create_update_discipline_by_name_undo_action(self.__discipline_services, "Logic", "30", old_discipline_id))
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(17, "PE"))
        list_of_expected_disciplines.append(Discipline(18, "Music"))
        list_of_expected_disciplines.append(Discipline(19, "FP"))
        list_of_expected_disciplines.append(Discipline(20, "Logic"))
        list_of_expected_disciplines.append(Discipline(21, "English"))
        self.__undo_service.undo()
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)
        self.__undo_service.redo()
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(17, "PE"))
        list_of_expected_disciplines.append(Discipline(18, "Music"))
        list_of_expected_disciplines.append(Discipline(19, "FP"))
        list_of_expected_disciplines.append(Discipline(30, "Logic"))
        list_of_expected_disciplines.append(Discipline(21, "English"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    def test_grade_a_student_undo__with_valid_data__is_going_to_grade_a_student_and_then_remove_it(self):
        self.__student_services.add_a_student("17", "Alin")
        self.__student_services.add_a_student("19", "Dani")
        self.__student_services.add_a_student("20", "Florin")
        self.__student_services.add_a_student("21", "George")
        self.__student_services.add_a_student("22", "Mihai")
        self.__discipline_services.add_a_discipline("1", "Math")
        self.__discipline_services.add_a_discipline("2", "English")
        self.__discipline_services.add_a_discipline("3", "French")
        self.__grade_services.add_a_grade("17", "2", "10")
        self.__undo_service.add(UndoActionAssembler.create_grade_a_student_undo_action(self.__grade_services, "17",  "2", "10"))
        self.__undo_service.undo()
        self.assertEqual(self.__grade_services.list_of_grades(), [])
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(17, 2, 10))
        self.__undo_service.redo()
        self.assertEqual(self.__grade_services.list_of_grades(), list_of_expected_grades)

    def test_undo__raise_exception_UndoServiceException__you_cant_undo_anymore(self):
        self.__student_services.add_a_student("17","Alin")
        self.__undo_service.add(UndoActionAssembler.create_add_student_undo_action(self.__student_services, "17", "Alin"))
        self.__undo_service.undo()
        with self.assertRaises(UndoServiceException) as use:
            self.__undo_service.undo()
        self.assertEqual(str(use.exception), "You can't undo anymore.")

    def test_redo_raise_exception_UndoServiceException__you_cant_redo_anymore(self):
        self.__student_services.add_a_student("17", "Alin")
        self.__undo_service.add( UndoActionAssembler.create_add_student_undo_action(self.__student_services, "17", "Alin"))
        self.__undo_service.undo()
        self.__undo_service.redo()
        with self.assertRaises(UndoServiceException) as use:
            self.__undo_service.redo()
        self.assertEqual(str(use.exception), "You can't redo anymore.")

    def test_get_all__with_valid_data__is_going_to_return_all_the_list(self):
        self.assertEqual(self.__undo_service.get_all(), [])