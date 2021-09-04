> fit <- coxph(Surv(tstart, tstop, status)~ fis_mono + I(log(num_cmt)) + frepo_type, data);  summary(fit)
Call:
coxph(formula = Surv(tstart, tstop, status) ~ fis_mono + I(log(num_cmt)) + 
    frepo_type, data = data)

  n= 6808, number of events= 675 

                    coef exp(coef) se(coef)       z Pr(>|z|)    
fis_mono1        0.81522   2.25967  0.16494   4.943 7.71e-07 ***
I(log(num_cmt)) -0.88191   0.41399  0.03557 -24.795  < 2e-16 ***
frepo_type1      0.24153   1.27319  0.18822   1.283   0.1994    
frepo_type2      0.24479   1.27735  0.29970   0.817   0.4141    
frepo_type3      0.44093   1.55416  0.18440   2.391   0.0168 *  
frepo_type4      0.24730   1.28056  0.21033   1.176   0.2397    
frepo_type5      0.28779   1.33348  0.26253   1.096   0.2730    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

                exp(coef) exp(-coef) lower .95 upper .95
fis_mono1           2.260     0.4425    1.6355    3.1221
I(log(num_cmt))     0.414     2.4155    0.3861    0.4439
frepo_type1         1.273     0.7854    0.8804    1.8412
frepo_type2         1.277     0.7829    0.7099    2.2983
frepo_type3         1.554     0.6434    1.0828    2.2308
frepo_type4         1.281     0.7809    0.8479    1.9339
frepo_type5         1.333     0.7499    0.7971    2.2308

Concordance= 0.85  (se = 0.008 )
Likelihood ratio test= 1004  on 7 df,   p=<2e-16
Wald test            = 784.8  on 7 df,   p=<2e-16
Score (logrank) test = 942.3  on 7 df,   p=<2e-16
