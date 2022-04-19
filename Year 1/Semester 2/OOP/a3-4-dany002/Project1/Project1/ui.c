//
// Created by SenZatIonALL on 3/4/2022.
//

#include <stdio.h>
#include <string.h>
#include "Controller.h"
#include "Ui.h"
#include <stdlib.h>
#include <ctype.h>

UI* createUI(Controller* control)
{
    UI* ui = malloc(sizeof(UI));
    if (ui == NULL)
        return NULL;
    ui->control = control;

    return ui;
}

void destroyUI(UI* ui)
{
    if (ui == NULL)
        return;

    destroy_controller(ui->control);
    free(ui);
}


void print_menu() {
    printf("What do you want to do? \n");
    printf("Type 'add' to add a new medicine. \n");
    printf("Type 'delete' to delete a medicine. \n");
    printf("Type 'Update' to update a medicine. \n");
    printf("Type 'print' to print all available medicines containing a given string. \n");
    printf("Type 'short' to print only those medicines that are in short supply. \n");
    printf("Type 'undo' for undo. \n");
    printf("Type 'redo' for redo. \n");
    printf("Type 'top' to print top x entities with the maximum price. \n");
    printf("Type 'prices' to print all the medicines with the given substring in a descending order. \n");
    printf("Type 'exit' for exit. \n");
}

void create_initial_list(UI* ui){
    add(ui->control, "Ibuprofen", 107, (float)15.4, (float)70.15);
    add(ui->control, "CBD", 1100, (float)90.5, (float)80.6);
    add(ui->control, "Morphine", 300, (float)30.12, (float)25.37);
    add(ui->control, "Paracetamol", 200, (float)69.99, (float)20);
    add(ui->control, "Xanax", 50, (float)130.47, (float)80.14);
    add(ui->control, "Adderall", 123, (float)189.4, (float)15.41);
    add(ui->control, "Syrup", 705, (float)30, (float)5.13);
    add(ui->control, "Nurofen", 458, (float)20.7, (float)15.18);
    add(ui->control, "Patch", 853, (float)5, (float)0.01);
    add(ui->control, "Vedixin", 153, (float)30.2, (float)18.3);

}

void add_ui(UI* ui) {
    char name[40];
    float concentration, price;
    int quantity;
    printf("\nWhat is the name of the medicine you want to add? \n");
    scanf("%s", name);
    printf("\nWhat is the concentration of the medicine you want to add? Please use . as decimal point. \n");
    scanf("%f", &concentration);
    printf("\nWhat is the quantity of the medicine you want to add? \n");
    scanf("%d", &quantity);
    printf("\nWhat is the price of the medicine you want to add? Please use . as decimal point. \n");
    scanf("%f", &price);
    int number = add(ui->control, name, quantity, price, concentration);
    switch(number){
        case 0:
            printf("The medicament was already added. I've added the quantity you've given. \n");
            break;
        case 1:
            printf("The medicament was successfully added. \n");
            break;
        case -1:
            printf("The quantity must be > 0. \n");
            break;
        case -2:
            printf("The price must be > 0. \n");
            break;
        case -3:
            printf("The concentration must be > 0 and < 100. \n");
            break;
        case -4:
            printf("The name must contain only letters! \n");
            break;
        default:
            break;
    }
}

void delete_ui(UI* ui) {
    char name[40];
    float concentration;
    printf("What is the name of the medicine you want to delete? \n");
    scanf("%s", name);
    printf("\nWhat is the concentration of the medicine you want to delete? \n");
    scanf("%f", &concentration);
    int number = delete(ui->control, name, concentration);
    switch(number){
        case 1:
            printf("The medicament was successfully deleted. \n");
            break;
        case 0:
            printf("The medicament wasn't found. \n");
            break;
        case -1:
            printf("The concentration must be > 0 and < 100. \n");
            break;
        case -2:
            printf("The name must contain only letters! \n");
            break;
        default:
            break;
    }
}

void update_ui(UI* ui) {
    char name[40];
    float concentration;
    char command[40];
    printf("What is the name of the medicine you want to update? \n");
    scanf("%s", name);
    printf("\nWhat is the concentration of the medicine you want to update? \n");
    scanf("%f", &concentration);
    printf("\nWhat do you want to update? Quantity or price?\n");
    scanf("%s", command);
    if (strcmp(command, "quantity") == 0) {
        int quantity;
        printf("What is the new quantity? \n");
        scanf("%d", &quantity);
        int number = update_quantity(ui->control, name, concentration, quantity);
        switch(number){
            case 1:
                printf("The medicament was updated with the given quantity! \n");
                break;
            case 0:
                printf("The medicament wasn't found! \n");
                break;
            case -1:
                printf("The concentration must be > 0 and < 100. \n");
                break;
            case -2:
                printf("The name must contain only letters! \n");
                break;
            case -3:
                printf("The quantity must be > 0. \n");
                break;
            default:
                break;

        }
    }
    if (strcmp(command, "price") == 0) {
        float price;
        printf("What is the new price? \n");
        scanf("%f", &price);
        int number = update_price(ui->control, name, concentration, price);
        switch(number){
            case 1:
                printf("The medicament was updated with the given price! \n");
                break;
            case 0:
                printf("The medicament wasn't found! \n");
                break;
            case -1:
                printf("The concentration must be > 0 and < 100. \n");
                break;
            case -2:
                printf("The name must contain only letters! \n");
                break;
            case -3:
                printf("The price must be > 0. \n");
                break;
            default:
                break;
        }
    }
}

