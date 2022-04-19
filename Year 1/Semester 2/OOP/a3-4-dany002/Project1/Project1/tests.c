//
// Created by SenZatIonALL on 3/5/2022.
//

#include "tests.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include "Medicine.h"
#include "Repository.h"
#include <string.h>
#include "Controller.h"
#include "Validator.h"

/******************************************************** Medicine.c **************************************************/

void test_get_name(){
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    assert(strcmp(m->name, "Nurofen") == 0);
    destroy_medicine(m);
}

void test_get_concentration(){
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    assert(m->concentration == 98.5);
    destroy_medicine(m);
}

void test_get_price(){
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    assert(m->price == 16.5);
    destroy_medicine(m);
}

void test_get_quantity(){
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    assert(m->quantity == 13);
    destroy_medicine(m);
}

void test_copy_medicine(){
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = copy_medicine(m);
    assert(m->concentration == m1->concentration);
    assert(m->quantity == m1->quantity);
    assert(m->price == m1->price);
    assert(strcmp(m->name, m1->name) == 0);
    destroy_medicine(m1);
    destroy_medicine(m);
}


void test_medicine(){
    test_get_name();
    test_get_concentration();
    test_get_price();
    test_get_quantity();
    test_copy_medicine();
}

/******************************************************** repository.c **************************************************/


void test_add_medicament__return_0__medicament_already_exists(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("Nurofen", 25, (float)16.5, (float)98.5);
    add_medicament(repo, m);
    assert(add_medicament(repo, m1) == 0);
    assert(get_quantity(repo->medicaments[0]) == 38);
    destroy_medicine(m1);
    destroy_repository(repo);
}

void test_add_medicament__return_1__medicament_is_going_to_be_added_successfully(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    assert(add_medicament(repo, m) == 1);
    destroy_repository(repo);
}

void test_delete_medicament__return_0__medicament_doesnt_exist(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    add_medicament(repo, m);
    assert(repo->length == 1);
    assert(delete_medicament(repo, "Paracetamol", (float)98.5) == 0);
    assert(repo->length == 1);
    destroy_repository(repo);
}

void test_delete_medicament__return_1__medicament_is_successfully_deleted(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    add_medicament(repo, m);
    assert(repo->length == 1);
    assert(delete_medicament(repo, "Nurofen", (float)98.5) == 1);
    assert(repo->length == 0);
    destroy_repository(repo);
}

void test_return_position_for_a_medicament__return_i_th_position__the_medicament_exists_in_the_repository(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    assert(return_position_for_a_medicament(repo, "CBD", (float)65.8) == 1);
    destroy_repository(repo);
}

void test_return_position_for_a_medicament__return_minus_1__the_medicament_doesnt_exist_in_the_repository(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    assert(return_position_for_a_medicament(repo, "CBD", (float)69) == -1);
    destroy_repository(repo);
}

void test_update_quantity_repo__return_1__the_quantity_is_successfully_updated(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    assert(get_quantity(repo->medicaments[0]) == 13);
    assert(update_quantity_repo(repo, "Nurofen", (float)98.5, 19) == 1);
    assert(get_quantity(repo->medicaments[0]) == 19);
    destroy_repository(repo);
}

void test_update_quantity_repo__return_0__the_medicament_doesnt_exist_in_the_repository(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    assert(update_quantity_repo(repo, "Ibuprofen", (float)98.5, 19) == 0);
    destroy_repository(repo);
}

void test_update_price_repo__return_1__the_price_is_successfully_updated(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    assert(get_price(repo->medicaments[0]) == 16.5);
    assert(update_price_repo(repo, "Nurofen", (float)98.5, (float)233.4) == 1);
    assert(get_price(repo->medicaments[0]) == (float)233.4);
    destroy_repository(repo);
}

void test_update_price_repo__return_0__the_medicament_doesnt_exist_in_the_repository(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    assert(update_price_repo(repo, "Ibuprofen", (float)98.5, 19) == 0);
    destroy_repository(repo);
}

void test_create_a_specific_medicament__is_going_to_return_the_medicament_from_the_repository(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    Medicine* m3 = create_a_specific_medicament(repo, "CBD", (float)65.8);
    assert(m3->quantity == 17);
    assert(m3->price == (float)30);
    destroy_repository(repo);
}

