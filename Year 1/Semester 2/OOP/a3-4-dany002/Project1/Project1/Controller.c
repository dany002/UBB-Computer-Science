#include "Controller.h"
#include <stdio.h>
#include <stdlib.h>
#include "Repository.h"
#include "Validator.h"
#include <string.h>
#include "Undo.h"

Controller* create_controller(Repository* repo, Undo* undo, Undo* redo) {
    /*
     * It creates a controller using dynamic memory allocation, and it returns the controller.
     */
    Controller* c = malloc(sizeof(Controller));
    if(c == NULL)
        return NULL;
    c->repo = repo;
    c->undo = undo;
    c->redo = redo;
    return c;
}

void destroy_controller(Controller* c) {
    /*
     * It destroys the controller using function free.
     */
    if (c == NULL)
        return;

    destroy_undo(c->redo);
    destroy_undo(c->undo);
    destroy_repository(c->repo);
    free(c);
    c = NULL;

}

int add(Controller* c, char* name, int quantity, float price, float concentration) {
    /*
     * First it checks if the input is correct. And after that it's going to be added in the repository.
     * return: -1 - quantity is < 0
     *          -2 - price is < 0
     *          -3 - concentration is <= 0 or >= 100
     *          -4 - name contains digits
     *           0 - the medicament is already in repository but the quantity is going to be updated.
     *           1 - the medicament was successfully added.
     */

    if(validator_quantity(quantity) == 0)
        return -1;
    if(validator_price(price) == 0)
        return -2;
    if(validator_concentration(concentration) == 0)
        return -3;
    if(validator_name(name) == 0)
        return -4;

    delete_drug(c->undo, create_medicament(name, quantity, price, concentration));

    return add_medicament(c->repo, create_medicament(name, quantity, price, concentration));
}

int delete(Controller* c, char* name, float concentration){
    /*
     * First it checks if the input is correct and after that, it's going to delete the medicament from repository.
     * return: -1 - concentration is <= 0 or >= 100
     *         -2 - name contains digits
     *          0 - the medicament that is supposed to be deleted is not found in the repository.
     *          1 - the medicament was successfully deleted.
     */
    if(validator_concentration(concentration) == 0)
        return -1;
    if(validator_name(name) == 0)
        return -2;
    Medicine* med = create_a_specific_medicament(c->repo, name, concentration);
    if(med != NULL)
        add_drug(c->undo, med);

    return delete_medicament(c->repo, name, concentration);
}


int update_quantity(Controller *control, char* name, float concentration, int quantity){
    /*
     * First it checks if the input is correct and after that, it's going to update the quantity for the given medicament from repository.
     * return: -1 - concentration is <= 0 or >= 100
     *         -2 - name contains digits
     *         -3 - quantity is < 0
     *          0 - the medicament that is supposed to be updated is not found in the repository.
     *          1 - the medicament was successfully updated.
     */
    if(validator_concentration(concentration) == 0)
        return -1;
    if(validator_name(name) == 0)
        return -2;
    if(validator_quantity(quantity) == 0)
        return -3;
    Medicine* med = create_a_specific_medicament(control->repo, name, concentration);
    if(med == NULL)
        return 0;
    update_drug_by_quantity(control->undo, med);
    update_quantity_repo(control->repo, name, concentration, quantity);

    return 1;
}

int update_price(Controller *control, char* name, float concentration, float price){
    /*
     * First it checks if the input is correct and after that, it's going to update the price for the given medicament from repository.
     * return: -1 - concentration is <= 0 or >= 100
     *         -2 - name contains digits
     *         -3 - price is < 0
     *          0 - the medicament that is supposed to be updated is not found in the repository.
     *          1 - the medicament was successfully updated.
     */
    if(validator_concentration(concentration) == 0)
        return -1;
    if(validator_name(name) == 0)
        return -2;
    if(validator_price(price) == 0)
        return -3;
    Medicine* med = create_a_specific_medicament(control->repo, name, concentration);
    if(med == NULL)
        return 0;
    update_drug_by_price(control->undo, med);
    update_price_repo(control->repo, name, concentration, price);

    return 1;
}

