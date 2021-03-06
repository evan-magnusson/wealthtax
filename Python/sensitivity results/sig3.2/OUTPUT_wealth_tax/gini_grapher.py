import numpy as np
import pickle
from matplotlib import pyplot as plt

variables = pickle.load(open("gini_vectors.pkl", "r"))
for key in variables:
    globals()[key] = variables[key]

variables = pickle.load(open("gini_vectors_2.pkl", "r"))
for key in variables:
    globals()[key] = variables[key]


domain = np.linspace(1, T, T)

plt.figure()
plt.plot(domain, wealth_baseline, label='Baseline', color='black', linestyle='--')
plt.plot(domain, wealth_wealth, label='Wealth Tax', color='green')
plt.plot(domain, wealth_income, label='Income Tax', color='red')
plt.legend(loc=0)
plt.xlabel('Time')
plt.ylabel('Gini Coefficient')
plt.title('Gini coefficient for inequality across age and ability')
plt.savefig('Nothing/gini_wealth.png')

plt.figure()
plt.plot(domain, income_baseline, label='Baseline', color='black', linestyle='--')
plt.plot(domain, income_wealth, label='Wealth Tax', color='green')
plt.plot(domain, income_income, label='Income Tax', color='red')
plt.legend(loc=0)
plt.xlabel('Time')
plt.ylabel('Gini Coefficient')
plt.title('Gini coefficient for inequality across age and ability')
plt.savefig('Nothing/gini_income.png')

plt.figure()
plt.plot(domain, cons_baseline, label='Baseline', color='black', linestyle='--')
plt.plot(domain, cons_wealth, label='Wealth Tax', color='green')
plt.plot(domain, cons_income, label='Income Tax', color='red')
plt.legend(loc=0)
plt.xlabel('Time')
plt.ylabel('Gini Coefficient')
plt.title('Gini coefficient for inequality across age and ability')
plt.savefig('Nothing/gini_cons.png')

plt.figure()
plt.plot(domain, lab_baseline, label='Baseline', color='black', linestyle='--')
plt.plot(domain, lab_wealth, label='Wealth Tax', color='green')
plt.plot(domain, lab_income, label='Income Tax', color='red')
plt.legend(loc=0)
plt.xlabel('Time')
plt.ylabel('Gini Coefficient')
plt.title('Gini coefficient for inequality across age and ability')
plt.savefig('Nothing/gini_lab.png')