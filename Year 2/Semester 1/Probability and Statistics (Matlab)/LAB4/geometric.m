clear
p = input('give the probability ');
N = input('give the nb of sim ');
for i=1:N
	X(i) = 0;
	while rand >= p
		X(i) = X(i)+1;
    end
end

U_X = unique(X);
k=0:max(U_X);
n_X = hist(X,length(U_X));
rel_freq = n_X / N;
plot(U_X,rel_freq,'*',k,geopdf(k,p),'o')
legend('simulation','geo')
