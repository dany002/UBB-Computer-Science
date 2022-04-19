from ui.Console import UI
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from services.StudentsService import StudentsService
from services.DisciplinesService import DisciplinesService
from services.GradesService import GradesService
from services.UndoService import UndoService
from repository.UndoRepository import UndoRepository
from repository.StudentTextFileRepository import StudentTextFileRepository
from repository.StudentBinFileRepository import StudentBinFileRepository
from repository.StudentRepository import StudentRepository
from repository.DisciplineTextFileRepository import DisciplineTextFileRepository
from repository.DisciplineBinFileRepository import DisciplineBinFileRepository
from repository.GradeTextFileRepository import GradeTextFileRepository
from repository.GradeBinFileRepository import GradeBinFileRepository

if __name__ == "__main__":

    student_repository = None
    discipline_repository = None
    grade_repository = None
    mode = None
    file = open("settings.properties", "r")
    informations = {}
    for line in file:
        command = line.strip().split("=", maxsplit=1)
        if command[0] == "repository ":
            if command[1] == " inmemory":
                mode = "inmemory"
            elif command[1] == " binaryfiles":
                mode = "binaryfiles"
            elif command[1] == " textfiles":
                mode = "textfiles"
            continue

        if mode == "textfiles":
            if command[0].strip() == "students":
                file_name = command[1].strip()
                file_name = file_name[1:-1]
                informations['student'] = file_name

            elif command[0].strip() == "disciplines":
                file_name = command[1].strip()
                file_name = file_name[1:-1]
                informations['disciplines'] = file_name
            elif command[0].strip() == "grades":
                file_name = command[1].strip()
                file_name = file_name[1:-1]
                informations['grades'] = file_name
            continue

        if mode == "binaryfiles":
            if command[0].strip() == "students":
                file_name = command[1].strip()
                file_name = file_name[1:-1]
                informations['student'] = file_name
            elif command[0].strip() == "disciplines":
                file_name = command[1].strip()
                file_name = file_name[1:-1]
                informations['disciplines'] = file_name

            elif command[0].strip() == "grades":
                file_name = command[1].strip()
                file_name = file_name[1:-1]
                informations['grades'] = file_name
            continue

        if mode == "inmemory":
            break

    if mode == "textfiles":
        student_repository = StudentTextFileRepository(informations['student'])
        discipline_repository = DisciplineTextFileRepository(informations['disciplines'])
        grade_repository = GradeTextFileRepository(informations['grades'])

    elif mode == "binaryfiles":
        student_repository = StudentBinFileRepository(informations['student'])
        discipline_repository = DisciplineBinFileRepository(informations['disciplines'])
        grade_repository = GradeBinFileRepository(informations['grades'])

    elif mode == "inmemory":
        student_repository = StudentRepository()
        discipline_repository = DisciplineRepository()
        grade_repository = GradeRepository()

    student_service = StudentsService(student_repository, grade_repository)
    discipline_service = DisciplinesService(discipline_repository, grade_repository)
    grade_service = GradesService(student_repository, discipline_repository, grade_repository)
    undo_repository = UndoRepository()
    undo_service = UndoService(undo_repository)
    ui = UI(student_service, discipline_service, grade_service, undo_service)
    ui.run_command()

