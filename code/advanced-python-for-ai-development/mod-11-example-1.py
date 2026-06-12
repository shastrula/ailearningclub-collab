import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code to profile
result = model.predict(X)

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)