void test_create_a_specific_medicament__is_going_to_return_NULL__the_drug_doesnt_exist_in_the_repository(){
    Repository *repo = create_repository();
    Medicine *m = create_medicament("Nurofen", 13, (float)16.5, (float)98.5);
    Medicine *m1 = create_medicament("CBD", 17, (float)30, (float)65.8);
    Medicine *m2 = create_medicament("Paracetamol", 19, (float)14.7, (float)73.9);
    add_medicament(repo, m);
    add_medicament(repo, m1);
    add_medicament(repo, m2);
    Medicine* m3 = create_a_specific_medicament(repo, "CBD", (float)68);
    assert(m3 == NULL);
    destroy_repository(repo);
}

void test_repository(){
    test_add_medicament__return_0__medicament_already_exists();
    test_add_medicament__return_1__medicament_is_going_to_be_added_successfully();
    test_delete_medicament__return_0__medicament_doesnt_exist();
    test_delete_medicament__return_1__medicament_is_successfully_deleted();
    test_return_position_for_a_medicament__return_i_th_position__the_medicament_exists_in_the_repository();
    test_return_position_for_a_medicament__return_minus_1__the_medicament_doesnt_exist_in_the_repository();
    test_update_quantity_repo__return_1__the_quantity_is_successfully_updated();
    test_update_quantity_repo__return_0__the_medicament_doesnt_exist_in_the_repository();
    test_update_price_repo__return_1__the_price_is_successfully_updated();
    test_update_price_repo__return_0__the_medicament_doesnt_exist_in_the_repository();
    test_create_a_specific_medicament__is_going_to_return_the_medicament_from_the_repository();
    test_create_a_specific_medicament__is_going_to_return_NULL__the_drug_doesnt_exist_in_the_repository();
}


/******************************************************** Controller.c **************************************************/

void test_add__with_valid_data__is_going_to_add_successfully_in_repository(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    assert(add(control, "Nurofen", 13, (float)16.5, (float)98.5) == 1);

    destroy_controller(control);
}

void test_add__with_valid_data__is_going_to_update_the_quantity_the_medicament_is_already_in_repository(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float)16.5, (float)98.5);
    assert(add(control, "Nurofen", 17, (float)16.5, (float)98.5 ) == 0);
    assert(get_quantity(control->repo->medicaments[0]) == 30);

    destroy_controller(control);
}

void test_add__return_minus_one__quantity_is_less_than_0(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    assert(add(control, "Nurofen", -4, (float)16.5, (float)98.5 ) == -1);
    destroy_controller(control);
}

void test_add__return_minus_two__price_is_less_than_0(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    assert(add(control, "Nurofen", 13, (float)-3.4, (float)98.5 ) == -2);
    destroy_controller(control);
}

void test_add__return_minus_three__concentration_is_less_than_0_or_greater_than_100(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    assert(add(control, "Nurofen", 13, (float)16.5, (float)-3.5 ) == -3);
    assert(add(control, "Nurofen", 13, (float)16.5, (float)103 ) == -3);
    destroy_controller(control);
}

void test_add__return_minus_four__name_doesnt_contain_only_digits(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    assert(add(control, "Nur0fen", 13, (float)16.5, (float)98.5 ) == -4);
    destroy_controller(control);
}

void test_delete__with_valid_data__is_going_to_remove_from_repository(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float)16.5, (float)98.5 );
    assert(control->repo->length == 1);
    assert(delete(control, "Nurofen", (float)98.5) == 1);
    assert(control->repo->length == 0);
    destroy_controller(control);
}

void test_delete__with_valid_data__wont_remove_from_repository_medicament_not_found(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float)16.5, (float)98.5);
    assert(control->repo->length == 1);
    assert(delete(control, "Ibuprsofen", (float)93.5) == 0);
    assert(control->repo->length == 1);
    destroy_controller(control);
}

void test_delete__return_minus_one__concentration_is_less_than_0_or_greater_than_100() {
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(control->repo->length == 1);
    assert(delete(control, "Nurofen", (float) -1.3) == -1);
    assert(delete(control, "Nurofen", (float) 101) == -1);
    assert(control->repo->length == 1);
    destroy_controller(control);
}

void test_delete__return_minus_two__name_doesnt_contain_only_digits(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(control->repo->length == 1);
    assert(delete(control, "Nur0fen", (float) 98.5) == -2);
    assert(control->repo->length == 1);
    destroy_controller(control);
}

