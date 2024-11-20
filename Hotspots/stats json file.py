import pstats

# Example for clock profiling results
p = pstats.Stats('NPC_CRIME.prof')
p.strip_dirs().sort_stats('cumulative').print_stats(189)

