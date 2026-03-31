import numpy as np
import sklearn

linear_model = sklearn.linear_model

years="1.2 1.4 1.6 2.1 2.3 3 3.1 3.3 3.3 3.8 4 4.1 4.1 4.2 4.6 5 5.2 5.4 6 6.1 6.9 7.2 8 8.3 8.8 9.1 9.6 9.7 10.4 10.6".split(" ")

years = [float(x.replace(",", ".")) for x in years]

x = np.array([years]).reshape(1, -1)


salary="""39344
46206
37732
43526
39892
56643
60151
54446
64446
57190
63219
55795
56958
57082
61112
67939
66030
83089
81364
93941
91739
98274
101303
113813
109432
105583
116970
112636
122392
121873""".split("\n")



salary = [float(x.replace(",", ".")) for x in salary]


# this instantiates the linear regression object

lr = linear_model.LinearRegression()

'''
We instantiate the linear regression object.

What does that do.   solve y = mx + b where x is years and y is salary.

fit calculates m and b

'''


y = np.array([salary]).reshape(1, -1)


preds= lr.fit(x, y)

a = np.array([[1.5]])

o=lr.predict(a)

print("predicted salary", o)