int undo(Controller* control){
    /*
     * First it checks if the undo list is 0. If it is, it returns -1.
     * If the id is 1 it means that undo function has to add back the drug, and also it sets for the redo function a future delete.
     * If the id is 2 it means that undo function has to remove the drug, and also it sets for the redo function a future add.
     * If the id is 3 it means that undo function has to update drug by quantity, and also it copies in redo what was before.
     * If the id is 4 it means that undo function has to update drug by price, and also it copies in redo what was before.
     */
    if(control->undo->length == 0)
        return -1;
    if(control->undo->drugs[control->undo->length - 1]->id == 1){
        add_medicament(control->repo, create_medicament(control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->quantity,
                                                        control->undo->drugs[control->undo->length - 1]->price, control->undo->drugs[control->undo->length - 1]->concentration));
        Medicine* med = create_a_specific_medicament(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration);
        delete_drug(control->redo, med);
        control->undo->length--;
        return 1;
    }
    if(control->undo->drugs[control->undo->length - 1]->id == 2){
        Medicine* med = create_a_specific_medicament(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration);
        add_drug(control->redo, med);
        delete_medicament(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration);
        control->undo->length--;
        return 1;
    }
    if(control->undo->drugs[control->undo->length - 1]->id == 3){
        Medicine* med2 = create_a_specific_medicament(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration);
        update_drug_by_quantity(control->redo, med2);
        update_quantity_repo(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration,
                             control->undo->drugs[control->undo->length - 1]->quantity);
        control->undo->length--;
        return 1;
    }
    if(control->undo->drugs[control->undo->length - 1]->id == 4){
        Medicine* med2 = create_a_specific_medicament(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration);
        update_drug_by_price(control->redo, med2);
        update_price_repo(control->repo, control->undo->drugs[control->undo->length - 1]->name, control->undo->drugs[control->undo->length - 1]->concentration,
                          control->undo->drugs[control->undo->length - 1]->price);
        control->undo->length--;
        return 1;
    }
}

int redo(Controller* control){
    /*
     * First it checks if the redo list is 0. If it is, it returns -1.
     * If the id is 1 it means that redo function has to add back the drug, and also it sets for the undo function a future delete.
     * If the id is 2 it means that redo function has to remove the drug, and also it sets for the undo function a future add.
     * If the id is 3 it means that redo function has to update drug by quantity, and also it copies in undo what was before.
     * If the id is 4 it means that redo function has to update drug by price, and also it copies in undo what was before.
     */
    if(control->redo->length == 0)
        return -1;

    if(control->redo->drugs[control->redo->length - 1]->id == 1){
        delete_drug(control->undo, create_medicament(control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->quantity,
                                                     control->redo->drugs[control->redo->length - 1]->price, control->redo->drugs[control->redo->length - 1]->concentration));
        add_medicament(control->repo, create_medicament(control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->quantity,
                                                        control->redo->drugs[control->redo->length - 1]->price, control->redo->drugs[control->redo->length - 1]->concentration));
        control->redo->length--;
        return 1;
    }
    if(control->redo->drugs[control->redo->length - 1]->id == 2){
        add_drug(control->undo, create_medicament(control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->quantity,
                                                  control->redo->drugs[control->redo->length - 1]->price, control->redo->drugs[control->redo->length - 1]->concentration));
        delete_medicament(control->repo, control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->concentration);
        control->redo->length--;
        return 1;
    }
    if(control->redo->drugs[control->redo->length - 1]->id == 3){
        Medicine* med2 = create_a_specific_medicament(control->repo, control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->concentration);
        update_quantity_repo(control->repo, control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->concentration,
                             control->redo->drugs[control->redo->length - 1]->quantity);
        update_drug_by_quantity(control->undo, med2);
        control->redo->length--;
        return 1;
    }
    if(control->redo->drugs[control->redo->length - 1]->id == 4){
        Medicine* med2 = create_a_specific_medicament(control->repo, control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->concentration);
        update_price_repo(control->repo, control->redo->drugs[control->redo->length - 1]->name, control->redo->drugs[control->redo->length - 1]->concentration,
                          control->redo->drugs[control->redo->length - 1]->price);
        update_drug_by_price(control->undo, med2);
        control->redo->length--;
        return 1;
    }
}


Controller* sort_medicaments(Controller *control){
    /*
     * It sorts ascending the medicaments from the repository by name and it returns the sorted controller.
     */

    Repository* new_repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* new_controller = create_controller(new_repo, new_undo, new_redo);

    Medicine* new_medicine;

    for(int i = 0; i < control->repo->length; i++){
        add_medicament(new_controller->repo, create_medicament(control->repo->medicaments[i]->name,
                                                               control->repo->medicaments[i]->quantity,
                                                               control->repo->medicaments[i]->price,
                                                               control->repo->medicaments[i]->concentration));
    }


    for(int i = 0; i < control->repo->length - 1; i++)
        for(int j = i + 1; j < control->repo->length; j++)
            if(strcmp(get_name(new_controller->repo->medicaments[i]), get_name(new_controller->repo->medicaments[j])) > 0){
                new_medicine = copy_medicine(create_medicament(new_controller->repo->medicaments[i]->name,
                                                               new_controller->repo->medicaments[i]->quantity,
                                                               new_controller->repo->medicaments[i]->price,
                                                               new_controller->repo->medicaments[i]->concentration));
                new_controller->repo->medicaments[i] = copy_medicine(create_medicament(new_controller->repo->medicaments[j]->name,
                                                                                       new_controller->repo->medicaments[j]->quantity,
                                                                                       new_controller->repo->medicaments[j]->price,
                                                                                       new_controller->repo->medicaments[j]->concentration));
                new_controller->repo->medicaments[j] = copy_medicine(new_medicine);
                destroy_medicine(new_medicine);
            }


    return new_controller;
}