void test_update_quantity__with_valid_data__is_going_to_update_the_quantity_for_the_given_medicament(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(get_quantity(control->repo->medicaments[0]) == 13);
    assert(update_quantity(control, "Nurofen", (float) 98.5, 17) == 1);
    assert(get_quantity(control->repo->medicaments[0]) == 17);
    destroy_controller(control);
}

void test_update_quantity__with_valid_data__is_going_to_return_0_because_the_medicament_is_not_found(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_quantity(control, "Ibuprofen", (float) 98.5, 17) == 0);
    destroy_controller(control);
}

void test_update_quantity__return_minus_one__concentration_is_less_than_0_or_greater_than_100(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_quantity(control, "Nurofen", (float) -3, 17) == -1);
    assert(update_quantity(control, "Nurofen", (float) 104, 17) == -1);
    destroy_controller(control);
}

void test_update_quantity__return_minus_two__name_doesnt_contain_only_letters(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_quantity(control, "Nur0fen", (float) 98.5, 17) == -2);
    destroy_controller(control);
}

void test_update_quantity__return_minus_three__quantity_is_less_than_0(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_quantity(control, "Nurofen", (float) 98.5, -14) == -3);
    destroy_controller(control);
}

void test_update_price__with_valid_data__is_going_to_update_the_quantity_for_the_given_medicament(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(get_price(control->repo->medicaments[0]) == 16.5);
    assert(update_price(control, "Nurofen", (float) 98.5, (float)31.4) == 1);
    assert(get_price(control->repo->medicaments[0]) == (float)31.4);
    destroy_controller(control);
}

void test_update_price__with_valid_data__is_going_to_return_0_because_the_medicament_is_not_found(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_price(control, "Ibuprofen", (float) 98.5, 17) == 0);
    destroy_controller(control);
}

void test_update_price__return_minus_one__concentration_is_less_than_0_or_greater_than_100(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_price(control, "Nurofen", (float) -3, 17) == -1);
    assert(update_price(control, "Nurofen", (float) 104, 17) == -1);
    destroy_controller(control);
}


void test_update_price__return_minus_two__name_doesnt_contain_only_letters(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_price(control, "Nur0fen", (float) 98.5, 17) == -2);
    destroy_controller(control);
}

void test_update_price__return_minus_three__price_is_less_than_0(){
    Repository *repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    assert(update_price(control, "Nurofen", (float) 98.5, -14) == -3);
    destroy_controller(control);
}

void test_sort_medicaments__return_Controller__sorted_ascending_by_name(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "CBD", 19, (float) 14.3, (float) 23.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    control = sort_medicaments(control);
    assert(strcmp(get_name(control->repo->medicaments[0]), "CBD") == 0);
    assert(strcmp(get_name(control->repo->medicaments[1]), "Nurofen") == 0);
    assert(strcmp(get_name(control->repo->medicaments[2]), "Paracetamol") == 0);
    destroy_controller(control);
}

void test_sort_medicaments_with_substring__return_controller__with_the_medicines_that_contain_the_given_substring(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "CBD", 19, (float) 14.3, (float) 23.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    add(control, "Crofas", 43, (float) 13.4, (float) 6.42);
    Controller* new_control;
    new_control = sort_medicaments_with_substring(control, "rof");
    assert(strcmp(get_name(new_control->repo->medicaments[0]), "Nurofen") == 0);
    assert(strcmp(get_name(new_control->repo->medicaments[1]), "Crofas") == 0);
    assert(get_quantity(new_control->repo->medicaments[0]) == 13);
    assert(get_quantity(new_control->repo->medicaments[1]) == 43);
    assert(get_price(new_control->repo->medicaments[0]) == (float)16.5);
    assert(get_price(new_control->repo->medicaments[1]) == (float)13.4);
    assert(get_concentration(new_control->repo->medicaments[0]) == (float)98.5);
    assert(get_concentration(new_control->repo->medicaments[1]) == (float)6.42);
    destroy_controller(new_control);
    destroy_controller(control);
}

void test_top_price__bad_input__return_NULL(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "CBD", 19, (float) 14.3, (float) 23.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    add(control, "Crofas", 43, (float) 13.4, (float) 6.42);
    assert(top_price(control, 5) == NULL);
    assert(top_price(control, -3) == NULL);
    destroy_controller(control);
}

