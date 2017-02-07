
# Dictionary of the periodic table
# Uses the element as the key value to access the atomic mass 
periodic_table = { 'Na': 22.98,
			 	   'Cl': 35.45,
			 	   'C' : 12.011,
			 	   'O' : 15.999
					}

# Determines the amount of substrate needed to create a specific volume of solution at a specific molarity 
# Parameters  (the desired molarity of the final solution (M) - 
# the desired final volume (mL), elements in the substrate)
def substrate(desired_molarity, final_volume, *args): 
	atomic_mass = [periodic_table[element] for element in args]
	molecular_forumla = ''.join([element for element in args])
	molecular_mass = sum(atomic_mass)

	# Determines whether we want a Molarity > or < 1 M
	# maybe replace this with the absolute value ?
	# Substrate needed for 1 Liter of the desired concentration
	if desired_molarity > 1: 
		factor = desired_molarity / 1
		substrate_needed = round(molecular_mass * factor, 2) 
	else:
		factor = 1 / desired_molarity
		substrate_needed = round(molecular_mass / factor, 2) 

	# Corrects the amount of substrate needed based on the desired final volume
	substrate_needed = (substrate_needed * final_volume) / 1000 
	desired_volume = round(final_volume / 1000, 2)
	
	print('You would need {} g of {} to make {} liters of a {} M solution of {}'.format
		(substrate_needed, molecular_forumla, desired_volume,  desired_molarity, molecular_forumla)) 
	return substrate_needed
			

# How to prepare percent solutions
# Create a proportion of the desired % conc. / 100 =  unknown / desired_volume 
# Parameters (volume in mL, and desired %)
def percentSolution(desired_volume, desired_percentage):
	return (desired_percentage * desired_volume) / 100


# cv = cv 
# creating a new solution from a stock solution 
def dilution(stock_conc, stock_vol, desired_conc, desired_vol):
	if stock_conc == 0:
		return round((desired_conc * desired_vol) / stock_vol, 2)  # solves for the stock conc.
	elif stock_vol == 0:
		return round((desired_conc * desired_vol) / stock_conc, 2) # solves for the stock volume.
	elif desired_vol == 0:
		return round((stock_conc * stock_vol) / desired_conc, 2) # solves for the desired volume.
	elif desired_con == 0:
		return round((stock_conc * stock_vol) / desired_vol, 2) # solves for the desired conc. 




# Testing Functions
print(dilution(1.8, 0, .5,20))
print(percentSolution(.2, 10))
substrate(1, 2000, 'Na', 'Cl')