clc
clear all
conf_level = input('conf level= ');
alpha = 1 - conf_level;
X = [7 7 4 5 9 9 ...
     4 12 8 1 8 7 ...
     3 13 2 1 17 7 ...
     12 5 6 2 1 13 ...
     14 10 2 4 9 11 ...
     3 5 12 6 10 7];
 
 sigma = 5;
 n = length(X);
 xbar = mean(X);
 
 q1 = norminv(alpha/2, 0, 1);
 q2 = norminv(1-alpha/2, 0, 1);
 
 ci1 = xbar - sigma/sqrt(n) * q2;
 ci2 = xbar - sigma/sqrt(n) * q1;
 
 fprintf('confidence interval for the population mean, miu, case sigma known is: (%3.4f, %3.4f)\n', ci1, ci2)
 
 s = std(X); % sigma unknown
 q3 = tinv(alpha/2, n - 1);
 q4 = tinv(1-alpha/2, n - 1);
 
 ci3 = xbar - s/sqrt(n) * q2;
 ci4 = xbar - s/sqrt(n) * q1;
 
 fprintf('Confidence interval for the population mean, miu, case sigma unknown is: (%3.4f, %3.4f)\n', ci3, ci4)
 
 ssq = var(X); % sample variance
 q5 = chi2inv(alpha/2, n-1);
 q6 = chi2inv(1-alpha/2, n-1);
 
 ci5 = (n-1)*ssq/q6;
 ci6 = (n-1)*ssq/q5;
 fprintf('Confidence interval for the population variance, sigma square: (%3.4f, %3.4f)\n', ci5, ci6)
 fprintf('Confidence interval for the population std dev, sigma square: (%3.4f, %3.4f)\n', sqrt(ci5), sqrt(ci6))
 