void test_top_price__with_valid_data__is_going_to_return_an_order_controller(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Ibuprofen", 107, (float)15.4, (float)70.15);
    add(control, "CBD", 1100, (float)90.5, (float)80.6);
    add(control, "Morphine", 300, (float)30.12, (float)25.37);
    add(control, "Paracetamol", 200, (float)69.99, (float)20);
    add(control, "Xanax", 50, (float)130.47, (float)80.14);
    add(control, "Adderall", 123, (float)189.4, (float)15.41);
    add(control, "Syrup", 705, (float)30, (float)5.13);
    add(control, "Nurofen", 458, (float)20.7, (float)15.18);
    add(control, "Patch", 853, (float)5, (float)0.01);
    add(control, "Vedixin", 153, (float)30.2, (float)18.3);
    Controller* new_control;
    new_control = top_price(control, 2);
    assert(get_price(new_control->repo->medicaments[0]) == get_price(control->repo->medicaments[5]));
    assert(get_price(new_control->repo->medicaments[1]) == get_price(control->repo->medicaments[4]));
    destroy_controller(new_control);
    destroy_controller(control);
}

void test_sort_by_quantity__ascending(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    add(control, "CBD", 19, (float) 14.3, (float) 23.5);
    add(control, "Crofas", 43, (float) 13.4, (float) 6.42);
    Controller* new_control;
    new_control = sort_by_quantity(control, "ascending");
    assert(get_quantity(new_control->repo->medicaments[0]) == get_quantity(control->repo->medicaments[0]));
    assert(get_quantity(new_control->repo->medicaments[1]) == get_quantity(control->repo->medicaments[2]));
    assert(get_quantity(new_control->repo->medicaments[2]) == get_quantity(control->repo->medicaments[1]));
    assert(get_quantity(new_control->repo->medicaments[3]) == get_quantity(control->repo->medicaments[3]));
    destroy_controller(new_control);
    destroy_controller(control);
}

void test_sort_by_quantity__descending(){
    Repository* repo = create_repository();
    Undo* undo = create_undo();
    Undo* redo = create_undo();
    Controller* control = create_controller(repo, undo, redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    add(control, "CBD", 19, (float) 14.3, (float) 23.5);
    add(control, "Crofas", 43, (float) 13.4, (float) 6.42);
    Controller* new_control;
    new_control = sort_by_quantity(control, "descending");
    assert(get_quantity(new_control->repo->medicaments[0]) == get_quantity(control->repo->medicaments[3]));
    assert(get_quantity(new_control->repo->medicaments[1]) == get_quantity(control->repo->medicaments[1]));
    assert(get_quantity(new_control->repo->medicaments[2]) == get_quantity(control->repo->medicaments[2]));
    assert(get_quantity(new_control->repo->medicaments[3]) == get_quantity(control->repo->medicaments[0]));
    destroy_controller(new_control);
    destroy_controller(control);
}

void test_undo_length_is_0__is_going_to_return_minus_one(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    undo(control);
    assert(control->repo->length == 1);
    undo(control);
    assert(control->repo->length == 0);
    assert(undo(control) == -1);
    destroy_controller(control);
}

void test_undo__is_going_to_add_back_the_drug(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->length == 2);
    undo(control);
    delete(control, "Nurofen", (float)98.5);
    assert(control->repo->length == 0);
    undo(control);
    assert(control->repo->length == 1);
    destroy_controller(control);
}

void test_undo__is_going_to_remove_from_the_repo_what_i_added(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->length == 2);
    undo(control);
    assert(control->repo->length == 1);
    undo(control);
    assert(control->repo->length == 0);
    destroy_controller(control);
}

void test_undo__is_going_to_undo_the_price_that_was_before(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->medicaments[0]->price == (float)16.5);
    update_price(control, "Nurofen", (float)98.5, (float)486.5);
    assert(control->repo->medicaments[0]->price == (float)486.5);
    undo(control);
    assert(control->repo->medicaments[0]->price == (float)16.5);
    destroy_controller(control);
}

void test_undo__is_going_to_undo_the_quantity_that_was_before(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->medicaments[0]->quantity == 13);
    update_quantity(control, "Nurofen", (float)98.5, 300);
    assert(control->repo->medicaments[0]->quantity == 300);
    undo(control);
    assert(control->repo->medicaments[0]->quantity == 13);
    destroy_controller(control);
}

void test_redo__length_is_0__return_minus_one(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(redo(control) == -1);
    destroy_controller(control);
}

