# Automatically generated by Pynguin.
import pytest
import doing_math as module0


def test_case_0():
    try:
        var0 = 2498
        var1 = 3660
        var2 = module0.add_some_numbers(var1, var0)
        assert var2 == 6158
        var3 = -724
        var4 = 389
        var5 = module0.add_some_numbers(var4, var0)
        assert var5 == 2887
        var6 = -1945
        var7 = module0.subtract_some_numbers(var6, var3)
        assert var7 == -1221
        var8 = -3806
        var9 = module0.subtract_some_numbers(var8, var3)
        assert var9 == -3082
        var10 = -1222
        var11 = module0.multiply_some_numbers(var10, var6)
        assert var11 == 2376790
        var12 = module0.divide_some_numbers(var6, var3)
        assert var12 == pytest.approx(2.68646408839779, abs=0.01, rel=0.01)
        var13 = module0.divide_some_numbers(var1, var6)
        assert var13 == pytest.approx(-1.8817480719794344, abs=0.01, rel=0.01)
        var14 = -2387
        var15 = 3159
        var16 = -1651
        var17 = module0.add_some_numbers(var1, var16)
        assert var17 == 2009
        var18 = module0.divide_some_numbers(var14, var15)
        assert var18 == pytest.approx(-0.7556188667299778, abs=0.01, rel=0.01)
        var19 = module0.divide_some_numbers(var0, var3)
        assert var19 == pytest.approx(-3.4502762430939224, abs=0.01, rel=0.01)
        var20 = 2235
        var21 = module0.add_some_numbers(var15, var20)
        assert var21 == 5394
        var22 = -398
        var23 = module0.multiply_some_numbers(var14, var22)
        assert var23 == 950026
        var24 = -2389
        var25 = -1455
        var26 = module0.subtract_some_numbers(var24, var25)
        assert var26 == -934
        var27 = module0.add_some_numbers(var0, var0)
        assert var27 == 4996
        var28 = 82
        var29 = module0.divide_some_numbers(var15, var28)
        assert var29 == pytest.approx(38.52439024390244, abs=0.01, rel=0.01)
        var30 = None
        var31 = module0.multiply_some_numbers(var6, var30)
    except BaseException:
        pass


def test_case_1():
    try:
        var0 = 2517
        var1 = module0.multiply_some_numbers(var0, var0)
        assert var1 == 6335289
        var2 = None
        var3 = 876
        var4 = 1147
        var5 = 1931
        var6 = module0.floor_divide_some_numbers(var4, var5)
        assert var6 == 0
        var7 = module0.floor_divide_some_numbers(var3, var2)
    except BaseException:
        pass