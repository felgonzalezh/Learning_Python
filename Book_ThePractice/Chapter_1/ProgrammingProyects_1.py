# Great lakes in US contain roughly 22% of world's fresh surface water (22810 km3).
# How deep would be a lake with this amount of water if it would spread over all US surface?
# US surface area = 9.834 millions of km2

v = 22810.0;
a = 9834000.0;

d = v/a;
d_meters = d*1000;

print "The deep would be ", d_meters, " m ";
