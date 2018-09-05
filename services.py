import sys 
reload (sys)
sys.setdefaultencoding("utf-8")

#Tao list tinh
def getDataTinh():
    sql_str = 'select * from tinh_thanh order by name_tinh'
    from database import db_session
    data1 = db_session().execute(sql_str)
    list = []
    for row in data1:
        tinhthanh = convertRowDataToTinhThanh(row)
        list.append(tinhthanh)
    return sql_str, list
def convertRowDataToTinhThanh(row):
    return {'gid': row['gid'],'code_tinh': row['code_tinh'], 'name_tinh':row['name_tinh']} # cot ten la cot name_vn
#tao list huyen
def getDataHuyen(tentinh):
    sql_str = "select * from quan_huyen where name_tinh = '" + tentinh + "' "
    from database import db_session
    data1 = db_session().execute(sql_str)
    list = []
    for row in data1:
        quanhuyen = convertRowDataToQuanHuyen(row)
        list.append(quanhuyen)
    return sql_str, list

def convertRowDataToQuanHuyen(row):
    # name_3 la ten quan/huyen, name_2 la ten tinh/thanh
    return {'gid': row['gid'], 'code_huyen':row['code_huyen'], 'name_tinh':row['name_tinh'], 'name_huyen':row['name_huyen']}

#tao list chu de
def getDataNhom():
    sql_str = 'select * from nhom_bai_bao'
    from database import db_session
    data1 = db_session().execute(sql_str)
    list = []
    for row in data1:
        chude = convertRowDataToChuDe(row)
        list.append(chude)
    return sql_str, list
def convertRowDataToChuDe(row):
    return {'manhom': row['manhom'],'tennhom': row['tennhom'], 'nhom':row['nhom']} # cot 

# tao list nam
def getDataNam():
    sql_str = 'select distinct(nam) from bai_bao'
    from database import db_session
    data1 = db_session().execute(sql_str)
    list1 = []
    for row in data1:
        nam = convertRowDataToNam(row)
        #if (list1.count(nam['nam'])==0):
        list1.append(nam)
    return sql_str, list1
def convertRowDataToNam(row):
    return {'nam':row['nam']}
    #return {'baibao_id': row['baibao_id'],'mabaibao': row['mabaibao'], 'nam':row['nam'], 'nhom': row['nhom']} # cot 

# tao list phanmem
def getDataSoftware():
    sql_str = 'select distinct(ten_software), software_id from phan_mem'
    from database import db_session
    data1 = db_session().execute(sql_str)
    list = []
    for row in data1:
        phanmem = convertRowDataToSoftware(row)
        list.append(phanmem)
    return sql_str, list
def convertRowDataToSoftware(row):
    return {'software_id': row['software_id'],'ten_software':row['ten_software']} # cot 

# tao list phuongphap
def getDataPhuongPhap():
    sql_str = 'select distinct(kythuatchinh),kythuat_id from chi_tiet_ky_thuat'
    from database import db_session
    data1 = db_session().execute(sql_str)
    list = []
    for row in data1:
        phuongphap = convertRowDataToPhuongPhap(row)
        list.append(phuongphap)
    return sql_str, list
def convertRowDataToPhuongPhap(row):
    return {'kythuat_id': row['kythuat_id'],'kythuatchinh':row['kythuatchinh']} # cot 

# nut tim kiem
def TimKiem(tp = "", chude = "", nam = "", phanmem = "", phuongphap = ""):
    #sql_str = 'select * from bai_bao'  # <--- chon tat ca bai bao!
    sql_str = '  select nam, bai_bao.mabaibao baibao_id,tenbai,tacgia,kythuatchinh, chi_tiet_ky_thuat.kythuat_id nhom_kythuat, '
    sql_str = sql_str + ' tennhom, nhom_bai_bao.nhom manhom, don_vi_hanh_chinh.code_tinh tinh, tinh_thanh.name_tinh tentinh '
    sql_str = sql_str + ' from bai_bao '
    sql_str = sql_str + ' JOIN nhom_bai_bao ON (bai_bao.nhom) = (nhom_bai_bao.nhom) '
    sql_str = sql_str + ' JOIN chi_tiet_ky_thuat ON bai_bao.mabaibao = chi_tiet_ky_thuat.mabaibao '
    sql_str = sql_str + ' JOIN don_vi_hanh_chinh ON bai_bao.mabaibao = (don_vi_hanh_chinh.mabaibao) '
    sql_str = sql_str + ' JOIN tinh_thanh ON (tinh_thanh.code_tinh) = (don_vi_hanh_chinh.code_tinh) '
    where_str = " where 1 = 1 "
    if (tp != ""):
        where_str = where_str + " and don_vi_hanh_chinh.code_tinh = '" + tp + "'"
    if (chude != ""):
        where_str = where_str + " and nhom_bai_bao.manhom = '" + chude + "'"
    if (nam != ""):
        where_str = where_str + " and nam = '" + nam + "'"
    if (phanmem != ""):
        where_str = where_str + " and nhom_bai_bao.manhom = '" + chude + "'"
    if (phuongphap != ""):
        where_str = where_str + " and chi_tiet_ky_thuat.kythuat_id = '" + phuongphap + "'"
    sql_str = sql_str + where_str
    from database import db_session
    data1 = db_session().execute(sql_str)
    list1 = []
    ma_baibao = []
    for row in data1:
        baibao = convertRowDataToBaiBao(row)
        # Chi lay 1 bai bao:
        if (ma_baibao.count(baibao['baibao_id'])==0): # kiem tra bai bao da co trong danh sach chua
            ma_baibao.append(baibao['baibao_id'])  # dua vao trong danh sach de lan sau kiem tra
            list1.append(baibao)  # dua vao trong danh sach ket qua
    return sql_str, list1

def convertRowDataToBaiBao(row):
    return {'baibao_id': row['baibao_id'],'nam': row['nam'],
            'tacgia':row['tacgia'], 'donvi': row['tinh'], 'tenbai':row['tenbai'],
            'kythuat_id': row['nhom_kythuat'], 'kythuatchinh': row['kythuatchinh'],
            'chude' : row['tennhom'], 'tentinh': row['tentinh']} # 

