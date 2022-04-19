#pragma once
#include "Medicine.h"

typedef struct {
	Medicine* medicaments[100];
	int length;
}Repository;

Repository* create_repository();

void destroy_repository(Repository* repo);

int add_medicament(Repository* repo, Medicine* medicament);

int delete_medicament(Repository* repo, char *name, float concentration);

int update_quantity_repo(Repository* repo, char* name, float concentration, int quantity);

int update_price_repo(Repository* repo, char* name, float concentration, float price);

int return_position_for_a_medicament(Repository* repo, char* name, float concentration);

Medicine* create_a_specific_medicament(Repository* repo, char* name, float concentration);