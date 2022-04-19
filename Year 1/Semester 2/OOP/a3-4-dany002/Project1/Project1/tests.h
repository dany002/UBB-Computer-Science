//
// Created by SenZatIonALL on 3/5/2022.
//
#pragma once

void test_get_name();

void test_all();

void test_get_concentration();

void test_get_price();

void test_get_quantity();

void test_copy_medicine();

void test_medicine();

void test_add_medicament__return_0__medicament_already_exists();

void test_add_medicament__return_1__medicament_is_going_to_be_added_successfully();

void test_delete_medicament__return_0__medicament_doesnt_exist();

void test_delete_medicament__return_1__medicament_is_successfully_deleted();

void test_return_position_for_a_medicament__return_i_th_position__the_medicament_exists_in_the_repository();

void test_return_position_for_a_medicament__return_minus_1__the_medicament_doesnt_exist_in_the_repository();

void test_update_quantity_repo__return_1__the_quantity_is_successfully_updated();

void test_update_quantity_repo__return_0__the_medicament_doesnt_exist_in_the_repository();

void test_update_price_repo__return_1__the_price_is_successfully_updated();

void test_update_price_repo__return_0__the_medicament_doesnt_exist_in_the_repository();

void test_create_a_specific_medicament__is_going_to_return_the_medicament_from_the_repository();

void test_create_a_specific_medicament__is_going_to_return_NULL__the_drug_doesnt_exist_in_the_repository();

void test_repository();

void test_add__with_valid_data__is_going_to_add_successfully_in_repository();

void test_add__with_valid_data__is_going_to_update_the_quantity_the_medicament_is_already_in_repository();

void test_add__return_minus_one__quantity_is_less_than_0();

void test_add__return_minus_two__price_is_less_than_0();

void test_add__return_minus_three__concentration_is_less_than_0_or_greater_than_100();

void test_add__return_minus_four__name_doesnt_contain_only_digits();

void test_delete__with_valid_data__is_going_to_remove_from_repository();

void test_delete__with_valid_data__wont_remove_from_repository_medicament_not_found();

void test_delete__return_minus_one__concentration_is_less_than_0_or_greater_than_100();

void test_delete__return_minus_two__name_doesnt_contain_only_digits();

void test_update_quantity__with_valid_data__is_going_to_update_the_quantity_for_the_given_medicament();

void test_update_quantity__with_valid_data__is_going_to_return_0_because_the_medicament_is_not_found();

void test_update_quantity__return_minus_one__concentration_is_less_than_0_or_greater_than_100();

void test_update_quantity__return_minus_two__name_doesnt_contain_only_letters();

void test_update_quantity__return_minus_three__quantity_is_less_than_0();

void test_update_price__with_valid_data__is_going_to_update_the_quantity_for_the_given_medicament();

void test_update_price__with_valid_data__is_going_to_return_0_because_the_medicament_is_not_found();

void test_update_price__return_minus_one__concentration_is_less_than_0_or_greater_than_100();

void test_update_price__return_minus_two__name_doesnt_contain_only_letters();

void test_update_price__return_minus_three__price_is_less_than_0();

void test_sort_medicaments__return_Controller__sorted_ascending_by_name();

void test_sort_medicaments_with_substring__return_controller__with_the_medicines_that_contain_the_given_substring();

void test_controller();

void test_validator_quantity__return_0__quantity_is_less_than_0();

void test_validator_quantity__return_1__quantity_is_greater_than_0();

void test_validator_price__return_0__price_is_less_than_0();

void test_validator_price__return_1__price_is_greater_than_0();

void test_validator_concentration__return_0__concentration_is_less_than_0_or_greater_than_100();

void test_validator_concentration__return_1__concentration_is_between_0_and_100();

void test_validator_name__return_0__name_doesnt_contain_only_letters();

void test_validator_name__return_1__name_has_only_letters();

void test_validator();

void test_top_price__with_valid_data__is_going_to_return_an_order_controller();

void test_top_price__bad_input__return_NULL();

void test_sort_by_quantity__ascending();

void test_sort_by_quantity__descending();

void test_undo_length_is_0__is_going_to_return_minus_one();

void test_undo__is_going_to_add_back_the_drug();

void test_undo__is_going_to_remove_from_the_repo_what_i_added();

void test_undo__is_going_to_undo_the_price_that_was_before();

void test_undo__is_going_to_undo_the_quantity_that_was_before();

void test_redo__length_is_0__return_minus_one();

void test_redo__is_going_to_add_back_what_i_ve_just_undo();

void test_redo__is_going_to_remove_what_i_ve_deleted_before_undo();

void test_redo__update_quantity();

void test_redo__update_price();

void test_add_drug();

void test_delete_drug();

void test_update_drug_by_quantity();

void test_update_drug_by_price();

void test_undo();