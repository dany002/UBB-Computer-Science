#pragma once
#include "Repository.h"
#include "Undo.h"


typedef struct {
	Repository* repo;
    Undo* undo;
    Undo* redo;
}Controller;

Controller* create_controller(Repository* repo, Undo* undo, Undo* redo);

void destroy_controller(Controller* c);

int add(Controller* c, char* name, int quantity, float price, float concentration);

int delete(Controller* c, char* name, float concentration);

int update_quantity(Controller *control, char* name, float concentration, int quantity);

int update_price(Controller *control, char* name, float concentration, float price);

Controller* sort_medicaments(Controller *control);

Controller* sort_medicaments_with_substring(Controller* control, char* substring);

Controller* top_price(Controller* control, int x);

Controller* sort_by_quantity(Controller* control, char* operation);

Controller* sort_price_with_a_given_substring(Controller* control, char* substring);

int undo(Controller* control);

int redo(Controller* control);