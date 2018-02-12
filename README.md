# TCSPC_simulator
A Monte-Carlo simulation to generate a photon record corresponding to diffusing or fixed particles of a given size in a given viscosity solvent with given emission statistics

All parameters are input in the main file, which passes them first to the simulation. This writes a photon record data file, which is (optionally) passed on to analysis using tsbischof's photon_correlation library (slightly edited here) and can output various figures. 
