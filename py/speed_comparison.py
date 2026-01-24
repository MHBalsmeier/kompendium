# This script compares the (theoretical) speeds of WRF and GAME.

timestep_factor_game = 1.61
timestep_factor_wrf = 7.0
alpha = 0.5

speed_game = timestep_factor_game/2.0*timestep_factor_game/(alpha*timestep_factor_game/2.0 + timestep_factor_game)
speed_wrf = timestep_factor_wrf/10.0*timestep_factor_wrf/3.0/(alpha*timestep_factor_wrf/10.0 + timestep_factor_wrf/3.0)

print("speed_game: " + str(speed_game))
print("speed_wrf: " + str(speed_wrf))



