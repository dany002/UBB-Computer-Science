#pragma once

typedef struct {
	char* name;
	float concentration;
	float price;
	int quantity;
    int id;
}Medicine;

Medicine* create_medicament(char* name, int quantity, float price, float concentration);

void destroy_medicine(Medicine* m);

char* get_name(Medicine* m);

float get_concentration(Medicine* m);

float get_price(Medicine* m);

int get_quantity(Medicine* m);

Medicine* copy_medicine(Medicine*);