void test_redo__is_going_to_add_back_what_i_ve_just_undo(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->length == 2);
    undo(control);
    assert(control->repo->length == 1);
    redo(control);
    assert(control->repo->length == 2);
    destroy_controller(control);
}

void test_redo__is_going_to_remove_what_i_ve_deleted_before_undo(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->length == 2);
    delete(control, "Nurofen", (float)98.5);
    assert(control->repo->length == 1);
    undo(control);
    assert(control->repo->length == 2);
    redo(control);
    assert(control->repo->length == 1);
    destroy_controller(control);
}

void test_redo__update_quantity(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->medicaments[0]->quantity == 13);
    update_quantity(control, "Nurofen", (float)98.5, 300);
    assert(control->repo->medicaments[0]->quantity == 300);
    undo(control);
    assert(control->repo->medicaments[0]->quantity == 13);
    redo(control);
    assert(control->repo->medicaments[0]->quantity == 300);
    destroy_controller(control);
}

void test_redo__update_price(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    add(control, "Nurofen", 13, (float) 16.5, (float) 98.5);
    add(control, "Paracetamol", 42, (float) 72.4, (float) 60.42);
    assert(control->repo->medicaments[0]->price == (float)16.5);
    update_price(control, "Nurofen", (float)98.5, (float)486.5);
    assert(control->repo->medicaments[0]->price == (float)486.5);
    undo(control);
    assert(control->repo->medicaments[0]->price == (float)16.5);
    redo(control);
    assert(control->repo->medicaments[0]->price == (float)486.5);
    destroy_controller(control);
}

void test_controller(){
    test_add__with_valid_data__is_going_to_add_successfully_in_repository();
    test_add__with_valid_data__is_going_to_update_the_quantity_the_medicament_is_already_in_repository();
    test_add__return_minus_one__quantity_is_less_than_0();
    test_add__return_minus_two__price_is_less_than_0();
    test_add__return_minus_three__concentration_is_less_than_0_or_greater_than_100();
    test_add__return_minus_four__name_doesnt_contain_only_digits();
    test_delete__with_valid_data__is_going_to_remove_from_repository();
    test_delete__with_valid_data__wont_remove_from_repository_medicament_not_found();
    test_delete__return_minus_one__concentration_is_less_than_0_or_greater_than_100();
    test_delete__return_minus_two__name_doesnt_contain_only_digits();
    test_update_quantity__with_valid_data__is_going_to_update_the_quantity_for_the_given_medicament();
    test_update_quantity__with_valid_data__is_going_to_return_0_because_the_medicament_is_not_found();
    test_update_quantity__return_minus_one__concentration_is_less_than_0_or_greater_than_100();
    test_update_quantity__return_minus_two__name_doesnt_contain_only_letters();
    test_update_quantity__return_minus_three__quantity_is_less_than_0();
    test_update_price__with_valid_data__is_going_to_update_the_quantity_for_the_given_medicament();
    test_update_price__with_valid_data__is_going_to_return_0_because_the_medicament_is_not_found();
    test_update_price__return_minus_one__concentration_is_less_than_0_or_greater_than_100();
    test_update_price__return_minus_two__name_doesnt_contain_only_letters();
    test_update_price__return_minus_three__price_is_less_than_0();
    test_sort_medicaments__return_Controller__sorted_ascending_by_name();
    test_sort_medicaments_with_substring__return_controller__with_the_medicines_that_contain_the_given_substring();
    test_top_price__bad_input__return_NULL();
    test_top_price__with_valid_data__is_going_to_return_an_order_controller();
    test_sort_by_quantity__ascending();
    test_sort_by_quantity__descending();
    test_undo_length_is_0__is_going_to_return_minus_one();
    test_undo__is_going_to_add_back_the_drug();
    test_undo__is_going_to_remove_from_the_repo_what_i_added();
    test_undo__is_going_to_undo_the_price_that_was_before();
    test_undo__is_going_to_undo_the_quantity_that_was_before();
    test_redo__length_is_0__return_minus_one();
    test_redo__is_going_to_add_back_what_i_ve_just_undo();
    test_redo__is_going_to_remove_what_i_ve_deleted_before_undo();
    test_redo__update_price();
    test_redo__update_quantity();
}
/******************************************************** Undo.c **************************************************/

