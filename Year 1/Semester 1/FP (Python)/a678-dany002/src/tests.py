# from services.StudentsService import StudentsService
# from services.DisciplinesService import DisciplinesService
# from services.GradesService import GradesService
# from domain.Student import Student
# from domain.Discipline import Discipline
# from domain.Grade import Grade
# from repository.StudentRepository import StudentRepository
# from repository.DisciplineRepository import DisciplineRepository
# from repository.GradeRepository import GradeRepository
#
# def test_add_a_student__with_valid_data__is_going_to_be_added_in_the_class():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     the_list_of_expected_students = []
#     service.add_a_student("30","Georgica")
#     the_list_of_expected_students.append(Student(30,"Georgica"))
#
#     assert the_list_of_expected_students == service.list_of_students()
#
# def test_add_a_student__raise_exception():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     try:
#         service.add_a_student("Idk mate", "som3thing is wr0ng")
#         assert False
#     except Exception:
#         assert True
#
# def test_add_a_student():
#     test_add_a_student__raise_exception()
#     test_add_a_student__with_valid_data__is_going_to_be_added_in_the_class()
#
# def test_add_a_discipline__with_valid_data__is_going_to_be_added_in_the_class():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     service = DisciplinesService(discipline_repository, grade_repository)
#     the_list_of_expected_disciplines = []
#     service.add_a_discipline("30","Chinese")
#     the_list_of_expected_disciplines.append(Discipline(30,"Chinese"))
#
#     assert the_list_of_expected_disciplines == service.list_of_disciplines()
#
#
# def test_add_a_discipline__raise_exception():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     service = DisciplinesService(discipline_repository, grade_repository)
#     try:
#         service.add_a_discipline("1o","3ducation")
#         assert False
#     except Exception:
#         assert True
#
# def test_add_a_discipline():
#     test_add_a_discipline__raise_exception()
#     test_add_a_discipline__with_valid_data__is_going_to_be_added_in_the_class()
#
# def test_add_a_grade__with_valid_data__is_going_to_be_added_in_the_class():
#     student_repository = StudentRepository()
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     grade_service = GradesService(student_repository, discipline_repository, grade_repository)
#     student_service = StudentsService(student_repository, grade_repository)
#     discipline_service = DisciplinesService(discipline_repository, grade_repository)
#     student_service.add_a_student("30","Alin")
#     discipline_service.add_a_discipline("17","Math")
#     grade_service.add_a_grade("30","17","10")
#     the_list_of_expected_grades = []
#
#     the_list_of_expected_grades.append(Grade(30,17, 10))
#     assert the_list_of_expected_grades == grade_service.list_of_grades()
#
# def test_add_a_grade__raise_exception():
#     student_repository = StudentRepository()
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     service = GradesService(student_repository, discipline_repository, grade_repository)
#     try:
#         service.add_a_grade("1o","31","13")
#         assert False
#     except Exception:
#         assert True
#
# def test_add_a_grade():
#     test_add_a_grade__raise_exception()
#     test_add_a_grade__with_valid_data__is_going_to_be_added_in_the_class()
#
# def test_remove_a_student__with_valid_data__is_going_to_be_removed_from_the_class():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     service.add_a_student("23","Alin")
#     service.add_a_student("17","Florin")
#     service.add_a_student("68","Alex")
#     service.remove_a_student("23")
#     the_list_of_expected_students = []
#     the_list_of_expected_students.append(Student(17,"Florin"))
#     the_list_of_expected_students.append(Student(68,"Alex"))
#     assert the_list_of_expected_students == service.list_of_students()
#
# def test_remove_a_student__raise_exception__no_id_in_the_list():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     service.add_a_student("23", "Alin")
#     service.add_a_student("17", "Florin")
#     service.add_a_student("68", "Alex")
#     try:
#         service.remove_a_student("10")
#         assert False
#     except Exception:
#         assert True
#
# def test_remove_a_student():
#     test_remove_a_student__with_valid_data__is_going_to_be_removed_from_the_class()
#     test_remove_a_student__raise_exception__no_id_in_the_list()
#
# def test_remove_a_discipline__with_valid_data__is_going_to_be_removed_from_the_class():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     services = DisciplinesService(discipline_repository, grade_repository)
#     services.add_a_discipline("10","Math")
#     services.add_a_discipline("12","Romanian")
#     services.add_a_discipline("56","English")
#     services.remove_a_discipline("12")
#     the_list_of_expected_disciplines = []
#     the_list_of_expected_disciplines.append(Discipline(10,"Math"))
#     the_list_of_expected_disciplines.append(Discipline(56,"English"))
#     assert the_list_of_expected_disciplines == services.list_of_disciplines()
#
# def test_remove_a_discipline__raise_exception__no_id_in_the_list():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     services = DisciplinesService(discipline_repository, grade_repository)
#     services.add_a_discipline("10","Math")
#     services.add_a_discipline("12","Romanian")
#     services.add_a_discipline("56","English")
#     try:
#         services.remove_a_discipline("300")
#         assert False
#     except Exception:
#         assert True
#
# def test_remove_a_discipline():
#     test_remove_a_discipline__raise_exception__no_id_in_the_list()
#     test_remove_a_discipline__with_valid_data__is_going_to_be_removed_from_the_class()
#
# def test_remove_grades_for_a_student__with_valid_data__is_going_to_be_removed_from_the_class():
#     student_repository = StudentRepository()
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     grade_service = GradesService(student_repository, discipline_repository, grade_repository)
#     student_service = StudentsService(student_repository, grade_repository)
#     discipline_service = DisciplinesService(discipline_repository, grade_repository)
#     student_service.add_a_student("15","Alin")
#     student_service.add_a_student("12","George")
#     student_service.add_a_student("17","Cata")
#     discipline_service.add_a_discipline("20","Math")
#     discipline_service.add_a_discipline("23","Russian")
#     discipline_service.add_a_discipline("56","French")
#     grade_service.add_a_grade("15","20","9")
#     grade_service.add_a_grade("12","23","10")
#     grade_service.add_a_grade("17","56","7")
#     grade_service.remove_grades_for_a_student("15")
#     the_list_of_expected_grades = []
#     the_list_of_expected_grades.append(Grade(12,23,10))
#     the_list_of_expected_grades.append(Grade(17,56,7))
#     assert the_list_of_expected_grades == grade_service.list_of_grades()
#
# def test_remove_grades_for_a_discipline__with_valid_data__is_going_to_be_removed_from_the_class():
#     student_repository = StudentRepository()
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     grade_service = GradesService(student_repository, discipline_repository, grade_repository)
#     student_service = StudentsService(student_repository, grade_repository)
#     discipline_service = DisciplinesService(discipline_repository, grade_repository)
#     student_service.add_a_student("15","Alin")
#     student_service.add_a_student("12","George")
#     student_service.add_a_student("17","Cata")
#     discipline_service.add_a_discipline("20","Math")
#     discipline_service.add_a_discipline("23","Russian")
#     discipline_service.add_a_discipline("56","French")
#     grade_service.add_a_grade("15","20","9")
#     grade_service.add_a_grade("12","23","10")
#     grade_service.add_a_grade("17","56","7")
#     grade_service.remove_grades_for_a_discipline("20")
#     the_list_of_expected_grades = []
#     the_list_of_expected_grades.append(Grade(12,23,10))
#     the_list_of_expected_grades.append(Grade(17,56,7))
#     assert the_list_of_expected_grades == grade_service.list_of_grades()
#
# def test_remove_grades():
#     test_remove_grades_for_a_discipline__with_valid_data__is_going_to_be_removed_from_the_class()
#     test_remove_grades_for_a_student__with_valid_data__is_going_to_be_removed_from_the_class()
#
# def test_update_a_student_by_id__with_valid_data__is_going_to_be_updated():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     service.add_a_student("23","Alin")
#     service.add_a_student("17","Florin")
#     service.add_a_student("68","Alex")
#     service.update_a_student_by_id("23","Dani")
#     the_list_of_expected_students = []
#     the_list_of_expected_students.append(Student(23,"Dani"))
#     the_list_of_expected_students.append(Student(17,"Florin"))
#     the_list_of_expected_students.append(Student(68,"Alex"))
#     assert the_list_of_expected_students == service.list_of_students()
#
# def test_update_a_student_by_id__raise_exception__id_not_found_in_the_class():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     service.add_a_student("23","Alin")
#     service.add_a_student("17","Florin")
#     service.add_a_student("68","Alex")
#     try:
#         service.update_a_student_by_id("196","Dani")
#         assert False
#     except Exception:
#         assert True
#
# def test_update_a_student_by_id():
#     test_update_a_student_by_id__raise_exception__id_not_found_in_the_class()
#     test_update_a_student_by_id__with_valid_data__is_going_to_be_updated()
#
# def test_update_a_student_by_name__with_valid_data__is_going_to_be_updated():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     service.add_a_student("23","Alin")
#     service.add_a_student("17","Florin")
#     service.add_a_student("68","Alex")
#     service.update_a_student_by_name("Alin","30")
#     the_list_of_expected_students = []
#     the_list_of_expected_students.append(Student(30,"Alin"))
#     the_list_of_expected_students.append(Student(17,"Florin"))
#     the_list_of_expected_students.append(Student(68,"Alex"))
#
#     assert the_list_of_expected_students == service.list_of_students()
#
# def test_update_a_student_by_name__raise_exception__id_is_already_taken():
#     student_repository = StudentRepository()
#     grade_repository = GradeRepository()
#     service = StudentsService(student_repository, grade_repository)
#     service.add_a_student("23","Alin")
#     service.add_a_student("17","Florin")
#     service.add_a_student("68","Alex")
#     try:
#         service.update_a_student_by_name("Alin","17")
#         assert False
#     except Exception:
#         assert True
#
# def test_update_a_student_by_name():
#     test_update_a_student_by_name__raise_exception__id_is_already_taken()
#     test_update_a_student_by_name__with_valid_data__is_going_to_be_updated()
#
# def test_update_a_student():
#     test_update_a_student_by_name()
#     test_update_a_student_by_id()
#
# def test_update_a_discipline_by_name__with_valid_data__is_going_to_be_updated():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     services = DisciplinesService(discipline_repository, grade_repository)
#     services.add_a_discipline("10","Math")
#     services.add_a_discipline("12","Romanian")
#     services.add_a_discipline("56","English")
#     services.update_a_discipline_by_name("Math","17")
#     the_list_of_expected_disciplines = []
#     the_list_of_expected_disciplines.append(Discipline(17,"Math"))
#     the_list_of_expected_disciplines.append(Discipline(12,"Romanian"))
#     the_list_of_expected_disciplines.append(Discipline(56,"English"))
#     assert the_list_of_expected_disciplines == services.list_of_disciplines()
#
# def test_update_a_discipline_by_name__raise_exception__discipline_id_is_already_taken():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     services = DisciplinesService(discipline_repository, grade_repository)
#     services.add_a_discipline("10","Math")
#     services.add_a_discipline("12","Romanian")
#     services.add_a_discipline("56","English")
#     try:
#         services.update_a_discipline_by_name("Math","56")
#         assert False
#     except Exception:
#         assert True
#
# def test_update_a_discipline_by_name():
#     test_update_a_discipline_by_name__raise_exception__discipline_id_is_already_taken()
#     test_update_a_discipline_by_name__with_valid_data__is_going_to_be_updated()
#
# def test_update_a_discipline_by_id__with_valid_data__is_going_to_be_updated():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     services = DisciplinesService(discipline_repository, grade_repository)
#     services.add_a_discipline("10","Math")
#     services.add_a_discipline("12","Romanian")
#     services.add_a_discipline("56","English")
#     services.update_a_discipline_by_id("12","Russian")
#     the_list_of_expected_disciplines = []
#     the_list_of_expected_disciplines.append(Discipline(10,"Math"))
#     the_list_of_expected_disciplines.append(Discipline(12,"Russian"))
#     the_list_of_expected_disciplines.append(Discipline(56,"English"))
#     assert the_list_of_expected_disciplines == services.list_of_disciplines()
#
# def test_update_a_discipline_by_id__raise_exception__discipline_id_is_not_in_the_class():
#     discipline_repository = DisciplineRepository()
#     grade_repository = GradeRepository()
#     services = DisciplinesService(discipline_repository, grade_repository)
#     services.add_a_discipline("10","Math")
#     services.add_a_discipline("12","Romanian")
#     services.add_a_discipline("56","English")
#     try:
#         services.update_a_discipline_by_id("45","French")
#         assert False
#     except Exception:
#         assert True
#
# def test_update_a_discipline_by_id():
#     test_update_a_discipline_by_id__raise_exception__discipline_id_is_not_in_the_class()
#     test_update_a_discipline_by_id__with_valid_data__is_going_to_be_updated()
#
# def test_update_a_discipline():
#     test_update_a_discipline_by_name()
#     test_update_a_discipline_by_id()
#
# def tests():
#     test_add_a_student()
#     test_add_a_discipline()
#     test_add_a_grade()
#     test_remove_a_student()
#     test_remove_a_discipline()
#     test_remove_grades()
#     test_update_a_student()
#     test_update_a_discipline()

#######################################################

from domain.TestStudent import TestStudent
from domain.TestGrade import TestGrade
from domain.TestDiscipline import TestDiscipline
from domain.TestValidators import TestValidators
from repository.TestStudentRepository import TestStudentRepository
from repository.TestDisciplineRepository import TestDisciplineRepository
from repository.TestGradeRepository import TestGradeRepository
from repository.TestUndoRepository import TestUndoRepository
from services.TestDisciplineSerivce import TestDisciplineService
from services.TestStudentService import TestStudentService
from services.TestGradesService import TestGradesService
from services.TestUndoService import TestUndoService

import unittest

if __name__ == "__main__":
    unittest.main()