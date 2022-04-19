from ui.Console import UI
from repository.StudentRepository import StudentRepository
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from services.StudentsService import StudentsService
from services.DisciplinesService import DisciplinesService
from services.GradesService import GradesService
from services.UndoService import UndoService
from repository.UndoRepository import UndoRepository


if __name__ == "__main__":
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

