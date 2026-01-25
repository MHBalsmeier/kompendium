# This script compares the (theoretical) speeds of WRF and GAME.

timestep_factor_game = 1.61
n_tau_game = 2
n_t_game = 1
timestep_factor_wrf = 8.0
n_substeps_wrf = timestep_factor_wrf
n_t_wrf = 3
n_tracers = 5
alpha = 0.5 + 0.2*n_tracers

# end of input section
n_tau_wrf = 1 + int(n_substeps_wrf/2) + n_substeps_wrf
tau_eff_game = timestep_factor_game/n_tau_game
tau_eff_wrf= timestep_factor_wrf/n_tau_wrf

speed_game = tau_eff_game*timestep_factor_game/n_t_game/(alpha*tau_eff_game + timestep_factor_game/n_t_game)
speed_wrf = tau_eff_wrf*timestep_factor_wrf/n_t_wrf/(alpha*tau_eff_wrf + timestep_factor_wrf/n_t_wrf)

print("speed_game: " + str(round(speed_game, 3)))
print("speed_wrf: " + str(round(speed_wrf, 3)))



