def star_to_delta(ra, rb, rc):
     numerator = (ra * rb) + (rb * rc) + (rc * ra)
     r_ab = numerator / rc
     r_bc = numerator / ra
     r_ca = numerator / rb
     return r_ab, r_bc, r_ca
ra_val = 10
rb_val = 20
rc_val = 30
delta_results = star_to_delta(ra_val, rb_val, rc_val)
print("star_to_delta(10, 20, 30) ->", delta_results)
