clear all;
clc;

p = input('p = ');
N = input('Number of simulations = ');
n = input('Target number of successes  = ');

for i = 1 : N
	x(i) = 0;
	j = 0;
	% the ith simulation
	U = rand;
	while j < n
		if U >= p
			x(i) = x(i) + 1;
		else
			j = j + 1;
		end
	end
end

U_X = unique(X);
n_X = hist(X, length(U_X));
rel_freq = n_X / N;
[U_X; n_X; rel_freq];
plot(U_X, rel_freq, 'x', 0:max(U_X), nbinpdf(0:max(U_X), n, p), 'o');
legend('simulation', 'pascal');
