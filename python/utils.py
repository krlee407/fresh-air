from math import sqrt
import numpy as np

vec = np.array([[40.126666666666665, 116.6152777777778],
  [39.986944444444454, 116.29055555555556],
  [40.44944444444444, 115.96888888888887],
  [40.3775, 116.86416666666666],
  [40.35777777777777, 116.62694444444445],
  [40.65888888888889, 117.11166666666666],
  [40.16944444444445, 117.11777777777776],
  [39.8475, 116.75666666666666],
  [39.9525, 116.50083333333332],
  [40.223333333333336, 116.21166666666667],
  [39.9738888888889, 115.69222222222223],
  [39.88777777777778, 116.15638888888893],
  [39.806111111111115, 116.46944444444445],
  [39.9425, 116.20527777777778],
  [39.87027777777778, 116.24527777777777],
  [39.718611111111116, 116.35444444444445],
  [39.77305555555555, 116.19416666666667],
  [39.728611111111114, 115.74055555555556],
  [51.46598327, 0.184877127],
  [51.46598327, 0.184877127],
  [51.522287, -0.12584800000000002],
  [51.52770662, -0.129053205],
  [51.544219, -0.175284],
  [51.51452534, -0.104515626],
  [51.51384718, -0.077765682],
  [51.410039000000005, -0.127523],
  [51.490532, 0.074003],
  [51.45258, 0.070766],
  [51.486957000000004, 0.095111],
  [51.456357000000004, 0.040725],
  [51.4563, 0.08560599999999999],
  [51.617327, -0.298775],
  [51.52078746, 0.20546070600000002],
  [51.48878, -0.44162700000000005],
  [51.52104675, -0.21349214],
  [51.52104675, -0.21349214],
  [51.474954, -0.039641],
  [51.56948433, 0.082907475],
  [51.42525604, -0.345608291],
  [51.3892869, -0.141661525],
  [51.51504617, -0.008418493],
  [51.52254, -0.15459]])

station = ['shunyi_meo',
  'hadian_meo',
  'yanqing_meo',
  'miyun_meo',
  'huairou_meo',
  'shangdianzi_meo',
  'pinggu_meo',
  'tongzhou_meo',
  'chaoyang_meo',
  'pingchang_meo',
  'zhaitang_meo',
  'mentougou_meo',
  'beijing_meo',
  'shijingshan_meo',
  'fengtai_meo',
  'daxing_meo',
  'fangshan_meo',
  'xiayunling_meo',
  'BX9',
  'BX1',
  'BL0',
  'CD9',
  'CD1',
  'CT2',
  'CT3',
  'CR8',
  'GN0',
  'GR4',
  'GN3',
  'GR9',
  'GB0',
  'HR1',
  'HV1',
  'LH0',
  'KC1',
  'KF1',
  'LW2',
  'RB7',
  'TD5',
  'ST5',
  'TH4',
  'MY7']

def get_nearest_station (lat, lon): # 0 : beijing, 1 : london
    result = []    
    
    for v in vec:
        result.append(pow(v[0]-lat,2)+pow(v[1]-lon,2))
    
    min_idx = result.index(min(result))
    
    return(station[min_idx])

def get_nearest_station_v2 (lat, lon):
    ind = np.array([lat, lon])
    result = np.sum((vec - ind) ** 2, axis = 0)

    return station[np.argmin(result)]

def get_nearest_station_v3 (lat_series, lon_series):
    lat = np.array(lat_series)
    lon = np.array(lon_series)
    
    T1 = (np.reshape(vec.T[0], (-1,1)) - np.reshape(lat, (1,-1))) ** 2
    T2 = (np.reshape(vec.T[1], (-1,1)) - np.reshape(lon, (1,-1))) ** 2
    
    idx = np.argmin(T1+T2, axis=0)
    
    return [station[i] for i in idx]

station_aq = ['dongsi', 'tiantan', 'guanyuan', 'wanshouxigong',
       'aotizhongxin', 'nongzhanguan', 'wanliu', 'beibuxinqu',
       'zhiwuyuan', 'fengtaihuayuan', 'yungang', 'gucheng',
       'fangshan', 'daxing', 'yizhuang', 'tongzhou',
       'shunyi', 'pingchang', 'mentougou', 'pinggu',
       'huairou', 'miyun', 'yanqin', 'dingling', 'badaling',
       'miyunshuiku', 'donggaocun', 'yongledian', 'yufa',
       'liulihe', 'qianmen', 'yongdingmennei', 'xizhimenbei',
       'nansanhuan', 'dongsihuan', 'BX9', 'BX1', 'BL0', 'CD9', 'CD1',
       'CT2', 'CT3', 'CR8', 'GN0', 'GR4', 'GN3', 'GR9', 'GB0', 'HR1',
       'HV1', 'LH0', 'KC1', 'KF1', 'LW2', 'RB7', 'TD5', 'ST5', 'TH4', 'MY7'] # aq 기준

grid_aq = ['beijing_grid_303',
 'beijing_grid_303',
 'beijing_grid_282',
 'beijing_grid_303',
 'beijing_grid_304',
 'beijing_grid_324',
 'beijing_grid_283',
 'beijing_grid_263',
 'beijing_grid_262',
 'beijing_grid_282',
 'beijing_grid_239',
 'beijing_grid_261',
 'beijing_grid_238',
 'beijing_grid_301',
 'beijing_grid_323',
 'beijing_grid_366',
 'beijing_grid_368',
 'beijing_grid_264',
 'beijing_grid_240',
 'beijing_grid_452',
 'beijing_grid_349',
 'beijing_grid_392',
 'beijing_grid_225',
 'beijing_grid_265',
 'beijing_grid_224',
 'beijing_grid_414',
 'beijing_grid_452',
 'beijing_grid_385',
 'beijing_grid_278',
 'beijing_grid_216',
 'beijing_grid_303',
 'beijing_grid_303',
 'beijing_grid_283',
 'beijing_grid_303',
 'beijing_grid_324',
 'london_grid_472',
 'london_grid_472',
 'london_grid_409',
 'london_grid_409',
 'london_grid_388',
 'london_grid_409',
 'london_grid_409',
 'london_grid_408',
 'london_grid_451',
 'london_grid_451',
 'london_grid_451',
 'london_grid_430',
 'london_grid_451',
 'london_grid_368',
 'london_grid_472',
 'london_grid_346',
 'london_grid_388',
 'london_grid_388',
 'london_grid_430',
 'london_grid_452',
 'london_grid_366',
 'london_grid_408',
 'london_grid_430',
 'london_grid_388']

def get_nearest_grid(station_id):
    return grid_aq[station_aq.index(station_id)]

def get_nearest_station_v4(grid_id):
    return station_aq[grid_aq.index(grid_id)]