void test_add_drug(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    Medicine* med = create_medicament("Nurofen", 13, (float) 16.5, (float) 98.5);
    add_drug(new_undo, med);
    assert(strcmp(control->undo->drugs[0]->name,"Nurofen") == 0);
    assert(control->undo->drugs[0]->quantity == 13);
    assert(control->undo->drugs[0]->price == (float)16.5);
    assert(control->undo->drugs[0]->concentration == (float)98.5);
    assert(control->undo->drugs[0]->id == 1);
    assert(control->undo->length == 1);
    destroy_controller(control);
}

void test_delete_drug(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    Medicine* med = create_medicament("Nurofen", 13, (float) 16.5, (float) 98.5);
    delete_drug(new_undo, med);
    assert(strcmp(control->undo->drugs[0]->name,"Nurofen") == 0);
    assert(control->undo->drugs[0]->quantity == 13);
    assert(control->undo->drugs[0]->price == (float)16.5);
    assert(control->undo->drugs[0]->concentration == (float)98.5);
    assert(control->undo->drugs[0]->id == 2);
    assert(control->undo->length == 1);
    destroy_controller(control);
}

void test_update_drug_by_quantity(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    Medicine* med = create_medicament("Nurofen", 13, (float) 16.5, (float) 98.5);
    update_drug_by_quantity(new_undo, med);
    assert(strcmp(control->undo->drugs[0]->name,"Nurofen") == 0);
    assert(control->undo->drugs[0]->quantity == 13);
    assert(control->undo->drugs[0]->price == (float)16.5);
    assert(control->undo->drugs[0]->concentration == (float)98.5);
    assert(control->undo->drugs[0]->id == 3);
    assert(control->undo->length == 1);
    destroy_controller(control);
}

void test_update_drug_by_price(){
    Repository* repo = create_repository();
    Undo* new_undo = create_undo();
    Undo* new_redo = create_undo();
    Controller* control = create_controller(repo, new_undo, new_redo);
    Medicine* med = create_medicament("Nurofen", 13, (float) 16.5, (float) 98.5);
    update_drug_by_price(new_undo, med);
    assert(strcmp(control->undo->drugs[0]->name,"Nurofen") == 0);
    assert(control->undo->drugs[0]->quantity == 13);
    assert(control->undo->drugs[0]->price == (float)16.5);
    assert(control->undo->drugs[0]->concentration == (float)98.5);
    assert(control->undo->drugs[0]->id == 4);
    assert(control->undo->length == 1);
    destroy_controller(control);
}

void test_undo(){
    test_add_drug();
    test_delete_drug();
    test_update_drug_by_quantity();
    test_update_drug_by_price();
}

/******************************************************** Validator.c **************************************************/

void test_validator_quantity__return_0__quantity_is_less_than_0(){
    assert(validator_quantity(-4) == 0);
}

void test_validator_quantity__return_1__quantity_is_greater_than_0(){
    assert(validator_quantity(13) == 1);
}

void test_validator_price__return_0__price_is_less_than_0(){
    assert(validator_price((float)-13.4) == 0);
}

void test_validator_price__return_1__price_is_greater_than_0(){
    assert(validator_price((float)14.5) == 1);
}

void test_validator_concentration__return_0__concentration_is_less_than_0_or_greater_than_100(){
    assert(validator_concentration((float)-3.4) == 0);
    assert(validator_concentration((float)103.4) == 0);
}

void test_validator_concentration__return_1__concentration_is_between_0_and_100(){
    assert(validator_concentration((float)84.31) == 1);
}

void test_validator_name__return_0__name_doesnt_contain_only_letters(){
    assert(validator_name("1bupr0fen") == 0);
    assert(validator_name("Ibu profen") == 0);
}

void test_validator_name__return_1__name_has_only_letters(){
    assert(validator_name("Paracetamol") == 1);
}


void test_validator(){
    test_validator_concentration__return_0__concentration_is_less_than_0_or_greater_than_100();
    test_validator_concentration__return_1__concentration_is_between_0_and_100();
    test_validator_name__return_0__name_doesnt_contain_only_letters();
    test_validator_name__return_1__name_has_only_letters();
    test_validator_quantity__return_0__quantity_is_less_than_0();
    test_validator_quantity__return_1__quantity_is_greater_than_0();
    test_validator_price__return_0__price_is_less_than_0();
    test_validator_price__return_1__price_is_greater_than_0();
}

void test_all(){
    test_medicine();
    test_repository();
    test_controller();
    test_validator();
    test_undo();
}
