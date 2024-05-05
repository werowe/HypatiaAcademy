import logging

from injector import singleton
from scipy import stats
import numpy as np

@singleton
class LinearRegressionService:

    '''
    Net Income list examples (numbers for calculate_on_numbers method)

    DE Company: Deere & Company
    [980.70, 850.70, 649.20, 386.80, 690.50, 511.60, 351.20, 254.40, 495.40, 488.80, 285.30, 193.80, 802.40, 641.80, 510.30, -535.10, 1,208.30, 910.30, 784.80, 498.50, 1,134.90, 899.00, 722.00, 517.00, 666.00, 811.00, 757.00, 1,224.00, 1,790.00, 1,667.00, 1,283.00, 903.00, 2,098.00, 1,884.00, 2,246.00, 1,959.00, 2,860.00, 2,978.00, 2,369.00, 1,751.00]

    AMZN Company: Amazon.com Inc
    y: [108.00, -126.00, -437.00, 214.00, -57.00, 92.00, 79.00, 482.00, 513.00, 857.00, 252.00, 749.00, 724.00, 197.00, 256.00, 1,856.00, 1,629.00, 2,534.00, 2,883.00, 3,027.00, 3,561.00, 2,625.00, 2,134.00, 3,268.00, 2,535.00, 5,243.00, 6,331.00, 7,222.00, 8,107.00, 7,778.00, 3,156.00, 14,323.00, -3,844.00, -2,028.00, 2,872.00, 278.00, 3,172.00, 6,750.00, 9,879.00, 10,624.00]

    MCD Company: McDonald’s Corporation;
    [1,204.80, 1,387.10, 1,068.40, 1,097.50, 811.50, 1,202.40, 1,309.20, 1,206.20, 1,098.60, 1,092.90, 1,275.40, 1,193.40, 1,214.80, 1,395.10, 1,883.70, 698.70, 1,375.40, 1,496.30, 1,637.30, 1,415.30, 1,328.40, 1,516.90, 1,607.90, 1,572.20, 1,106.90, 483.80, 1,762.60, 1,377.20, 1,537.20, 2,219.30, 2,149.90, 1,638.80, 1,104.40, 1,188.00, 1,981.60, 1,903.40, 1,802.30, 2,310.40, 2,317.10, 2,039.00]

    LEVI Company: Levi Strauss & Co Class A
    [49.97, 11.46, 50.62, -6.00, 38.39, 11.69, 58.17, 101.18, 65.84, 30.73, 98.32, 96.17, 60.14, 17.52, 87.99, 115.75, -19.01, 74.93, 130.12, 97.10, 146.58, 28.23, 124.51, 95.30, 152.69, -363.55, 27.05, 56.67, 142.50, 64.72, 193.33, 152.99, 195.84, 49.74, 172.96, 150.56, 114.70, -1.60, 9.60, 126.90]

    DAL Company: Delta Air Lines Inc;
    [213.00, 801.00, 357.00, -712.00, 746.00, 1,485.00, 1,315.00, 980.00, 946.00, 1,546.00, 1,259.00, 622.00, 603.00, 1,224.00, 1,178.00, 299.00, 547.00, 1,025.00, 1,312.00, 1,019.00, 730.00, 1,443.00, 1,495.00, 1,099.00, -534.00, -5,717.00, -5,379.00, -755.00, -1,177.00, 652.00, 1,212.00, -408.00, -940.00, 735.00, 695.00, 829.00, -363.00, 1,827.00, 1,108.00, 2,037.00]

    DIS Company: Walt Disney Company
    [1,917.00, 2,245.00, 1,499.00, 2,182.00, 2,108.00, 2,483.00, 1,609.00, 2,880.00, 2,143.00, 2,597.00, 1,771.00, 2,479.00, 2,388.00, 2,366.00, 1,747.00, 4,423.00, 2,937.00, 2,916.00, 2,322.00, 2,788.00, 5,452.00, 1,760.00, 1,054.00, 2,107.00, 460.00, -4,721.00, -710.00, 17.00, 901.00, 918.00, 159.00, 1,104.00, 470.00, 1,409.00, 254.00, 1,279.00, 1,271.00, -460.00, 264.00, 1,911.00]

    F Company: Ford Motor Company
    [989.00, 1,311.00, 835.00, 52.00, 924.00, 1,885.00, 1,909.00, 2,655.00, 2,452.00, 1,970.00, 957.00, -783.00, 1,587.00, 2,042.00, 1,564.00, 2,409.00, 1,736.00, 1,066.00, 991.00, -116.00, 1,146.00, 148.00, 425.00, -1,672.00, -1,993.00, 1,117.00, 2,385.00, -2,788.00, 3,262.00, 561.00, 1,832.00, 12,282.00, -3,119.00, 667.00, -930.00, 1,289.00, 1,757.00, 1,917.00, 1,199.00, -526.00]
    '''

    def __init__(self):
        pass

    def calculate_on_numbers(self, numbers):
        if not numbers:
            logging.info(f'numbers not provided.')
            return self.__inint_regression_result()
        return self.__calculate(numbers)

    def calculate_on_history(self, history):
        if not history:
            logging.info(f'historic_values not provided.')
            return self.__inint_regression_result()
        numbers = [e.value for e in history]
        return self.__calculate(numbers)

    def __inint_regression_result(self):
        regression_result = RegressionResult()
        regression_result.linear_regression = LinearRegressionResult()
        regression_result.polynomial_regression_1 = PolynomialRegressionResult()
        regression_result.polynomial_regression_2 = PolynomialRegressionResult()
        regression_result.polynomial_regression_3 = PolynomialRegressionResult()
        return regression_result

    def __calculate(self, numbers):
        regression_result = self.__inint_regression_result()
        regression_result.x = list(range(0, len(numbers)))
        regression_result.y = [None if n is None else float(n) for n in numbers]
        # Linear regression cannot be calculated if None values in lists
        clean_x = []
        clean_y = []
        for idx, val in enumerate(regression_result.y):
            if val is not None:
                clean_x.append(idx)
                clean_y.append(val)

        regression_result.polynomial_regression_1 = self.__calculate_polynomial_regression(clean_x, clean_y, 1)
        regression_result.polynomial_regression_2 = self.__calculate_polynomial_regression(clean_x, clean_y, 2)
        regression_result.polynomial_regression_3 = self.__calculate_polynomial_regression(clean_x, clean_y, 3)
        regression_result.linear_regression = self.__calculate_linear_regression(clean_x, clean_y)
        return regression_result

    # deg is an order of polynom
    def __calculate_polynomial_regression(self, clean_x, clean_y, deg):
        result = PolynomialRegressionResult()
        if not clean_y or len(clean_y) < 5 :
            return result
        result.x = clean_x
        result.y = clean_y
        result.model = np.poly1d(np.polyfit(result.x, result.y, deg))
        return result

    def __calculate_linear_regression(self, clean_x, clean_y):
        result = LinearRegressionResult()
        result.x = clean_x
        result.y = clean_y
        if len(clean_y) <= 5:
            logging.info(f'Data list length: {len(clean_y)} too short to process')
            result.slope, result.intercept, result.r, result.p, result.std_err = 0, 0, 0, 0, 0
        else:
            result.slope, result.intercept, result.r, result.p, result.std_err = stats.linregress(clean_x, clean_y)
            result.slope = round(result.slope, 2)
            result.intercept = round(result.intercept, 2)
            result.r = round(result.r, 2)
            result.p = round(result.p, 4)
            result.std_err = round(result.std_err, 2)
        logging.info(f'slope: {result.slope}, intercept: {result.intercept}, r: {result.r}, p: {result.p}, '
                     f'std_err: {result.std_err}')
        return result


class RegressionResult(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.linear_regression = None
        self.polynomial_regression_1 = None
        self.polynomial_regression_2 = None
        self.polynomial_regression_3 = None


class LinearRegressionResult(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.slope = None
        self.intercept = None
        self.r = None
        self.p = None
        self.std_err = None


class PolynomialRegressionResult(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.model = None
