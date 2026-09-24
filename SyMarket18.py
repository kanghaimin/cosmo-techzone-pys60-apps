NOTE = 'DILARANG KERAS MELAKUKAN PERUBAHAN PADA SCRIPT APLIKASI INI TANPA SEIZIN DARI PIHAK PENGEMBANG (COSMO TECHZONE)'
import e32
from os import path as op
from appuifw import app as A
from appuifw import Listbox as L
from socket import select_access_point as SAP, access_point as AP, set_default_access_point as DAP
import ini
target_path = "e:\\private\\88888818\\SyMarket.pyc"
if op.exists(target_path):
 ds = 'E'
else:
 ds = 'C'
apa = (ds + ':\\data\\cosmotech.symarket\\')
ace = (apa+'accint.dat')
class SyMarket :
    __module__ = __name__
    def __init__(a):
        if ini.read(ace)['id'] == 0 : 
            pass
        else : 
            x = AP(ini.read(ace)['id'])
            DAP(x)
        a.menu = [(u'Download', u'Beragam file untuk symbian mu'), (u'Umpan balik', u'Kirim laporan atau minta file'), (u'Donasi (QRIS)', u'Dukung developer'), (u'Jalur akses', ini.read(ace)['ap']), (u'Periksa pembaruan', u'v1.8, \xa92026 Cosmo TechZone')]
        a.li = ['sapp', 'sfont', 'sgame', 'smod', 'sskin', 'stheme', 'swm', 'sother']
        a.L = L(a.menu, a.sel)
        A.body = a.L
        A.exit_key_handler = a.quit
        A.menu = []

        a.app_lock = e32.Ao_lock()

        a.app_lock.wait()

    def urut_nama_file(a, x, y):
        nama_x = x.split('/')[-1]
        nama_y = y.split('/')[-1]
        if nama_x < nama_y: return -1
        if nama_x > nama_y: return 1
        return 0


    def quit(a):
        a.app_lock.signal()
        A.set_exit()


    def pomen(a):
        from appuifw import popup_menu as pm
        isian = [u'Kirim umpan balik', u'Riwayat umpan balik']
        pilih = pm(isian, u"")

        if pilih == 0:
            a.up()
        elif pilih == 1:
            a.history()
        else:
            pass


    def down(a):
        from appuifw import popup_menu as pm
        daf = [u'Aplikasi', u'Fonts', u'Game/Permainan', u'Modding', u'Skins', u'Tema', u'Watermark', u'Lainnya']
        pilih = pm(daf, u'Kategori:')
        if pilih == None : 
            return 0
        from urllib import urlopen as u
        try :
            site = u(('http://bimasakti.rf.gd/' + a.li[pilih] + '.txt'))
        except :
            from appuifw import note as n
            n(u"Tidak dapat terhubung ke server", 'error')
            return 0
        isi = site.read().decode('latin1')
        isi = isi.replace('\r', '')
        pecah = isi.split('\n')
        uniko = [(u'' + i) for i in pecah]
        from appuifw import selection_list as sel
        nuniko = []
        for i in uniko:
            nama_file = i.split('/')[-1]
            nuniko.append(nama_file)
        pili = sel(nuniko, 1)
        if pili == None : 
            return 0
        import laa
        laa.execute(268471609, (uniko[pili]))

    def hash_string(a, s):
        h = 0

        for c in s:
            h = (h * 31 + ord(c)) & 0xFFFFFFFF

        return h


    def up(a):
        from sysinfo import imei
        from appuifw import query, note
        req = query(u"Permintaan file/laporan:", "text")
        if req == None:
            return
        req = str(req)

        imei = imei()
        h = a.hash_string(imei)
        id10 = "%010d" % (h % 10000000000)
        
        import urllib
        import httplib

        url = "http://symarket.onlinewebshop.net/symarket-req.php"

        data = urllib.urlencode({
            "id10": id10,
            "req": req
        })

        urllib.urlopen(url, data)
        note(u'Mengirim umpan balik..')
        note(u'Berhasil!','conf')
        
    def history(a):
        from sysinfo import imei
        import laa

        imei = imei()
        h = a.hash_string(imei)
        id10 = "%010d" % (h % 10000000000)

        url = "http://symarket.onlinewebshop.net/symarket-his.php?id="+id10

        laa.execute(268471609, unicode(url))

    def about(a):
        import laa
        laa.execute(268471609, u'http://cosmotz.blogspot.com/2019/01/symarket.html')

    def donate(a):
        from appuifw import Content_handler as C
        C().open(apa+'cosmotz_support.png')

    def jalur(a):
        from socket import access_points as alist
        from appuifw import popup_menu as pm
        li=alist()
        lis=[i['name'] for i in li]
        lis.insert(0,u'Selalu tanya')
        sel=pm(lis,u'Pilih jalur akses')
        if sel==None:return 0
        elif sel==0:
            ini.write(ace,{'id':0,'ap':lis[0]})
            a.menu[3]=(u'Jalur akses',lis[0])
            a.L.set_list(a.menu,3)
            DAP(None)
        else:
            ini.write(ace,{'id':li[sel-1]['iapid'],'ap':li[sel-1]['name']})
            a.menu[3]=(u'Jalur akses',li[sel-1]['name'])
            a.L.set_list(a.menu,3)
            x=AP(ini.read(ace)['id'])
            DAP(x)


    def sel(a):
        last = a.L.current()
        if last == 0 : 
            a.down()
        elif last == 1 : 
            a.pomen()
        elif last == 2 : 
            a.donate()
        elif last == 3 : 
            a.jalur()
        else : 
            a.about()




SyMarket()
