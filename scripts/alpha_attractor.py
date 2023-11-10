# import classy module
from classy import Class
import matplotlib.pyplot as plt
from math import pi

# In[ ]:

common_params = {'omega_b':0.0223828,
				'omega_cdm':0.1201075,
				'h':0.67810,
				'A_s':2.100549e-09,
				'n_s':0.9660499,
				'tau_reio':0.05430842,
				'output':'tCl,pCl,lCl,mPk',
				'lensing':'yes',
				'P_k_max_1/Mpc': 3.0,
				'Omega_fld': 0,
				'Omega_scf': -1,
				'Omega_Lambda': 0,
				'scf_parameters': '127,2.333333333,0,0,-10,0.0',
				'attractor_ic_scf': 'no',
				'scf_tuning_index': 0
				}
				
# create instance of the class "Class"
LambdaCDM = Class()
# pass input parameters
LambdaCDM.set(common_params)
# run class
LambdaCDM.compute()


# get all C_l output
cls = LambdaCDM.lensed_cl(2500)
# To check the format of cls
cls.keys()

ll = cls['ell'][2:]
clTT = cls['tt'][2:]
clEE = cls['ee'][2:]
clPP = cls['pp'][2:]

# plot C_l^TT
plt.figure(1)
plt.xscale('log');plt.yscale('linear');plt.xlim(2,2500)
plt.xlabel(r'$\ell$')
plt.ylabel(r'$[\ell(\ell+1)/2\pi]  C_\ell^\mathrm{TT}$')
plt.plot(ll,clTT*ll*(ll+1)/2./pi,'r-')

plt.savefig('warmup_cltt.pdf')

# optional: reset parameters to default in case you want
# to set different parameters and rerun LambdaCDM.compute()
LambdaCDM.empty()
