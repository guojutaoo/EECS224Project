#functions
def exp_mode(base, exponent, n):
  bin_array = bin(exponent)[2:][::-1]
  r = len(bin_array)
  base_array = []
  pre_base = base
  base_array.append(pre_base)
  for _ in range(r - 1):
    next_base = (pre_base * pre_base) % n
    base_array.append(next_base)
    pre_base = next_base
  a_w_b = __multi(base_array, bin_array)
  return a_w_b % n


def __multi(array, bin_array):
  result = 1
  for index in range(len(array)):
    a = array[index]
    if not int(bin_array[index]):
      continue
    result *= a
  return result


def exgcd(m, n):
	if n == 0:
		x = 1
		y = 0
		return (m,x,y)
	a1 = b = 1
	a = b1 = 0
	c = m
	d = n
	q = int(c/d)
	r = c%d
	while r:
		c = d
		d = r
		t = a1
		a1 = a
		a = t-q*a
		t = b1
		b1 = b
		b = t-q*b
		q = int(c/d)
		r = c%d
	x = a
	y = b
	return (d,x,y)


def priv_gen(m, n):
    a = list(exgcd(m, n))
    while a[1] <= 0:
        a[1] += n
    return a[1]
