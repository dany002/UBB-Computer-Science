#include <iostream>
#include "Repo.h"
#include "Service.h"
#include "UI.h"


int main() {

    Repo repo;
    Service serv(repo);
    UI ui(serv);
    ui.run();

    return 0;
}
