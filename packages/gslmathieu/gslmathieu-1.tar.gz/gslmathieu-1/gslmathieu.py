

# goal: provide access to GSL's mathieu functions
# https://www.gnu.org/software/gsl/doc/html/specfunc.html
#
# First stage: basic acess to scalar functions
#  double gsl_sf_mathieu_a(int n, double q)
#  double gsl_sf_mathieu_b(int n, double q)
#  double gsl_sf_mathieu_ce(int n, double q, double x)
#  double gsl_sf_mathieu_se(int n, double q, double x)
#  double gsl_sf_mathieu_Mc(int j, int n, double q, double x)
#  double gsl_sf_mathieu_Ms(int j, int n, double q, double x)
#
# In the first stage, the input is always a single floating-point number
#
# Second stage: acess to the error-handled functions *_e
# behavior: never throw exceptions, return NaN on error
#
# Third stage: implement ``fake'' vectorization.
#
# Fourth stage: access to the *_array based functions
# When the _array function exists, vectorization goes through it.  Otherwise,
# fake vectorization is used.
#
# (The fourth stage is an internal optimization not visible in the interface).
#


# globally accessible C functions
__gsl_sf_mathieu_a  = 0
__gsl_sf_mathieu_b  = 0
__gsl_sf_mathieu_ce = 0
__gsl_sf_mathieu_se = 0
__gsl_sf_mathieu_Mc = 0
__gsl_sf_mathieu_Ms = 0


# internal function to initialize the C interface
def __setup_functions():
	global __gsl_sf_mathieu_a
	global __gsl_sf_mathieu_b
	global __gsl_sf_mathieu_ce
	global __gsl_sf_mathieu_se
	global __gsl_sf_mathieu_Mc
	global __gsl_sf_mathieu_Ms
	if __gsl_sf_mathieu_a != 0: return

	from ctypes import CDLL, c_int, c_double
	from ctypes.util import find_library

	libgsl = CDLL(find_library('gsl'))

	libgsl.gsl_sf_mathieu_a.argtypes = [c_int, c_double]
	libgsl.gsl_sf_mathieu_a.restype = c_double
	__gsl_sf_mathieu_a = libgsl.gsl_sf_mathieu_a

	libgsl.gsl_sf_mathieu_b.argtypes = [c_int, c_double]
	libgsl.gsl_sf_mathieu_b.restype = c_double
	__gsl_sf_mathieu_b = libgsl.gsl_sf_mathieu_b

	libgsl.gsl_sf_mathieu_ce.argtypes = [c_int, c_double, c_double]
	libgsl.gsl_sf_mathieu_ce.restype = c_double
	__gsl_sf_mathieu_ce = libgsl.gsl_sf_mathieu_ce

	libgsl.gsl_sf_mathieu_se.argtypes = [c_int, c_double, c_double]
	libgsl.gsl_sf_mathieu_se.restype = c_double
	__gsl_sf_mathieu_se = libgsl.gsl_sf_mathieu_se

	libgsl.gsl_sf_mathieu_Mc.argtypes = [c_int, c_int, c_double, c_double]
	libgsl.gsl_sf_mathieu_Mc.restype = c_double
	__gsl_sf_mathieu_Mc = libgsl.gsl_sf_mathieu_Mc

	libgsl.gsl_sf_mathieu_Ms.argtypes = [c_int, c_int, c_double, c_double]
	libgsl.gsl_sf_mathieu_Ms.restype = c_double
	__gsl_sf_mathieu_Ms = libgsl.gsl_sf_mathieu_Ms

	# disable the error handling
	libgsl.gsl_set_error_handler_off()



# API stage 1, scalar arguments, no error management (calls abort() on error)

def __api_stage1_a(n, q):
	"""Characteristic values of even Mathieu function"""
	__setup_functions()
	return __gsl_sf_mathieu_a(n, q)

def __api_stage1_b(n, q):
	"""Characteristic values of odd Mathieu function"""
	__setup_functions()
	return __gsl_sf_mathieu_b(n, q)

def __api_stage1_ce(n, q, x):
	"""Even angular Mathieu function"""
	__setup_functions()
	return __gsl_sf_mathieu_ce(n, q, x)

def __api_stage1_se(n, q, x):
	"""Odd angular Mathieu function"""
	__setup_functions()
	return __gsl_sf_mathieu_se(n, q, x)

def __api_stage1_Mc(j, n, q, x):
	"""Even radial Mathieu function"""
	__setup_functions()
	return __gsl_sf_mathieu_Mc(j, n, q, x)

def __api_stage1_Ms(j, n, q, x):
	"""Odd radial Mathieu function"""
	__setup_functions()
	return __gsl_sf_mathieu_Ms(j, n, q, x)


# API stage 1, scalar arguments, no error management (calls abort() on error)


__gslmathieu_stage = "stage3"
if __gslmathieu_stage == "stage1":
	a  = __api_stage1_a
	b  = __api_stage1_b
	ce = __api_stage1_ce
	se = __api_stage1_se
	Mc = __api_stage1_Mc
	Ms = __api_stage1_Ms
if __gslmathieu_stage == "stage3":
	from numpy import vectorize as __vectorize
	a  = __vectorize(__api_stage1_a)
	b  = __vectorize(__api_stage1_b)
	ce = __vectorize(__api_stage1_ce)
	se = __vectorize(__api_stage1_se)
	Mc = __vectorize(__api_stage1_Mc)
	Ms = __vectorize(__api_stage1_Ms)


# API
version = 1

__all__ = [ "a", "b", "ce", "se", "Mc", "Ms" ]
