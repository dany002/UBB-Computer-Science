from repository.DisciplineRepository import DisciplineRepository
from domain.Discipline import Discipline
import os.path

class DisciplineTextFileRepository(DisciplineRepository):
    def __init__(self, file_name):
        super().__init__()

        self._file_name = file_name
        if not os.path.exists(self._file_name):
            self._save_file()
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")
        for line in file.readlines():
            discipline_id, name = line.split(maxsplit=1, sep=',')
            self.add_a_discipline(Discipline(int(discipline_id), name.rstrip()))
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt")

        for discipline in self._disciplines:
            file.write(str(discipline.discipline_id) + ',' + discipline.name + "\n")
        file.close()

    def add_a_discipline(self, discipline_that_is_going_to_be_added):
        super(DisciplineTextFileRepository, self).add_a_discipline(discipline_that_is_going_to_be_added)
        self._save_file()

    def remove_a_discipline(self, discipline_id):
        super(DisciplineTextFileRepository, self).remove_a_discipline(discipline_id)
        self._save_file()

    def update_a_discipline_by_id(self, discipline_id, new_discipline_name):
        super(DisciplineTextFileRepository, self).update_a_discipline_by_id(discipline_id, new_discipline_name)
        self._save_file()

    def update_a_discipline_by_name(self, discipline_name, new_discipline_id):
        super(DisciplineTextFileRepository, self).update_a_discipline_by_name(discipline_name, new_discipline_id)
        self._save_file()