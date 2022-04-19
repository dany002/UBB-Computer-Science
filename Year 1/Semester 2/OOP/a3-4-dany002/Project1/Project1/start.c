#include "Controller.h"
#include "Repository.h"
#include "Ui.h"
#include "tests.h"
#include "Undo.h"

int main() {
    /*
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    UI* ui = createUI(control);
    start(ui);
    destroyUI(ui);
     */
    test_all();

    return 0;
}