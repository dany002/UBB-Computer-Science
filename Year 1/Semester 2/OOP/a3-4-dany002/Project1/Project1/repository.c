#include "Repository.h"
#include <stdio.h>
#include "Medicine.h"
#include <string.h>
#include <stdlib.h>

Repository* create_repository() {
    /*
     * It creates a repository using dynamic memory allocation, and it returns the repository.
     */
	Repository* repo = malloc(sizeof(Repository));
    if(repo == NULL)
        return NULL;
	repo->length = 0;
	return repo;
}

void destroy_repository(Repository* repo) {
    /*
     * It destroys the repository using function free.
     */
	if (repo == NULL)
		return;
	for (int i = 0; i < repo->length; i++)
		destroy_medicine(repo->medicaments[i]);
	free(repo);
}

int add_medicament(Repository* repo, Medicine* medicament) {
    /*
     * It adds a medicament to the repository and if it's already in repository, it will modify its quantity ( in this case it will return 0 ) and
     * if the medicament hasn't been before in the repository it will return 1.
     */
	for (int i = 0; i < repo->length; i++)
		if (strcmp(get_name(medicament), get_name(repo->medicaments[i])) == 0 && get_concentration(medicament) == get_concentration(repo->medicaments[i])) {
			repo->medicaments[i]->quantity += medicament->quantity;
			return 0; // the quantity is modified.
		}
	repo->medicaments[repo->length++] = copy_medicine(medicament);
	return 1;
}

int delete_medicament(Repository* repo, char *name, float concentration){
    /*
     * It deletes the given medicament from the repository if it exists and it returns 1 and if it doesn't exist is going to return 0.
     */

    for(int i = 0; i < repo->length; i++)
        if(strcmp(get_name(repo->medicaments[i]), name) == 0 && get_concentration(repo->medicaments[i]) == concentration){
            for(int j = i; j < repo->length - 1; j++)
                repo->medicaments[j] = repo->medicaments[j+1];
            repo->length -= 1;
            return 1;
        }

    return 0;
}

int return_position_for_a_medicament(Repository* repo, char* name, float concentration){
    /*
     * It returns the position in the repository for a given medicament; -1 if it's not found.
     */
    for(int i = 0; i < repo->length; i++)
        if(strcmp(get_name(repo->medicaments[i]), name) == 0 && get_concentration(repo->medicaments[i]) == concentration)
            return i;
    return -1;
}

int update_quantity_repo(Repository* repo, char* name, float concentration, int quantity){
    /*
     * First it checks if the medicine that has to be updated exists in the repository ( returns 0 if it doesn't exist ) and
     * if it exists is going to update the quantity and return 1.
     */
    int i = return_position_for_a_medicament(repo, name, concentration);
    if(i == -1)
        return 0;
    repo->medicaments[i]->quantity = quantity;
    return 1;
}

int update_price_repo(Repository* repo, char* name, float concentration, float price){
    /*
     * First it checks if the medicine that has to be updated exists in the repository ( returns 0 if it doesn't exist ) and
     * if it exists is going to update the price and return 1.
     */
    int i = return_position_for_a_medicament(repo, name, concentration);
    if(i == -1)
        return 0;
    repo->medicaments[i]->price = price;
    return 1;
}

Medicine* create_a_specific_medicament(Repository* repo, char* name, float concentration){
    /*
     * It returns the drug from the repository with that name and concentration.
     */
    int i = return_position_for_a_medicament(repo, name, concentration);
    if(i == -1)
        return NULL;
    Medicine* med = create_medicament(get_name(repo->medicaments[i]), get_quantity(repo->medicaments[i]), get_price(repo->medicaments[i]),
                                      get_concentration(repo->medicaments[i]));
    return med;
}