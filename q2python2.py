def devvie(self, input):
      from math  import cos, sin, pi
      from numpy import linalg, dot
        
      d = [0, pi/2, pi, 3*pi/2]
      x, y = 0, 0
        
      for ch in input:
        if ch == "F":
          x += cos(d[0])
          y += sin(d[0])
        if ch == "L":
          d = d[-1:] + d[:-1]
        if ch == "R":
          d = d[1:] + d[:1]
    
      r = round(abs(x) + abs(y))
      if r == 0: return r
   
      dp = dot(
        [-x, -y] / linalg.norm([-x, -y]),
        [cos(d[0]), sin(d[0])]
      )
      
      if      dp < 0: return r + 2
      if 0 <= dp < 1: return r + 1
        
      return r
