import traceback
from domain.Validators import StudentIdError, StudentNameError, DisciplineIdError, DisciplineNameError, StudentOrDisciplineError, StudentsOrDisciplinesOrGradesError, NameOrId, GradeError, StudentIdNotFoundError, DisciplineIdNotFoundError
from repository.RepositoryException import RepositoryException, RepositoryException2
from services.UndoActionAssembler import UndoActionAssembler
from services.UndoExceptions import UndoServiceException


class UI:
    def __init__(self, student_service, discipline_service, grade_service, undo_service):

        self.__student_services = student_service
        self.__discipline_services = discipline_service
        self.__grade_services = grade_service
        self.__undo_services = undo_service
        self.__commands = {'print': self.ui_print, 'add': self.ui_add, 'search': self.search, 'update': self.update,
                           'grade': self.grade_a_student, 'help': self.help, 'remove': self.remove, 'statistics': self.ui_statistics, 'undo': self.undo, 'redo': self.redo}


    def _print_menu(self):
        print("Choose one from the following")
        print("    <add> to add a student or a discipline.")
        print("    <remove> to remove a student or a discipline.")
        print("    <update> to update a student or a discipline.")
        print("    <print> to print a student or a discipline.")
        print("    <search> to search for a student or a discipline by ID/name.")
        print("    <grade> to grade a student for a discipline.")
        print("    <statistics> for statistics.")
        print("    <help> prints the documentation for all the commands. If you want help only for a command type <help> <command>")
        print("    <undo> ")
        print("    <redo> ")
        print("    <exit> to exit the program.")

    def _initial_list(self):

        self.__student_services.add_a_student("1","Dani")
        self.__student_services.add_a_student("2","Alin")
        self.__student_services.add_a_student("3","George")
        """
        self.__student_services.add_a_student("4","Bogdan")
        self.__student_services.add_a_student("5","Gheorghe")
        self.__student_services.add_a_student("6","Ion")
        self.__student_services.add_a_student("7","Alex")
        self.__student_services.add_a_student("8","Ioan")
        self.__student_services.add_a_student("9","Florin")
        self.__student_services.add_a_student("10","Marian")
        self.__student_services.add_a_student("11","Andreea")
        self.__student_services.add_a_student("12","Alexandra")
        self.__student_services.add_a_student("13","Getuta")
        self.__student_services.add_a_student("14","Gloria")
        self.__student_services.add_a_student("15","Simona")
        self.__student_services.add_a_student("16","Alina")
        self.__student_services.add_a_student("17","Catalina")
        self.__student_services.add_a_student("18","Florentina")
        self.__student_services.add_a_student("19","Corina")
        self.__student_services.add_a_student("20","Dana")
        """
        self.__discipline_services.add_a_discipline("1","FP")
        self.__discipline_services.add_a_discipline("2","Math")
        self.__discipline_services.add_a_discipline("3","English")
        self.__discipline_services.add_a_discipline("4","Romanian")
        self.__discipline_services.add_a_discipline("5","French")
        self.__discipline_services.add_a_discipline("6","Assembly")
        self.__discipline_services.add_a_discipline("7","Logic")
        self.__discipline_services.add_a_discipline("8","Chemistry")
        self.__discipline_services.add_a_discipline("9","Arts")
        self.__discipline_services.add_a_discipline("10","Biology")
        self.__discipline_services.add_a_discipline("11","Geography")
        self.__discipline_services.add_a_discipline("12","History")
        self.__discipline_services.add_a_discipline("13","Russian")
        self.__discipline_services.add_a_discipline("14","Philosophy")
        self.__discipline_services.add_a_discipline("15","Informatics")
        self.__discipline_services.add_a_discipline("16","AI")
        self.__discipline_services.add_a_discipline("17","ML")
        self.__discipline_services.add_a_discipline("18","PE")
        self.__discipline_services.add_a_discipline("19","Music")
        self.__discipline_services.add_a_discipline("20","TIC")
        """

        self.__grade_services.add_a_grade("1","20","10")
        self.__grade_services.add_a_grade("2","19","9")
        self.__grade_services.add_a_grade("3","18","8")
        self.__grade_services.add_a_grade("3","15","10")
        self.__grade_services.add_a_grade("3","11","10")
        self.__grade_services.add_a_grade("4","17","7")
        self.__grade_services.add_a_grade("5","16","6")
        self.__grade_services.add_a_grade("6","15","5")
        self.__grade_services.add_a_grade("7","14","4")
        self.__grade_services.add_a_grade("8","13","3")
        self.__grade_services.add_a_grade("9","12","2")
        self.__grade_services.add_a_grade("10","11","1")
        self.__grade_services.add_a_grade("11","10","2")
        self.__grade_services.add_a_grade("12","9","3")
        self.__grade_services.add_a_grade("13","8","4")
        self.__grade_services.add_a_grade("14","7","5")
        self.__grade_services.add_a_grade("15","6","6")
        self.__grade_services.add_a_grade("16","5","7")
        self.__grade_services.add_a_grade("17","4","8")
        self.__grade_services.add_a_grade("18","3","9")
        self.__grade_services.add_a_grade("19","2","10")
        self.__grade_services.add_a_grade("20","1","6")
        """

    def get_command_and_list(self, command_line):
        position = command_line.find(' ')
        if position == -1:
            return command_line, []
        command = command_line[:position]
        self.list_of_commands = command_line[position:]
        self.list_of_commands = self.list_of_commands.split(' ')
        self.list_of_commands = [elements.strip() for elements in self.list_of_commands]  # now is a list
        del self.list_of_commands[0]  # the first element is ''
        return command, self.list_of_commands

    def run_command(self):

        while True:
            self._print_menu()
            command_line = input("Enter command line: ")
            if command_line == "exit":
                break
            command, list_of_commands = self.get_command_and_list(command_line)
            try:
                self.__commands[command](*list_of_commands)
            except KeyError:
                print("This option is not implemented yet!")
            except ValueError as ve:
                print("The following exception was:", ve)
            except TypeError:
                print("Incorrect input!")
                traceback.print_exc()
            except StudentOrDisciplineError:
                print("The given command must be student or discipline.")
            except StudentsOrDisciplinesOrGradesError:
                print("The given command must be students, disciplines or grades")
            except NameOrId:
                print("You have to choose between Name or ID")

    def undo(self):
        try:
            self.__undo_services.undo()
        except UndoServiceException:
            print("You can't undo anymore!")
        except IndexError:
            print("I'll give you another chance.")

    def redo(self):
        try:
            self.__undo_services.redo()
        except UndoServiceException:
            print("You can't redo anymore!")

    def ui_add(self):
        given_command = input("What do you want to add? A student or a discipline?")
        given_command = given_command.lower()

        if given_command == "student":
            student_id = input("Student id:")
            name = input("Student name: ")
            try:
                self.__student_services.add_a_student(student_id, name)
                self.__undo_services.add(UndoActionAssembler.create_add_student_undo_action(self.__student_services, student_id, name))
            except StudentIdError:
                print("Student id invalid. You need to insert a positive integer.")
            except StudentNameError:
                print("Student name invalid. You need to insert only letters.")
            except RepositoryException:
                print("Student ID is already taken.")

        elif given_command == "discipline":
            discipline_id = input("Discipline id:")
            name = input("Discipline name: ")
            try:
                self.__discipline_services.add_a_discipline(discipline_id, name)
                self.__undo_services.add(UndoActionAssembler.create_add_discipline_undo_action(self.__discipline_services, discipline_id, name))
            except DisciplineIdError:
                print("Discipline id invalid. You need to insert a positive integer.")
            except DisciplineNameError:
                print("Discipline name invalid. You need to insert only letters.")
            except RepositoryException:
                print("Discipline ID is already taken.")
        else:
            raise StudentOrDisciplineError

    def ui_print(self, *list_of_commands):
        if len(list_of_commands) == 0:
            given_command = input("What do you want to list? Students or disciplines or grades?")
            given_command = given_command.lower()
        else:
            given_command = list_of_commands[0]
        if given_command == "students":
            for students in self.__student_services.list_of_students():
                print(students)

        elif given_command == "disciplines":
            for disciplines in self.__discipline_services.list_of_disciplines():
                print(disciplines)


        elif given_command == "grades":
            for grades in self.__grade_services.list_of_grades():
                print(grades)

        elif given_command == "search": # i have no idea how to do this one.
            student_or_discipline = list_of_commands[1]
            if student_or_discipline == "student":
                result_list = list_of_commands[2]
                for result in result_list:
                    print("Student id: ", result.student_id, " Student name: ", result.name) # [{'id': 87, 'name': AWFS}, {...}]
            else:
                result_list = list_of_commands[2]
                for result in result_list:
                    print("Discipline id: ", result.discipline_id, " Discipline name: ", result.name)
        else:
            raise StudentsOrDisciplinesOrGradesError

    def search(self):
        given_command = input("What do you want to search? Discipline or student?")
        given_command = given_command.lower()
        if given_command == "discipline":
            discipline_name_or_discipline_id = input("Do you want to search discipline based on ID or name?")
            discipline_name_or_discipline_id = discipline_name_or_discipline_id.lower()
            if discipline_name_or_discipline_id == "name":
                discipline_name = input("What is the discipline name?")
                discipline_name.lower()
                try:
                    result_list_with_searched_discipline = self.__discipline_services.search_a_discipline_by_name(discipline_name)
                    self.ui_print('search', 'discipline', result_list_with_searched_discipline)
                except RepositoryException:
                    print("There isn't that discipline name in the list.")
                except RepositoryException2:
                    print("Discipline name invalid. You need to insert only letters.")
            elif discipline_name_or_discipline_id == "id":
                discipline_id = input("What is the discipline id?")
                try:
                    result_list_with_searched_discipline = self.__discipline_services.search_a_discipline_by_discipline_ID(discipline_id)
                    self.ui_print('search', 'discipline', result_list_with_searched_discipline)
                except RepositoryException:
                    print("There isn't that discipline ID in the list.")
                except DisciplineIdError:
                    print("Discipline id invalid. You need to insert a positive integer.")

            else:
                raise NameOrId
        elif given_command == "student":
            student_name_or_student_id = input("Do you want to search student based on ID or name?")
            student_name_or_student_id = student_name_or_student_id.lower()
            if student_name_or_student_id == "name":
                student_name = input("What is the student name?")
                student_name.lower()
                try:
                    result_list_with_searched_student = self.__student_services.search_a_student_by_name(student_name)
                    self.ui_print('search','student', result_list_with_searched_student)
                except RepositoryException:
                    print("There isn't that student name in the list.")
                except RepositoryException2:
                    print("Student name invalid. You need to insert only letters.")
            elif student_name_or_student_id == "id":
                student_id = input("What is the student id?")
                try:
                    result_list_with_searched_student = self.__student_services.search_a_student_by_student_ID(student_id)
                    self.ui_print('search','student', result_list_with_searched_student)
                except RepositoryException:
                    print("There isn't that student id in the list.")
                except StudentIdError:
                    print("Student id invalid. You need to insert a positive integer.")
            else:
                raise NameOrId
        else:
            raise StudentOrDisciplineError

    def update(self):
        given_command = input("What do you want to update? Student or discipline?")
        given_command = given_command.lower()
        if given_command == "student":
            id_or_name = input("What do you want to update for a student? The ID or the name?")
            id_or_name = id_or_name.lower()
            if id_or_name == "id":
                student_name = input("What is the student name that you want to update?")
                student_id = input("What ID do you want to be the new student with this name?")
                try:
                    old_student_id = self.__student_services.search_a_student_by_name(student_name)[0].student_id
                    self.__student_services.update_a_student_by_name(student_name, student_id)
                    self.__undo_services.add(UndoActionAssembler.create_update_student_by_name_undo_action(self.__student_services, student_name, student_id, old_student_id))
                except RepositoryException:
                    print("The id that you want to update to the new student is already taken.")
                except RepositoryException2:
                    print("There is no name to be updated.")
            elif id_or_name == "name":
                student_id = input("What is the student ID that you want to update?")
                student_name = input("What name do you want to be the new student with this ID?")
                try:
                    old_student_name = self.__student_services.search_a_student_by_student_ID(student_id)[0].name
                    self.__student_services.update_a_student_by_id(student_id, student_name)
                    self.__undo_services.add(UndoActionAssembler.create_update_student_by_id_undo_action(self.__student_services, student_id, student_name, old_student_name))
                except RepositoryException:
                    print("There is no id to be updated.")
            else:
                raise NameOrId
        elif given_command == "discipline":
            id_or_name = input("What do you want to update for a discipline? The ID or the name?")
            id_or_name = id_or_name.lower()
            if id_or_name == "id":
                discipline_name = input("What is the discipline name that you want to update?")
                discipline_id = input("What ID do you want to be new discipline with this name?")
                try:
                    old_discipline_id = self.__discipline_services.search_a_discipline_by_name(discipline_name)[0].discipline_id
                    self.__discipline_services.update_a_discipline_by_name(discipline_name, discipline_id)
                    self.__undo_services.add(UndoActionAssembler.create_update_discipline_by_name_undo_action(self.__discipline_services, discipline_name, discipline_id, old_discipline_id))
                except RepositoryException:
                    print("The id that you want to update to the new discipline is already taken.")
                except RepositoryException2:
                    print("There is no discipline name to be updated.")

            elif id_or_name == "name":
                discipline_id = input("What is the discipline ID that you want to update?")
                discipline_name = input("What name do you want to be the new discipline with this ID?")
                try:
                    old_discipline_name = self.__discipline_services.search_a_discipline_by_discipline_ID(discipline_id)[0].name
                    self.__discipline_services.update_a_discipline_by_id(discipline_id, discipline_name)
                    self.__undo_services.add(UndoActionAssembler.create_update_discipline_by_id_undo_action(self.__discipline_services, discipline_id, discipline_name, old_discipline_name))
                except RepositoryException:
                    print("There is no id to be updated.")

            else:
                raise NameOrId
        else:
            raise StudentOrDisciplineError

    def remove(self):

        given_command = input("What do you want to remove? Student or discipline?")
        given_command = given_command.lower()
        if given_command == "student":
            student_id = input("What is the student id that you want to remove?")
            try:
                student = self.__student_services.search_a_student_by_student_ID(student_id)[0]
                grades = self.__grade_services.get_all_grades_for_a_given_student(student_id)
                self.__student_services.remove_a_student(student_id)
                self.__undo_services.add(UndoActionAssembler.create_remove_student_undo_action(self.__student_services, self.__grade_services, student, grades))
            except RepositoryException:
                print("The id that you want to remove is not in the list.")
        elif given_command == "discipline":
            discipline_id = input("What is the discipline id that you want to remove?")
            try:
                discipline = self.__discipline_services.search_a_discipline_by_discipline_ID(discipline_id)[0]
                grades = self.__grade_services.get_all_grades_for_a_given_discipline(discipline_id)
                self.__discipline_services.remove_a_discipline(discipline_id)
                self.__undo_services.add(UndoActionAssembler.create_remove_discipline_undo_action(self.__discipline_services, self.__grade_services, discipline, grades))
            except RepositoryException:
                print("The id that you want to remove is not in the list.")
        else:
            raise StudentOrDisciplineError

    def grade_a_student(self):

        student_id = input("What is the student id that you want to grade?")
        discipline_id = input("What is the discipline id that you want to grade?")
        grade = input("What is the grade?")
        try:
            self.__grade_services.add_a_grade(student_id, discipline_id, grade)
            self.__undo_services.add(UndoActionAssembler.create_grade_a_student_undo_action(self.__grade_services, student_id, discipline_id, grade))
        except StudentIdError:
            print("Student id invalid. You need to insert a positive integer.")
        except DisciplineIdError:
            print("Discipline id invalid. You need to insert a positive integer.")
        except GradeError:
            print("Grade invalid. You need to insert a integer between 1 and 10.")
        except StudentIdNotFoundError:
            print("The student id that you want to grade is not found.")
        except DisciplineIdNotFoundError:
            print("The discipline id that you want to grade is not found.")

    def help_all(self,):
        self.help("add")
        self.help("print")
        self.help("search")
        self.help("grade")
        self.help("update")
        self.help("statistics")

    def help(self, *list_of_commands):
        if len(list_of_commands) == 0:
            self.help_all()
            return
        else:
            given_command = list_of_commands[0]

        if given_command == "add":
            print("Commands: add student <student_id> <student_name> - it adds a student. \n"
                  "          add discipline <discipline_id> <discipline_name> - it adds a discipline. \n")
        elif given_command == "print":
            print("Commands: print students - it prints all the students. \n"
                  "          print disciplines - it prints all the disciplines. \n"
                  "          print grades - it prints all the grades. \n")
        elif given_command == "search":
            print("Commands: search discipline <discipline_id> - it prints all the disciplines with the given id. \n"
                  "          search discipline <discipline_name> - it prints all the discipline with the given name. \n"
                  "          search student <student_id> - it prints all the students with the given id. \n"
                  "          search student <student_name> - it prints all the students with the given name. \n")
        elif given_command == "grade":
            print("Commands: grade <student_id> <discipline_id> <grade> - it grades a student with the given grade to the given discipline. \n")
        elif given_command == "update":
            print("Commands: update student id <student_id> with name <student_name>. \n"
                  "          update student name <student_name> with id <student_id>. \n"
                  "          update discipline id <discipline_id> with name <discipline_name>. \n"
                  "          update discipline name <discipline_name> with id <discipline_id>. \n")
        elif given_command == "statistics":
            print("Commands: statistics all students failing. \n"
                  "          statistics best school situation. \n"
                  "          statistics all disciplines with at least one grade. \n")

    def ui_statistics(self):
        all_students_failing__or__best_school_situation__all_disciplines_with_at_least_one_grade = \
            input('Choose one from the following: "all students failing" or "best school situation" or "all disciplines with at least one grade":')
        all_students_failing__or__best_school_situation__all_disciplines_with_at_least_one_grade = all_students_failing__or__best_school_situation__all_disciplines_with_at_least_one_grade.lower()
        if all_students_failing__or__best_school_situation__all_disciplines_with_at_least_one_grade == "all students failing":
            list_with_all_students_id_failing = self.__grade_services.statistics_for_all_students_failing_at_one_or_more_disciplines()
            for index in range(len(list_with_all_students_id_failing)):
                student_id = list_with_all_students_id_failing[index]
                result_list_with_searched_student = self.__student_services.search_a_student_by_student_ID(str(student_id))
                self.ui_print('search', 'student', result_list_with_searched_student)
        elif all_students_failing__or__best_school_situation__all_disciplines_with_at_least_one_grade == "best school situation":
            print("Students with the best school situation: ")
            students_with_the_best_school_situation = self.__grade_services.statistics_for_students_with_best_school_situation()
            for index in range(len(students_with_the_best_school_situation)):
                student_id = students_with_the_best_school_situation[index]
                result_list_with_searched_student = self.__student_services.search_a_student_by_student_ID(str(student_id))
                self.ui_print('search', 'student', result_list_with_searched_student)

        elif all_students_failing__or__best_school_situation__all_disciplines_with_at_least_one_grade == "all disciplines with at least one grade":
            print("All disciplines at which there is at least one grade, sorted in descending order of the average grade(s) received by all students are:")
            all_disciplines_with_at_least_one_grade = self.__grade_services.statistics_for_all_disciplines_with_at_least_one_grade()
            for index in range(len(all_disciplines_with_at_least_one_grade)):
                result_list_with_searched_discipline = self.__discipline_services.search_a_discipline_by_discipline_ID(str(all_disciplines_with_at_least_one_grade[index]))
                self.ui_print('search', 'discipline', result_list_with_searched_discipline)

