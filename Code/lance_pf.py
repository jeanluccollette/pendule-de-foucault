import pf
pf.pf_sim(l=30, g=9.81, OT=0, Lat=45,
          R=28, V=1, Dir=0,
          Duree=100, Pas=0.02, methode='rk4')
pf.pf_sim(l=30, g=9.81, OT=7.292115e-5, Lat=45,
          R=3, V=0, Dir=0,
          Duree=3600, Pas=0.02, methode='rk4')
pf.pf_sim(l=30, g=9.81, OT=7.292115e-5, Lat=45,
          R=3, V=0.04125, Dir=0,
          Duree=3600, Pas=0.02, methode='rk4')
