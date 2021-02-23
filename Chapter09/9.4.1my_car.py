"""
之前我是用章节名加程序名给py命名，因此会有9.4.1car这种模块名，但是导入的时候有问题
搜索以后下面这条连接给了下面这段代码解决，但是学Python不久，还是没有成功
https://www.itdaan.com/blog/2014/01/26/77572eeaee84b6792d337a59ff90ea6a.html
import imp

with open('models.admin.py', 'rb') as fp:

    models_admin = imp.load_module(

        'models_admin', fp, 'models.admin.py',

        ('.py', 'rb', imp.PY_SOURCE)

    )

所以只好把9.4.1car.py改成car.py按照书上的代码照常运行了
因此，各位以后也要注意尽量不要用小数点在py模块里面，或者用数字开头
因为数字开头也会报错，可参考下面这条连接
http://www.voidcn.com/article/p-sgggszwg-bsq.html
"""

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()