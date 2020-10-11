# ===============================================================
# Math
# ===============================================================

class V3(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return "V3(%s, %s, %s)" % (self.x, self.y, self.z)

class V2(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "V2(%s, %s)" % (self.x, self.y)

# V2 = namedtuple('Point2', ['x', 'y'])
# V3 = namedtuple('Point3', ['x', 'y', 'z'])

def sum(v0, v1):
  """
    Input: 2 size 3 vectors
    Output: Size 3 vector with the per element sum
  """
  return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

def sub(v0, v1):
  """
    Input: 2 size 3 vectors
    Output: Size 3 vector with the per element substraction
  """
  return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

def mul(v0, k):
  """
    Input: 2 size 3 vectors
    Output: Size 3 vector with the per element multiplication
  """
  return V3(v0.x * k, v0.y * k, v0.z *k)

def dot(v0, v1):
  """
    Input: 2 size 3 vectors
    Output: Scalar with the dot product
  """
  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0, v1):
  """
    Input: 2 size 3 vectors
    Output: Size 3 vector with the cross product
  """
  return V3(
    v0.y * v1.z - v0.z * v1.y,
    v0.z * v1.x - v0.x * v1.z,
    v0.x * v1.y - v0.y * v1.x,
  )

def length(v0):
  """
    Input: 1 size 3 vector
    Output: Scalar with the length of the vector
  """
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5

def norm(v0):
  """
    Input: 1 size 3 vector
    Output: Size 3 vector with the normal of the vector
  """
  v0length = length(v0)

  if not v0length:
    return V3(0, 0, 0)

  return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)

def reflect(I, N):
  Lm = mul(I, -1)
  n = mul(N, 2 * dot(Lm, N))
  return norm(sub(Lm, n))

def bbox(*vertices):
  """
    Input: n size 2 vectors
    Output: 2 size 2 vectors defining the smallest bounding rectangle possible
  """
  xs = [ vertex.x for vertex in vertices ]
  ys = [ vertex.y for vertex in vertices ]
  xs.sort()
  ys.sort()

  return V2(int(xs[0]), int(ys[0])), V2(int(xs[-1]), int(ys[-1]))


def barycentric(A, B, C, P):
  """
    Input: 3 size 2 vectors and a point
    Output: 3 barycentric coordinates of the point in relation to the triangle formed
            * returns -1, -1, -1 for degenerate triangles
  """
  bary = cross(
    V3(C.x - A.x, B.x - A.x, A.x - P.x),
    V3(C.y - A.y, B.y - A.y, A.y - P.y)
  )

  if abs(bary.z) < 1:
    return -1, -1, -1   # this triangle is degenerate, return anything outside

  return (
    1 - (bary.x + bary.y) / bary.z,
    bary.y / bary.z,
    bary.x / bary.z
  )

def reflect(I, N):
  Lm = mul(I, -1)
  n = mul(N, 2 * dot(Lm, N))
  return norm(sub(Lm, n))

def refract(I, N, refractive_index):
  etai = 1
  etat = refractive_index

  cosi = -dot(I, N)

  if cosi < 0:
    cosi = -cosi
    etai, etat = etat, etai
    N = mul(N, -1)

  eta = etai/etat

  k = 1 - eta ** 2 * (1 - cosi ** 2)

  if k < 0:
    return V3(1,0,0)

  cost = k**(1/2)

  return norm(
    sum(
      mul(I, eta), # A
      mul(N, (eta * cosi - cost))
    )
  )