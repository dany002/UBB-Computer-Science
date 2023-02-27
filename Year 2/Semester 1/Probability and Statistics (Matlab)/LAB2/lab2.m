clear
clc
message_for_n = 'n = ';
n = input(message_for_n);
p = input('p = ');
k = 0:1:n;
kk = 0:0.1:n;
A = [k;binopdf(k,n,p)]
plot(k,binopdf(k,n,p),'x')
axis([-0.1 3.1 -0.1 1.1]);
hold on
plot(kk, binocdf(kk,n,p))
legend('bino.pdf', 'binocdf');
title('Titleeee :D');
hold off

c = binopdf(0,n,p);
fprintf('P(x=0) %f\n', c)

c1 = binopdf(1,n,p);
fprintf('P(x!=1) %f\n', 1-c1)

d1 = binocdf(2,n,p);
fprintf('P(x<=2) %f\n', d1)

d2 = binocdf(1,n,p);
fprintf('P(x<2) %f\n', d2)

e1 = binocdf(0,n,p);
fprintf('P(x>=1) %f\n', 1-e1)

e2 = binocdf(1,n,p);
fprintf('P(x>1) %f\n', 1-e2)
c23 = 0;
for i = 1:3
    x = randi(2) - 1;
    if x < 0.5
        fprintf('head\n')
        c23 = c23+1;
    else
        fprintf('tails\n')
    end
end
fprintf('The number of heads is %d\n', c23)
fprintf('The probability is %f\n',binopdf(c23,n,p))
