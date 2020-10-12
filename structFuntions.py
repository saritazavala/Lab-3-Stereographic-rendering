import struct


# Struct Functions ---------------------------------
def char(c):
    return struct.pack('=c', c.encode('ascii'))

# 2 bytes
def word(c):
    return struct.pack('=h', c)

# 4 bytes
def dword(c):
    return struct.pack('=l', c)

# --------------------------------------------------

class color(object):
  def __init__(self,r,g,b):
    self.r = r
    self.g = g
    self.b = b

  def equals(self, other):
    return (self.r==other.r and self.g==other.g and self.b==other.b)

  def __add__(self, other_color):
    r = self.r + other_color.r
    g = self.g + other_color.g
    b = self.b + other_color.b

    return color(r,g,b)

  def __mul__(self, other):
    r = self.r * other
    g = self.g * other
    b = self.b * other

    return color(r,g,b)
  __rmul__ = __mul__

  def __repr__(self):
    return "color(%s, %s, %s)" % (self.r, self.g,self.b)

  def toBytes(self):
    self.r = int(max(min(self.r, 255), 0))
    self.g = int(max(min(self.g, 255), 0))
    self.b = int(max(min(self.b, 255), 0))
    return bytes([self.b,self.g,self.r])