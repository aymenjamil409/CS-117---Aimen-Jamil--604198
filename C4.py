def loaded_divider(vs, r1, r2, rl):
    unloaded_v = vs * (r2 / (r1 + r2))
    reciprocal_sum = (1 / r2) + (1 / rl)
    r2_p_rl = 1 / reciprocal_sum
    loaded_v = vs * (r2_p_rl / (r1 + r2_p_rl))
    return unloaded_v, loaded_v
vs_val = 12
r1_val = 1000
r2_val = 1000
rl_val = 500
results = loaded_divider(vs_val, r1_val, r2_val, rl_val)
print("loaded_divider(12, 1000, 1000, 500) ->", results)
