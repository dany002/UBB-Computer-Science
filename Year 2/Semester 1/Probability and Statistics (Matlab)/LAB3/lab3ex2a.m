clc
clear

n = 0:1:100;
p = input('p = ');
if p < 0.05 || p > 0.95
    fprintf('Bad input');
    return;
end

for i = 1:2:100
    mu = i*p;
    ala = sqrt(i*p*(1-p));
    k = 0:1:i;
    n = normpdf(k,mu,ala);
    b = binopdf(k,i,p);
    plot(k,n,k,b);
    title("Aproximation of bino and norm approximation for " + i);
    legend('bino','norm');
    pause(0.5);
end
