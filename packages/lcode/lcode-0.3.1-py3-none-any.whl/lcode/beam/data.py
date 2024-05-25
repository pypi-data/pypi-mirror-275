import numba as nb
import numpy as np

particle_dtype = np.dtype([('xi', 'f8'), ('r', 'f8'), ('p_z', 'f8'),
                           ('p_r', 'f8'), ('M', 'f8'), ('q_m', 'f8'),
                           ('q_norm', 'f8'), ('id', 'i8')])

class BeamParticles:
    def __init__(self, size=0, particles=None):
        self.size = size
        if particles is not None:
            self.particles = particles
        else:
            self.particles = np.zeros(size, dtype=particle_dtype)
        self.xi = self.particles['xi']
        self.r = self.particles['r']
        self.p_z = self.particles['p_z']
        self.p_r = self.particles['p_r']
        self.M = self.particles['M']
        self.q_m = self.particles['q_m']
        self.q_norm = self.particles['q_norm']
        self.id = self.particles['id']

        # Additional particle properties for substepping, not stored in beam
        self.dt = np.zeros(size, dtype=np.float64)
        self.remaining_steps = np.ones(size, dtype=np.int64)

        self.nlost = 0
        self.lost = np.zeros(size, dtype=np.bool_)

    def swap_particles(self, i, j):
        self.particles[i], self.particles[j] = self.particles[j], self.particles[i]
        self.dt[i], self.dt[j] = self.dt[j], self.dt[i]
        self.remaining_steps[i], self.remaining_steps[j] = self.remaining_steps[j], self.remaining_steps[i]
        self.status[i], self.status[j] = self.status[j], self.status[i]
        self.lost[i], self.lost[j] = self.lost[j], self.lost[i]

    def get_subslice(self, begin, end):
        temp_particles = self.particles[begin:end]
        sub_slice = BeamParticles(len(temp_particles), temp_particles)
        sub_slice.dt[:] = self.dt[begin:end]
        sub_slice.remaining_steps[:] = self.remaining_steps[begin:end]
        sub_slice.lost[:] = self.lost[begin:end]
        return sub_slice
    
    def concat(self, other_slice):
        
        new_slice = BeamParticles(0, None)
        new_slice.size = self.size + other_slice.size
        new_slice.particles = np.concatenate((self.particles, other_slice.particles))
        new_slice.xi = new_slice.particles['xi']
        new_slice.r = new_slice.particles['r']
        new_slice.p_z = new_slice.particles['p_z']
        new_slice.p_r = new_slice.particles['p_r']
        new_slice.M = new_slice.particles['M']
        new_slice.q_m = new_slice.particles['q_m']
        new_slice.q_norm = new_slice.particles['q_norm']
        new_slice.id = new_slice.particles['id']
        # Additional particle properties for substepping, not stored in beam
        new_slice.dt =  np.concatenate((self.dt, other_slice.dt))
        new_slice.remaining_steps = np.concatenate((self.remaining_steps, other_slice.remaining_steps))

        new_slice.nlost = self.nlost + other_slice.nlost
        new_slice.lost = np.concatenate((self.lost, other_slice.lost))
        return new_slice
    
    def append(self, other_slice):
        self.particles = np.concatenate((
            self.particles, other_slice.particles,
        ))
        self.size = self.particles.size
        self.xi = self.particles['xi']
        self.r = self.particles['r']
        self.p_z = self.particles['p_z']
        self.p_r = self.particles['p_r']
        self.M = self.particles['M']
        self.q_m = self.particles['q_m']
        self.q_norm = self.particles['q_norm']
        self.id = self.particles['id']

        self.dt = np.concatenate((self.dt, other_slice.dt))
        self.remaining_steps = np.concatenate((
            self.remaining_steps, other_slice.remaining_steps,
        ))
        #self.status = np.concatenate((self.status, other_slice.status))
        self.lost = np.concatenate(((self.lost), other_slice.lost))
        return self

    def mark_lost(self, idx):
        self.lost[idx] = True
        self.nlost += 1

    def sort(self):
        sorted_idxes = np.argsort(-self.xi)
        self.particles = self.particles[sorted_idxes]
        self.xi = self.particles['xi']
        self.r = self.particles['r']
        self.p_z = self.particles['p_z']
        self.p_r = self.particles['p_r']
        self.M = self.particles['M']
        self.q_m = self.particles['q_m']
        self.q_norm = self.particles['q_norm']
        self.id = self.particles['id']

        self.dt = self.dt[sorted_idxes]
        self.remaining_steps = self.remaining_steps[sorted_idxes]
        self.lost = self.lost[sorted_idxes]

    def load(self, *args, **kwargs):
        with np.load(*args, **kwargs) as loaded:
            self.size = loaded['xi'].shape[0]
            self.particles = np.zeros(self.size, dtype=particle_dtype)
            self.particles['xi'] = loaded['xi']
            self.particles['r'] = loaded['r']
            self.particles['p_r'] = loaded['p_r']
            self.particles['p_z'] = loaded['p_z']
            self.particles['M'] = loaded['M']
            self.particles['q_m'] = loaded['q_m']
            self.particles['q_norm'] = loaded['q_norm']
            self.particles['id'] = loaded['id']
            self.xi = self.particles['xi']
            self.r = self.particles['r']
            self.p_r = self.particles['p_r']
            self.p_z = self.particles['p_z']
            self.M = self.particles['M']
            self.q_m = self.particles['q_m']
            self.q_norm = self.particles['q_norm']
            self.id = self.particles['id']

            self.dt = np.zeros(self.size, dtype=np.float64)
            self.remaining_steps = np.ones(self.size, dtype=np.int64)

            self.nlost = 0
            self.lost = np.zeros(self.size, dtype=np.bool_)
