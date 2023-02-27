clc
option_distribution = input('Normal/Student/Fischer/Chi2\n', 's');

switch option_distribution
    case 'normal'
        fprintf('normal case\n');
        mu = input('mu = ');
        sigma = input('sigma = ');
        prob_a = normcdf(0,mu,sigma);
        prob_b = 1 - prob_a;
        prob_c = normcdf(1,mu,sigma) - normcdf(-1,mu,sigma);
        prob_d = 1 - prob_c;
        alpha = input('alpha = ');
        if alpha < 0 || alpha > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_e = norminv(alpha, mu, sigma);
        beta = input('beta = ');
        if beta < 0 || beta > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_f = norminv(1-beta, mu, sigma);
    case 'student'
        fprintf('student\n');
        n = input('n = \n');
        prob_a = tcdf(0,n);
        prob_b = 1 - prob_a;
        prob_c = tcdf(1,n) - tcdf(-1,n);
        prob_d = 1 - prob_c;
        alpha = input('alpha = ');
        if alpha < 0 || alpha > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_e = tinv(alpha, n);
        beta = input('beta = ');
        if beta < 0 || beta > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_f = norminv(1-beta, n);
    case 'fischer'
        fprintf('fischer\n');
        n = input('n = ');
        m = input('m = ');
        prob_a = fcdf(0,n,m);
        prob_b = 1 - prob_a;
        prob_c = fcdf(1,n,m) - fcdf(-1,n,m);
        prob_d = 1 - prob_c;
        alpha = input('alpha = ');
        if alpha < 0 || alpha > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_e = finv(alpha, n, m);
        beta = input('beta = ');
        if beta < 0 || beta > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_f = finv(1-beta, n, m);
    case 'Chi2'
        fprintf('Chi2\n');
        n = input('n = ');
        
        prob_a = chi2cdf(0,n);
        prob_b = 1 - prob_a;
        prob_c = chi2cdf(1,n) - chi2cdf(-1,n);
        prob_d = 1 - prob_c;
        alpha = input('alpha = ');
        if alpha < 0 || alpha > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_e = chi2inv(alpha, n);
        beta = input('beta = ');
        if beta < 0 || beta > 1
            fprintf('You have to choose between [0,1]');
            return;
        end
        prob_f = chi2inv(1-beta, n);
    otherwise
        fprintf('Bad input\n');
end
fprintf('P(x<=0) %f\n', prob_a);
fprintf('P(x>=0) %f\n', prob_b);
fprintf('P(-1<=x<=1) %f\n', prob_c);
fprintf('P(x<=-1 or x>=1) %f\n', prob_d);
fprintf('x(alfa) %f\n', prob_e);
fprintf('x(beta) %f\n', prob_f);

