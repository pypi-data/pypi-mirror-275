import request.request as rq

"""
获取指定日历下的假期数据
参数:
  calendar -- 日历 CFETS
"""


def get_holidays(calendar, token):
    return rq.post("/capdata/get/holidays/" + calendar, None, token)


"""
获取基准利率定义数据
参数:
  ir_index -- 基准利率编码列表 ['USDLIBOR_2W','SIBOR_12M']
"""


def get_ir_index(ir_index, token):
    return rq.post("/capdata/get/ir/index", ir_index, token)


"""
获取产品信息参考数据
参数:
  inst -- 产品编码列表 ['zc17060604.SH','zc17021505.SH']
"""


def get_instrument(inst, token):
    return rq.post("/capdata/get/instrument", inst, token)


"""
获取产品模板参考数据  
参数:
  inst -- 模板编码列表 ['CNY_FR_007_SWAP','SHIBOR_USDLIBOR_3M_SWAP','USDCNY_CASH','CN_TREAS_ZERO','EUR_CASH_DEPO']
"""


def get_inst_template(inst, token):
    return rq.post("/capdata/get/inst/template", inst, token)
