from domain.ActionComposite import ActionComposite
from domain.ActionLeaf import ActionLeaf
from domain.UndoAction import UndoAction


class UndoActionAssembler:

    @staticmethod
    def create_add_student_undo_action(student_service, student_id, name):
        redo_action = ActionLeaf(student_service.add_a_student, (student_id, name))
        undo_action = ActionLeaf(student_service.remove_a_student, tuple([student_id]))
        return UndoAction(undo_action, redo_action)

    @staticmethod
    def create_remove_student_undo_action(student_service, grade_service, student, grades):

        redo_action = ActionLeaf(student_service.remove_a_student, tuple([str(student.student_id)]))
        undo_action = ActionComposite()
        add_student_action = ActionLeaf(student_service.add_a_student, (str(student.student_id), str(student.name)))
        undo_action.add_child(add_student_action)
        for grade in grades:
            add_grade_action = ActionLeaf(grade_service.add_a_grade, (str(grade.student_id), str(grade.discipline_id), str(grade.grade_value)))
            undo_action.add_child(add_grade_action)
        return UndoAction(undo_action, redo_action)

    @staticmethod
    def create_update_student_by_id_undo_action(student_service, student_id, student_name, old_student_name):
        redo_action = ActionLeaf(student_service.update_a_student_by_id, (str(student_id), str(student_name)))
        undo_action = ActionLeaf(student_service.update_a_student_by_id, (str(student_id), str(old_student_name)))
        return UndoAction(undo_action, redo_action)

    @staticmethod
    def create_update_student_by_name_undo_action(student_service, student_name, student_id, old_student_id):
        redo_action = ActionLeaf(student_service.update_a_student_by_name, (str(student_name), str(student_id)))
        undo_action = ActionLeaf(student_service.update_a_student_by_name, (str(student_name), str(old_student_id)))
        return UndoAction(undo_action, redo_action)

    ##########DISCIPLINE##################


    @staticmethod
    def create_add_discipline_undo_action(discipline_service, discipline_id, name):
        redo_action = ActionLeaf(discipline_service.add_a_discipline, (discipline_id, name))
        undo_action = ActionLeaf(discipline_service.remove_a_discipline, tuple([discipline_id]))
        return UndoAction(undo_action, redo_action)

    @staticmethod
    def create_remove_discipline_undo_action(discipline_service, grade_service, discipline, grades):
        redo_action = ActionLeaf(discipline_service.remove_a_discipline, tuple([str(discipline.discipline_id)]))
        undo_action = ActionComposite()
        add_discipline_action = ActionLeaf(discipline_service.add_a_discipline, (str(discipline.discipline_id), str(discipline.name)))
        undo_action.add_child(add_discipline_action)
        for grade in grades:
            add_grade_action = ActionLeaf(grade_service.add_a_grade, (str(grade.student_id), str(grade.discipline_id), str(grade.grade_value)))
            undo_action.add_child(add_grade_action)
        return UndoAction(undo_action, redo_action)

    @staticmethod
    def create_update_discipline_by_id_undo_action(discipline_service, discipline_id, discipline_name, old_discipline_name):
        redo_action = ActionLeaf(discipline_service.update_a_discipline_by_id, (str(discipline_id), str(discipline_name)))
        undo_action = ActionLeaf(discipline_service.update_a_discipline_by_id, (str(discipline_id), str(old_discipline_name)))
        return UndoAction(undo_action, redo_action)

    @staticmethod
    def create_update_discipline_by_name_undo_action(discipline_service, discipline_name, discipline_id, old_discipline_id):
        redo_action = ActionLeaf(discipline_service.update_a_discipline_by_name, (str(discipline_name), str(discipline_id)))
        undo_action = ActionLeaf(discipline_service.update_a_discipline_by_name, (str(discipline_name), str(old_discipline_id)))
        return UndoAction(undo_action, redo_action)

    ###########GRADE##########

    @staticmethod
    def create_grade_a_student_undo_action(grade_service, student_id, discipline_id, grade_value):
        redo_action = ActionLeaf(grade_service.add_a_grade, (student_id, discipline_id, grade_value))
        undo_action = ActionLeaf(grade_service.remove_a_grade_for_a_student_at_a_discipline, (student_id, discipline_id, grade_value))
        return UndoAction(undo_action, redo_action)