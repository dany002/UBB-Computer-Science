from repository.DisciplineRepository import DisciplineRepository
import pickle
import os.path

class DisciplineBinFileRepository(DisciplineRepository):
    def __init__(self, file_name):
        super().__init__()

        self.__file_name = file_name
        if not os.path.exists(self.__file_name):
            self._save_file()
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rb")
        self._disciplines = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._disciplines, file)
        file.close()

    def add_a_discipline(self, discipline_that_is_going_to_be_added):
        super(DisciplineBinFileRepository, self).add_a_discipline(discipline_that_is_going_to_be_added)
        self._save_file()

    def remove_a_discipline(self, discipline_id):
        super(DisciplineBinFileRepository, self).remove_a_discipline(discipline_id)
        self._save_file()

    def update_a_discipline_by_id(self, discipline_id, new_discipline_name):
        super(DisciplineBinFileRepository, self).update_a_discipline_by_id(discipline_id, new_discipline_name)
        self._save_file()

    def update_a_discipline_by_name(self, discipline_name, new_discipline_id):
        super(DisciplineBinFileRepository, self).update_a_discipline_by_name(discipline_name, new_discipline_id)
        self._save_file()