import sim as sim

#control parameters - 1 means on, 0 means off
write = 1
analyze = 1
makefig = 1

diffuse = 1
antibunch = 1
pulsed = 0

#General saving folder parameters
filepath = "C:/Users/Karen/Dropbox (WilsonLab)/WilsonLab Team Folder/Data/2017-08-25-cleanup/"
filedir = "NormArtChase"
filenames = ["1AE0-2kex-1-a1kem10000bf50-", "testap-p05mW10ppbf1001MHz-", "testap-p-5mW10pp"]

#file length - goes to the max of these two
numlines = 10**8
maxlines = 10**9
endtime = 10**12 #ps = 1 s

#Sample parameters
temp = 298 #K
k_emission = 10000 #emission lifetime in ps
emwavelength = 815
bfrate = 0.5 #fraction of successful emitting bright fission events - make sure to consider laser wavelength and emission wavelength

r = 10 #nm - hydrodynamic radius of particles

eta = 8.9 * 10**(-13) # kg/nm s - dynamic viscosity of solvent (water)
n = 1.3 # index of refraction - sample in water

concentration = 2*10**-8 

absXsec = 7.180616773321853*10**-9# per emitter numabs'd = phperpulse*absXsec*numEms - this is reasonable based on absXsec for CdSe is 550000*r^3/cm (from Bawendi paper Ruvim sent me)

#Laser parameters
reprate = 1 #MHz

wavelength = 532 #nm
beamdiam = 5000000 #5 mm in nm
laserpwr = 0.5 # mW (0.52 mWinto back of objective 23 #mW)
#laserpwr = [0.05,0.1,0.2,0.3,0.5,0.75,1,10]#[0.001,0.01,0.025,

pulselength = 80 #ps - not used


#Objective parameters
foclen = 310000 #310 microns in nm (working distance + coverslip thickness)
NA = 1.4

#Detector parameters
darkcounts = 1 #s^-1
sensitivity = 1 
deadtime = 70000 #70 ns in ps
afterpulse = 0.0001 #percent of time a photon is emitted a deadtime after one is detected

#Correlation parameters
order = 2 #g2
mode = "t2"
gnpwr = 20
numbins = 4096
pulsebins = (10**2)-1#should always be an odd number
channels = 2

#Miscellaneous simulation parameters
picyzoom = [-1,-1]
timestep = 1000000 #average number of photons per "round" of calculations

for i in range(10):  
    count = 0
    
    for filename in filenames:
        if count == 0:
            bfrate = 0.5
            pulsed = 0
            absXsec = absXsec/10
        if count == 1:
            bfrate = 1
            pulsed = 1
            absXsec = absXsec *10
        f = filename + str(i)
        count = count + 1
        sim.simulate(filepath, filedir, f, write, analyze, makefig, diffuse, antibunch,
                    pulsed, numlines, maxlines, endtime,temp, concentration, absXsec,
                    k_emission, emwavelength, bfrate, r,eta, n, reprate,
                    wavelength, laserpwr, pulselength, foclen,
                    NA, darkcounts, sensitivity, deadtime, afterpulse, order, 
                    mode, gnpwr, numbins, pulsebins, channels) 

    

    
    


                