Controller* sort_medicaments_with_substring(Controller* control, char* substring){
    /*
     * It creates a new controller ( and a new repository ) where it adds all the medicines that contains the given substring in the name.
     */
    Repository* new_repository = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* new_control = create_controller(new_repository, new_undo, new_redo);

    for(int i = 0; i < control->repo->length; i++)
        if(strstr(get_name(control->repo->medicaments[i]), substring) != NULL)
            add_medicament(new_control->repo, create_medicament(control->repo->medicaments[i]->name,
                                                                   control->repo->medicaments[i]->quantity,
                                                                   control->repo->medicaments[i]->price,
                                                                   control->repo->medicaments[i]->concentration));

    return new_control;
}

Controller* top_price(Controller* control, int x){
    /*
     * It creates a new controller and it sorts the medicaments by the price in a descending order. It returns the new controller.
     */
    if(x < 0 || x > control->repo->length)
        return NULL;
    Medicine* new_medicine;

    Repository* new_repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* new_controller = create_controller(new_repo, new_undo, new_redo);

    for(int i = 0; i < control->repo->length; i++){
        add_medicament(new_controller->repo, create_medicament(control->repo->medicaments[i]->name,
                                                               control->repo->medicaments[i]->quantity,
                                                               control->repo->medicaments[i]->price,
                                                               control->repo->medicaments[i]->concentration));
    }
    for(int m = 0; m < new_controller->repo->length - 1; m++)
        for(int j = m + 1; j < new_controller->repo->length; j++)
            if(get_price(new_controller->repo->medicaments[m]) < get_price(new_controller->repo->medicaments[j])){
                new_medicine = new_controller->repo->medicaments[m];
                new_controller->repo->medicaments[m] = new_controller->repo->medicaments[j];
                new_controller->repo->medicaments[j] = new_medicine;
            }

    return new_controller;
}

Controller* sort_by_quantity(Controller* control, char* operation){
    /*
     * It returns a new controller with the medicaments sorted by quantity.
     */
    Medicine* new_medicine;

    Repository* new_repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* new_controller = create_controller(new_repo, new_undo, new_redo);

    for(int i = 0; i < control->repo->length; i++){
        add_medicament(new_controller->repo, create_medicament(control->repo->medicaments[i]->name,
                                                               control->repo->medicaments[i]->quantity,
                                                               control->repo->medicaments[i]->price,
                                                               control->repo->medicaments[i]->concentration));
    }

    for(int i = 0; i < new_controller->repo->length - 1; i++)
        for(int j = i + 1; j < new_controller->repo->length; j++)
            if((strcmp(operation,"ascending") == 0 && get_quantity(new_controller->repo->medicaments[i]) > get_quantity(new_controller->repo->medicaments[j]))
               || (strcmp(operation,"descending") == 0 && get_quantity(new_controller->repo->medicaments[i]) < get_quantity(new_controller->repo->medicaments[j]))){
                new_medicine = new_controller->repo->medicaments[i];
                new_controller->repo->medicaments[i] = new_controller->repo->medicaments[j];
                new_controller->repo->medicaments[j] = new_medicine;
            }

    return new_controller;
}

Controller* sort_price_with_a_given_substring(Controller* control, char* substring){
    /*
     * It creates a new controller that contain only the medicines with the given substring and it sorts it by price in a descending order.
     */
    Repository* new_repository = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* new_control = create_controller(new_repository, new_undo, new_redo);
    Medicine* new_medicine;

    for(int i = 0; i < control->repo->length; i++)
        if(strstr(get_name(control->repo->medicaments[i]), substring) != NULL)
            add_medicament(new_control->repo, create_medicament(control->repo->medicaments[i]->name,
                                                                control->repo->medicaments[i]->quantity,
                                                                control->repo->medicaments[i]->price,
                                                                control->repo->medicaments[i]->concentration));
    if (new_control->repo->length == 0)
        return NULL;
    for(int i = 0; i < new_control->repo->length - 1; i++)
        for(int j = i + 1; j < new_control->repo->length; j++)
            if(get_price(new_control->repo->medicaments[i]) < get_price(new_control->repo->medicaments[j])){
                new_medicine = new_control->repo->medicaments[i];
                new_control->repo->medicaments[i] = new_control->repo->medicaments[j];
                new_control->repo->medicaments[j] = new_medicine;
            }
    return new_control;
}