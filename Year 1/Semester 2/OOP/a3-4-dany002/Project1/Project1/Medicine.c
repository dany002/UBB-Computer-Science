#include "Medicine.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

Medicine* create_medicament(char* name, int quantity, float price, float concentration)
{
    /*
     * This function creates the medicament, and it uses dynamic memory allocation. It return the medicament.
     */
    Medicine* m = malloc(sizeof(Medicine));
    m->name = malloc(sizeof(char) * (strlen(name) + 1));
    if(m->name != NULL)
        strcpy(m->name, name);
    m->quantity = quantity;
    m->price = price;
    m->concentration = concentration;
    return m;
}

void destroy_medicine(Medicine* m)
{
    /*
     * It destroys the medicine structure ( using free ).
     */
    if (m == NULL)
        return;
    free(m->name);
    free(m);
    m = NULL;
}


char* get_name(Medicine* m) {
    /*
     * It returns the name of the medicine.
     */
    return m->name;
}

float get_concentration(Medicine* m) {
    /*
     * It returns the concentration of the medicine.
     */
    return m->concentration;
}


float get_price(Medicine* m) {
    /*
     * It returns the price of the medicine.
     */
    return m->price;
}

int get_quantity(Medicine* m) {
    /*
     * It returns the quantity of the medicine.
     */
    return m->quantity;
}

Medicine* copy_medicine(Medicine* m) {
    /*
     * It returns a copy of the medicine.
     */
    return create_medicament(m->name, m->quantity, m->price, m->concentration);
}