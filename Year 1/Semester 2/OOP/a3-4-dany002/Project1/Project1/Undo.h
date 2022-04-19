//
// Created by SenZatIonALL on 3/10/2022.
//
#pragma once
#include "Medicine.h"

typedef struct{
    int length;
    Medicine* drugs[100];
}Undo;

Undo* create_undo();

void destroy_undo(Undo* undo);

void add_drug(Undo* undo, Medicine* medicine);

void delete_drug(Undo* undo, Medicine* medicine);

void update_drug_by_quantity(Undo* undo, Medicine* medicine);

void update_drug_by_price(Undo* undo, Medicine* medicine);