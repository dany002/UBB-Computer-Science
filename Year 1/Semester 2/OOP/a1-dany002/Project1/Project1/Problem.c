#include <stdio.h>
#include <assert.h>

typedef struct Vector {
	int length;
	int a[100];
}Vector;


int prime(int x) {
	/*
		return 1 if the number is prime and 0 otherwise.
	*/
	if (x < 2)
		return 0;
	if (x == 2)
		return 1;
	if (x % 2 == 0)
		return 0;
	for (int d = 3; d <= x / 2; d += 2)
		if (x % d == 0)
			return 0;
	return 1;
}


int check_if_two_numbers_contain_the_same_digits(int x, int y) {
	/*
		It checks if 2 numbers contain the same digits by using 2 arrays and if they contain the same digits it return 1 and 0 otherwise.
	*/
	int digits_for_first_one[10], digits_for_the_second_one[10];
	for (int i = 0; i <= 9; i++) {
		digits_for_first_one[i] = 0;
		digits_for_the_second_one[i] = 0;
	}
	if (x == 0 && y != 0 || x != 0 && y == 0)
		return 0;
	if (x < 0)
		x = -x;
	if (y < 0)
		y = -y;
	while (x) {
		digits_for_first_one[x % 10] = 1;
		x /= 10;
	}
	while (y) {
		digits_for_the_second_one[y % 10] = 1;
		y /= 10;
	}
	for (int i = 0; i <= 9; i++) 
		if (digits_for_first_one[i] != digits_for_the_second_one[i])
			return 0;

	return 1;
}


int exercise_b() {
	/*
		It solves exercise b, by reading a vector from keyboard ( the length and the elements ) and then it prints the maximum subsequence that respect the requirement.
	*/
	Vector v1;
	printf("How many numbers do you want to add in the vector?");
	scanf("%d", &v1.length);
	if (v1.length == 0) {
		printf("What is wrong with you? \n");
		return 0;
	}
	printf("What are the numbers?");
	for (int i = 0; i < v1.length; i++)
		scanf("%d", &v1.a[i]);

	if (v1.length == 1) {
		printf("%d \n", v1.a[0]);
		return 0;
	}
	int current_subsequence = 1;
	int maximum_subsequence = 0;
	int final_index_for_maximum_subsequence = 0;
	for (int i = 0; i < v1.length - 1; i++) {
		if (check_if_two_numbers_contain_the_same_digits(v1.a[i], v1.a[i + 1]) == 1)
			current_subsequence++;
		else
			current_subsequence = 1;
		if (current_subsequence > maximum_subsequence){
			maximum_subsequence = current_subsequence;
			final_index_for_maximum_subsequence = i + 1;
		}
	}

	for (int i = final_index_for_maximum_subsequence - maximum_subsequence + 1; i <= final_index_for_maximum_subsequence; i++)
		printf("%d ", v1.a[i]);
}

int gcd(int a, int b) {
	/*
		It computes the greatest common divisor ( Euclidean Algorithm ).
	*/
	int r;
	while (b) {
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}


int solve_a(int x) {
	/*
		It checks if all the natural numbers smaller than x that are relatively prime with x are prime.
	*/
	for (int i = 2; i < x; i++)
		if (gcd(x, i) == 1)
			if (prime(i) == 0)
				return 0;
	return 1;
}


int exercise_a() {
	/*
		It prints the first 8 numbers with the given property.
	*/
	int count = 8;
	unsigned int x = 3;
	unsigned int y;

	while (count) {
		y = solve_a(x);
		if (y == 0) 
			x++;
		else
		{
			printf("%d ", x);
			x++;
			count--;
		}
	}
	return 0;
}


int start() {
	/*
		It reads a letter from the keyboard and if it's 'a' is going to solve exercise a, if it's 'b' is going to solve exercise b and if it's x exits the program.
	*/
	char command[20];
	printf("Which problem statement do you want to solve? a or b? type x if you want to stop the program.\n");
	scanf("%s", command);
	
	if (command[0] == 'x')
		return 0;
	if (command[0] == 'a') {
		exercise_a();
		printf("\n");
		return 1;
	}
		
	else
		if(command[0] == 'b') {
			exercise_b();
			return 1;
		}	
}



/***************************************************** TESTS **********************************************************/

void test_for_prime() {
	assert(prime(2) == 1);
	assert(prime(3) == 1);
	assert(prime(-3) == 0);
	assert(prime(4) == 0);
	assert(prime(101) == 1);
	assert(prime(17) == 1);
	assert(prime(402030) == 0);
	assert(prime(123) == 0);
	assert(prime(124) == 0);
	assert(prime(127) == 1);
	assert(prime(35) == 0);
}

void test_check_if_two_numbers_contain_the_same_digit() {
	assert(check_if_two_numbers_contain_the_same_digits(13, 31) == 1);
	assert(check_if_two_numbers_contain_the_same_digits(12, 12121) == 1);
	assert(check_if_two_numbers_contain_the_same_digits(168, 879) == 0);
	assert(check_if_two_numbers_contain_the_same_digits(548, 85454548) == 1);
	assert(check_if_two_numbers_contain_the_same_digits(156, 87986) == 0);
	assert(check_if_two_numbers_contain_the_same_digits(-489, 489) == 1);
	assert(check_if_two_numbers_contain_the_same_digits(-35898, 8953) == 1);
	assert(check_if_two_numbers_contain_the_same_digits(89798, 65484) == 0);
	assert(check_if_two_numbers_contain_the_same_digits(674, -7646764) == 1);
	assert(check_if_two_numbers_contain_the_same_digits(56748, 564856) == 0);
	assert(check_if_two_numbers_contain_the_same_digits(189, 0) == 0);
	assert(check_if_two_numbers_contain_the_same_digits(0, 0) == 1);
}


void test_gcd() {
	assert(gcd(10, 5) == 5);
	assert(gcd(12, 18) == 6);
	assert(gcd(-3, -12) == -3);
	assert(gcd(50, 26) == 2);
	assert(gcd(0, 13) == 13);
	assert(gcd(15, 23) == 1);
	assert(gcd(17, 19) == 1);
	assert(gcd(156, 29) == 1);
	assert(gcd(165, 25) == 5);
}


void all_tests() {
	test_for_prime();
	test_check_if_two_numbers_contain_the_same_digit();
	test_gcd();
}

/***************************************************** MAIN **********************************************************/



int main() {
	all_tests();
	while (1)
		if (start() == 0)
			break;
	return 0;
}