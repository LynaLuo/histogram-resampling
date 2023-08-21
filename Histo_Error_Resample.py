#! /usr/local/bin/python3

# --------------------------------------------------------------------------------
# Script will generate errobars (std.err) using resampling method. 
# Examples with silly 'fake' historgam. Taken, in part, from 
# G. Tribello's examples in "SOR1020 Introduction to probability and statistics"
# 
# - 20200602	Jesper Madsen	Initial version, early
# - 20230118	Jesper Madsen	Update and revision using 'fake_histo' data proc
#                               Please revise carefully before using..
# --------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import random

# make 'fake' data
def fake_histo(n_sample,n_bins):
    histo=np.zeros(n_bins)
    for i in range(n_sample):
        rand=int( random.randint(0,n_bins-1) )
        histo[rand]=histo[rand]+rand
    histo=histo/n_sample
    return histo

# generate histogram
nb=10 #num bin
ns=1000 #num samples

histo_sample=np.zeros([ns,nb])
for i in range(ns): histo_sample[i,:]=fake_histo(ns,nb)

lo,med,up = np.zeros(nb),np.zeros(nb),np.zeros(nb)
for i in range(nb):
    med[i]=np.median( histo_sample[:,i] )
    lo[i]=med[i] - np.percentile( histo_sample[:,i],5 )
    up[i]=np.percentile( histo_sample[:,i], 95 ) - med[i]

x=np.linspace( 0,nb-1,nb )
plt.errorbar( x, med, yerr=[lo,up],fmt='ko',ecolor=None )
plt.bar( x,med,width=0.5 )
#plt.show()
plt.savefig('Histo_resample.png')