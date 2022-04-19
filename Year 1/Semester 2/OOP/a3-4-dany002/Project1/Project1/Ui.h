#pragma once
#include "Controller.h"

typedef struct
{
    Controller* control;
} UI;

UI* createUI(Controller* s);

void destroyUI(UI* ui);

void print_menu();

void add_ui(UI* ui);

void delete_ui(UI* ui);

void update_ui(UI* ui);

void print_all(UI* ui);

void print_ui(UI* ui);

void short_ui(UI* ui);

void undo_ui(UI* ui);

void redo_ui(UI* ui);

int get_command(UI* ui);

void start(UI* ui);

void create_initial_list(UI* ui);

void print_substring(UI* ui, char* substring);

void top(UI* ui);

void sort_prices_ui(UI* ui);