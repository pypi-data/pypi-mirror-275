def first_text():
    """
Абсолютно непрерывная случайная величина X
 может принимать значения только в отрезке [4,7]
. На этом отрезке плотность распределения случайной величины X
 имеет вид: f(x)=C(1+3x0,5+6x0,7+9x0,9)1,5
, где C
 – положительная константа. Найдите: 1) константу C
; 2) математическое ожидание E(X)
; 3) стандартное отклонение σX
; 4) квантиль уровня 0,8
 распределения X
.
.
    """

def first():
    """
    def f(x, C):
        return C * ((1 + 3*x**0.5 + 6*x**0.7 + 9*x**0.9)**1.5)
    def integral_C(C):
        result, _ = quad(f, 4, 7, args=(C))
        return result - 1
    res = opt.fsolve(integral_C, 0.1)
    C = res[0]
    class rv_continuous_f(rv_continuous):
        def _pdf(self, x):
            pdf_values = np.zeros_like(x)
            pdf_values = np.where((4 <= x) & (x <= 7), f(x, C), pdf_values)
            return pdf_values
    X = rv_continuous_f(a=4, b=7)
    print(C)
    X.mean()
    X.std()
    X.ppf(0.8)
    """

def second_text():
    """
    Случайная величина X
     равномерно распределена на отрезке [4,8]
    . Случайная величина Y
     выражается через X
     следующим образом: Y=(1+6X0,5+4X0,7+5X0,9)1,3
    . Найдите: 1) математическое ожидание E(Y)
    ; 2) стандартное отклонение σY
    ; 3) асимметрию As(Y)
    ; 4) квантиль уровня 0,8
     распределения Y
.
    """

def second():
    """
    a = 4
    b = 8
    def Y(x):
        return (1 + 6*(x**0.5) + 4*(x**0.7) + 5*(x**0.9))**1.3
    X = uniform(a, b-a)
    def E_Y():
        integrand = lambda x: Y(x) * X.pdf(x)
        EY_value, _ = quad(integrand, a, b)
        return EY_value
    def std_Y():
        integrand = lambda x: ((Y(x)-E_Y())**2)*X.pdf(x)
        Var_Y, _ = quad(integrand, a, b)
        return math.sqrt(Var_Y)
    def skew_Y():
        integrand = lambda x: (((Y(x) - E_Y()) / std_Y())**3) * X.pdf(x)
        skew, _ = quad(integrand, a, b)
        return skew
    np.around(E_Y(), 1)
    np.around(std_Y(), 2)
    np.around(skew_Y(), 4)
    q = 0.8
    q_Y = Y(X.ppf(q))
    np.around(q_Y, 3)
    """
def third_text():
    """
    Для нормального случайного вектора (X,Y)∼N(−8;16;49;1;0,8) найдите вероятность P((X−3)(Y−7)<0)

    """
def third():
    """
    mu_X = -8
    mu_Y = 16
    sigma_X = 49 ** 0.5
    sigma_Y = 1 ** 0.5
    ro = 0.8
    cov_XY = ro*sigma_X*sigma_Y

    mu_list = [mu_X,mu_Y]
    cov_matrix = [[sigma_X**2,cov_XY],[cov_XY,sigma_Y**2]]
    XY = multivariate_normal(mean=mu_list,cov=cov_matrix)
    P = XY.cdf([np.inf,7])-XY.cdf([3,7])+(XY.cdf([3,np.inf])-XY.cdf([3,7]))
    print(P)
    """

def fourth_text():
    """
    Для нормального случайного вектора (X,Y)∼N(−4;4;64;81;−0,31)
    найдите вероятность P((X−8)(X−10)(Y−1)<0)
    .
    """
def fourth():
    """
    mu_X = -4
    mu_Y = 4
    sigma_X = 64 ** 0.5
    sigma_Y = 81 ** 0.5
    ro = -0.31
    cov_XY = ro*sigma_X*sigma_Y

    mu_list = [mu_X, mu_Y]
    cov_matrix = [[sigma_X**2, cov_XY], [cov_XY, sigma_Y**2]]
    XY = multivariate_normal(mean=mu_list, cov=cov_matrix)
    X=norm(mu_X, sigma_X)
    Y=norm(mu_Y,sigma_Y)
    Pa=XY.cdf([8,1])
    Pb=X.cdf(10)-X.cdf(8)-(XY.cdf([10,1])-XY.cdf([8,1]))
    Pc=Y.cdf(1)-XY.cdf([10,1])

    PA=Pa+Pb+Pc
    print(PA)
    """

def fifth_text():
    """
    Случайный вектор (X,Y)
 имеет плотность распределения
    fX,Y(x,y)=18e^(−30x2−48xy+8x−30y2−5y−85/24)/π
    """

def fifth():
    """
    x, y = symbols('x y')
    print(x)
    Rational(85, 12)
    q = 60*x**2 + 96*x*y - 16*x + 60*y**2 + 10*y + Rational(85, 12)
    print(q)
    # diff - диф-ние по x
    eq_1 = diff(q, x)
    print(eq_1)
    eq_2 = diff(q, y)
    print(eq_2)
    solve({eq_1, eq_2}, {x, y})
    Cinv = Matrix([[51, 45], [45, 51]])
    print(Cinv)
    print(Cinv**(-1))
    Cinv = Matrix([[60, 48], [48, 60]])
    print(Cinv)
    print(Cinv**(-1))
    """