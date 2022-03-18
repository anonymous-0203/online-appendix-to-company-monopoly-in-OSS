> library(car)
> library(survival);library("survminer")
> sd <- read.csv('survival_data.csv', header=TRUE)
> fit <- coxph(Surv(tstart, tstop, status) ~ is_domi + repo_type + log(num_cmt + 1) + log(num_com + 1) + log(num_dvpr + 1), data=sd)
> summary(fit)
Call:
coxph(formula = Surv(tstart, tstop, status) ~ is_domi + repo_type + 
    log(num_cmt + 1) + log(num_com + 1) + log(num_dvpr + 1), 
    data = sd)

  n= 6808, number of events= 675 

                      coef exp(coef) se(coef)      z Pr(>|z|)    
is_domi1          -0.22458   0.79885  0.13962 -1.609  0.10772    
repo_type1        -0.14239   0.86728  0.09216 -1.545  0.12232    
repo_type2        -0.37258   0.68895  0.18568 -2.007  0.04479 *  
repo_type3        -0.16104   0.85126  0.13197 -1.220  0.22237    
repo_type4        -0.17467   0.83974  0.20244 -0.863  0.38824    
repo_type5        -0.32234   0.72445  0.25693 -1.255  0.20962    
log(num_cmt + 1)  -0.62197   0.53688  0.07426 -8.375  < 2e-16 ***
log(num_com + 1)  -0.72454   0.48455  0.22692 -3.193  0.00141 ** 
log(num_dvpr + 1) -0.74562   0.47444  0.18295 -4.076 4.59e-05 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

                  exp(coef) exp(-coef) lower .95 upper .95
is_domi1             0.7989      1.252    0.6076    1.0503
repo_type1           0.8673      1.153    0.7240    1.0390
repo_type2           0.6890      1.451    0.4788    0.9914
repo_type3           0.8513      1.175    0.6572    1.1025
repo_type4           0.8397      1.191    0.5647    1.2487
repo_type5           0.7245      1.380    0.4378    1.1987
log(num_cmt + 1)     0.5369      1.863    0.4642    0.6210
log(num_com + 1)     0.4845      2.064    0.3106    0.7559
log(num_dvpr + 1)    0.4744      2.108    0.3315    0.6791

Concordance= 0.859  (se = 0.007 )
Likelihood ratio test= 1085  on 9 df,   p=<2e-16
Wald test            = 692.4  on 9 df,   p=<2e-16
Score (logrank) test = 854.5  on 9 df,   p=<2e-16

> vif(fit)
                      GVIF Df GVIF^(1/(2*Df))
is_domi           1.596513  1        1.263532
repo_type         1.090009  5        1.008656
log(num_cmt + 1)  2.547100  1        1.595964
log(num_com + 1)  4.487655  1        2.118409
log(num_dvpr + 1) 5.283207  1        2.298523
Warning message:
In vif.default(fit) : No intercept: vifs may not be sensible.


> fit <- coxph(Surv(tstart, tstop, status) ~ is_domi + repo_type + log(num_cmt + 1), data=sd)
> summary(fit)
Call:
coxph(formula = Surv(tstart, tstop, status) ~ is_domi + repo_type + 
    log(num_cmt + 1), data = sd)

  n= 6808, number of events= 675 

                     coef exp(coef) se(coef)       z Pr(>|z|)    
is_domi1          0.37769   1.45891  0.11454   3.297 0.000976 ***
repo_type1       -0.20746   0.81265  0.09112  -2.277 0.022806 *  
repo_type2       -0.50708   0.60225  0.18482  -2.744 0.006077 ** 
repo_type3       -0.23132   0.79349  0.13061  -1.771 0.076562 .  
repo_type4       -0.18727   0.82922  0.20186  -0.928 0.353554    
repo_type5       -0.22468   0.79877  0.25671  -0.875 0.381435    
log(num_cmt + 1) -1.20008   0.30117  0.04680 -25.643  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

                 exp(coef) exp(-coef) lower .95 upper .95
is_domi1            1.4589     0.6854    1.1656    1.8261
repo_type1          0.8126     1.2305    0.6797    0.9716
repo_type2          0.6022     1.6604    0.4192    0.8652
repo_type3          0.7935     1.2603    0.6143    1.0250
repo_type4          0.8292     1.2060    0.5583    1.2317
repo_type5          0.7988     1.2519    0.4830    1.3211
log(num_cmt + 1)    0.3012     3.3204    0.2748    0.3301

Concordance= 0.848  (se = 0.008 )
Likelihood ratio test= 1005  on 7 df,   p=<2e-16
Wald test            = 736.8  on 7 df,   p=<2e-16
Score (logrank) test = 843.5  on 7 df,   p=<2e-16

> vif(fit)
                     GVIF Df GVIF^(1/(2*Df))
is_domi          1.075501  1        1.037064
repo_type        1.046135  5        1.004520
log(num_cmt + 1) 1.030245  1        1.015010
Warning message:
In vif.default(fit) : No intercept: vifs may not be sensible.
> 
