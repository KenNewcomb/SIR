'''sir.py: Numerically integrate the SIR equations.'''
import sys

def usage():
	print('usage: python3 sir.py beta gamma s0 i0 r0 dt timesteps')
	print('Note: s(t) + i(t) + r(t) = 1.')

def integrate(beta, gamma, s0, i0, r0, dt):
	
	snew = -beta*s0*i0*dt + s0
	inew = (beta*s0*i0-gamma*i0)*dt + i0
	rnew = 1-snew-inew

	return [snew, inew, rnew] 

def writeTrajectories():
	pass

# Check if enough parameters are given
if len(sys.argv) != 8:
	usage()
	exit()

# Parameters
beta  = float(sys.argv[1])
gamma = float(sys.argv[2])

# Initial populations
s0    = float(sys.argv[3])
i0    = float(sys.argv[4])
r0    = float(sys.argv[5])

# Options
dt        = float(sys.argv[6])
timesteps = int(sys.argv[7])

s = []
i = []
r = []

# Verify that S+I+R=1
if s0 + i0 + r0 != 1.0:
	usage()
	exit()
 
for step in range(0, timesteps):
	[snew, inew, rnew]  = integrate(beta, gamma, s0, i0, r0, dt)
	s.append(snew)
	i.append(inew)
	r.append(rnew)
	
	s0 = snew
	i0 = inew
	r0 = rnew

# Save data
with open('data', 'w') as sirdata:
	for time in range(0, timesteps):
		sirdata.write('{0} {1} {2} {3}\n'.format(time*dt, s[time], i[time], r[time]))
