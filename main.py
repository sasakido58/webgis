from flask import Flask
from flask import render_template, request, redirect, url_for, Flask, session, abort, flash
from flask_wtf import Form

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from config import app, db, csrf
from database import db_session
import services

app = Flask(__name__)
app = Flask(__name__, static_folder='D:\\Sync\\Python\\webgis\\testgis\\templates\\static')

@app.route("/",methods = ['GET', 'POST'])
def index():
    ## phan doc cac yeu cau:
    ketqua = []
    tinhthanh_chon = request.args.get('tp', "")
    chude_chon = request.args.get('chude', "")
    nam_chon = request.args.get('nam', "")
    phanmem_chon = request.args.get('phanmem', "")
    phuongphap_chon = request.args.get('phuongphap', "")
    ## phan truy van csdl, render ra file:
    list_tinhthanh = []                                  #tinhthanh
    list_quanhuyen = []                                  #quanhuyen
    list_chude = []                                      # chude
    list_nam = [] 
    list_phanmem = []                                    # phanmem
    list_phuongphap = []                             
    sql_str = ""
    sql_str, list_tinhthanh = services.getDataTinh()
    #sql_str, list_quanhuyen = services.getDataHuyen(list_tinhthanh[0][2])  #id = 0, code_tinh = 1, name_tinh = 2
    sql_str, list_chude = services.getDataNhom()
    sql_str, list_nam = services.getDataNam()
    sql_str, list_phanmem = services.getDataSoftware()
    sql_str, list_phuongphap = services.getDataPhuongPhap()

    ketqua = []
    print("Chon tinh/thanh: ", tinhthanh_chon)
    print("Chon chu de: ", chude_chon)
    print("nam chon: ", nam_chon)
    print("phan mem chon: ", phanmem_chon)
    print("phuong phap chon: ", phuongphap_chon)

    if (chude_chon == 'chude'):
        chude_chon = ""

    sql, ketqua = services.TimKiem(tinhthanh_chon, chude_chon, nam_chon, phanmem_chon, phuongphap_chon)
    print(sql)

    ##    if (tinhthanh_chon) or (1==1):                          #tinhthanh
##        sql, ketqua = services.TimKiem(tinhthanh_chon)
##
##    if (chude_chon) or (1==1):                              # chude
##        sql, ketqua = services.TimKiem()
##
##    if (nam_chon) or (1==1):                          #nam
##        sql, ketqua = services.TimKiem()
##
##    if (phanmem_chon) or (1==1):                          #
##        sql, ketqua = services.TimKiem()
##
##    if (phuongphap_chon) or (1==1):                          #
##        sql, ketqua = services.TimKiem()

    return render_template('index.html', list_thanhpho = list_tinhthanh, list_huyen = list_quanhuyen, list_chude = list_chude, list_nam = list_nam, list_phanmem = list_phanmem, list_phuongphap = list_phuongphap, list_baibao = ketqua)

@app.route('/timeline', methods=['GET', 'POST'])
def timeline():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('timeline.html')


# THEM DOAN NAY DE THUC THI:
if __name__ == "__main__":
    app.run()
