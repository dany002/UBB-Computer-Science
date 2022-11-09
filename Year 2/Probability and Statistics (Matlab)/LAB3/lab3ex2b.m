clc
clear

n = input('n = ');
if n < 30
    fprintf('Bad input');
    return;
end
p = input('p = ');
if p >= 0.05
    fprintf('Bad input');
    return;
end

mu = n*p;
k = 0:1:n;
p1 = poisspdf(k,mu);
b = binopdf(k,n,p);
plot(k,p1,k,b);
title("Aproximation of bino and norm approximation for " + n);
legend('bino','norm');
pause(0.5);