void print_all(UI* ui) {
    //We have to sort first and after we ll print it.
    Controller* new_control;
    new_control = sort_medicaments(ui->control);
    for (int i = 0; i < new_control->repo->length; i++) {
        printf("Name: %s ;    ", get_name(new_control->repo->medicaments[i]));
        printf("Quantity: %d ;    ", get_quantity(new_control->repo->medicaments[i]));
        printf("Price: %.2f ;    ", get_price(new_control->repo->medicaments[i]));
        printf("Concentration: %.2f ;  \n", get_concentration(new_control->repo->medicaments[i]));
    }
    destroy_controller(new_control);
}

void print_substring(UI* ui, char* substring){
    Controller* Control = sort_medicaments_with_substring(ui->control, substring);
    //We have to sort first and after we ll print it.

    Controller* new_control;
    new_control = sort_medicaments(Control);
    for (int i = 0; i < new_control->repo->length; i++) {
        printf("Name: %s ;    ", get_name(new_control->repo->medicaments[i]));
        printf("Quantity: %d ;    ", get_quantity(new_control->repo->medicaments[i]));
        printf("Price: %.2f ;    ", get_price(new_control->repo->medicaments[i]));
        printf("Concentration: %.2f ;  \n", get_concentration(new_control->repo->medicaments[i]));
    }
    destroy_controller(new_control);
    destroy_controller(Control);

}

void print_ui(UI* ui) {
    char new_string[40];
    printf("\nWhat is the string?");
    scanf("%s", new_string);

    char all[5] = "all";
    if (strcmp(new_string, all) == 0){
        print_all(ui);

    }

    else {

         print_substring(ui, new_string);
    }
}

void short_ui(UI* ui) {
    int quantity;
    printf("\nGive me the maximum quantity to print all the medicines that have the quantity less than the given value. \n");
    scanf("%d", &quantity);
    char command[40];
    printf("Do you want ascending/descending order?");
    scanf("%s", command);
    Controller* new_control = sort_by_quantity(ui->control, command);
    for(int i = 0; i < ui->control->repo->length; i++)
        if(get_quantity(new_control->repo->medicaments[i]) < quantity){
            printf("Name: %s ;    ", get_name(new_control->repo->medicaments[i]));
            printf("Quantity: %d ;    ", get_quantity(new_control->repo->medicaments[i]));
            printf("Price: %.2f ;    ", get_price(new_control->repo->medicaments[i]));
            printf("Concentration: %.2f ;  \n", get_concentration(new_control->repo->medicaments[i]));
        }
    destroy_controller(new_control);
}

void undo_ui(UI* ui) {
    if(undo(ui->control) == -1)
        printf("You can't undo anymore! \n");
}

void redo_ui(UI* ui) {
    if(redo(ui->control) == -1)
        printf("You can't redo anymore! \n");
}

void top(UI* ui){
    int number;
    printf("Top price! How many medicaments do you want to have in this top?");
    scanf("%d", &number);
    Controller* new_control;
    new_control = top_price(ui->control, number);
    if(new_control == NULL){
        printf("Bad input! \n");
        return;
    }
    else{
        for(int i = 0; i < number; i++){
            printf("Name: %s ;    ", get_name(new_control->repo->medicaments[i]));
            printf("Quantity: %d ;    ", get_quantity(new_control->repo->medicaments[i]));
            printf("Price: %.2f ;    ", get_price(new_control->repo->medicaments[i]));
            printf("Concentration: %.2f ;\n", get_concentration(new_control->repo->medicaments[i]));
            }
    }
    destroy_controller(new_control);
}

void sort_prices_ui(UI* ui){
    char substring[40];
    Controller* new_control;
    printf("Give me the substring \n");
    scanf("%s", substring);
    new_control = sort_price_with_a_given_substring(ui->control, substring);
    if(new_control == NULL){
        printf("No names found with given substring.");
        return;
    }
    for(int i = 0; i < new_control->repo->length; i++){
        printf("Name: %s ;    ", get_name(new_control->repo->medicaments[i]));
        printf("Quantity: %d ;    ", get_quantity(new_control->repo->medicaments[i]));
        printf("Price: %.2f ;    ", get_price(new_control->repo->medicaments[i]));
        printf("Concentration: %.2f ;\n", get_concentration(new_control->repo->medicaments[i]));
    }
    destroy_controller(new_control);
}


int get_command(UI* ui) {
    print_menu();
    char command[40];
    scanf("%s", command);

    if (strcmp(command, "add") == 0) {
        add_ui(ui);
        return 0;
    }
    if (strcmp(command, "delete") == 0) {
        delete_ui(ui);
        return 0;
    }

    if (strcmp(command, "update") == 0) {
        update_ui(ui);
        return 0;
    }

    if (strcmp(command, "print") == 0) {
        print_ui(ui);
        return 0;
    }

    if (strcmp(command, "short") == 0) {
        short_ui(ui);
        return 0;
    }

    if (strcmp(command, "undo") == 0) {
        undo_ui(ui);
        return 0;
    }

    if (strcmp(command, "redo") == 0) {
        redo_ui(ui);
        return 0;
    }

    if (strcmp(command, "top") == 0){
        top(ui);
        return 0;
    }
    if(strcmp(command, "prices") == 0){
        sort_prices_ui(ui);
        return 0;
    }
    if (strcmp(command, "exit") == 0){
        return -1;
    }

}


void start(UI* ui) {

    create_initial_list(ui);
    while (1) {
        if (get_command(ui) == -1)
            break;

    }
}
