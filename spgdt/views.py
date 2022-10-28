from calendar import month
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from spgdt.forms import AddpbfreeForm

from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db import connection
import pandas as pd


def spgdt(request):
    telps = Telp.objects.all()
    context = {'telps': telps}
    return render(request, 'spgdt/main.html', context)


def addspgdt(request):
    pbfrees = Pbfree.objects.all()
    context = {'pbfrees': pbfrees}
    return render(request, 'spgdt/addspgdt.html', context)


def pb(request):
    pbfrees = Pbfree.objects.all()
    context = {'pbfrees': pbfrees}
    return render(request, 'spgdt/datatables/pbfree.html', context)


def giat(request):
    data = Giat.objects.all()
    context = {'data': data}
    return render(request, 'spgdt/datatables/giat.html', context)


def chart_giat(request):
    # item = Giat.objects.all().values()
    item = Giat.objects.filter(ket='P3K')
    df = pd.DataFrame(item)
    df1 = df.ket.tolist()
    df = df['tgl'].tolist()
    mydict = {
        'df': df,
        'df1': df1
    }
    return render(request, 'spgdt/chart.html', context=mydict)


def chart_pb(request):
    pbfrees = Pbfree.objects.all()
    pbfrees_count = pbfrees.count()  # <-count pengobatan gratis
    giats = Giat.objects.all()
    giats_count = giats.count()  # <-count kegiatan
    telps = Telp.objects.all()
    telps_count = telps.count()  # <-count telp
    videos = Video_giat.objects.all()
    video_count = videos.count()  # <-count video kegiatan

    context = {
        'pbfrees': pbfrees, 'pbfrees_count': pbfrees_count,
        'giats': giats, 'giats_count': giats_count,
        'telps': telps, 'telps_count': telps_count,
        'videos': videos, 'video_count': video_count,
    }
    return render(request, 'spgdt/chart2.html', context)


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


def getpb(request):
    if request.method == "GET":
        query = """
            SELECT a.bulan, SUM(a.total_berobat) total_berobat,SUM(a.total_vaksin) total_vaksin,SUM(a.total_berobat_vaksin) total_berobat_vaksin
                FROM
                (SELECT 'AGUSTUS' AS bulan, count(dx) total_berobat,0 total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                WHERE dx='BEROBAT' and MONTH(tgl)=8
                GROUP BY dx
                UNION ALL
                SELECT 'AGUSTUS' AS bulan, 0 total_berobat,count(dx) total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='VAKSINASI' and MONTH(tgl)=8
                group by dx
                UNION ALL
            SELECT 'AGUSTUS' AS bulan, 0 total_berobat,0 total_vaksin,count(dx) total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='BEROBAT & VAKSINASI' and MONTH(tgl)=8
                group by dx
                )a
                union all
                SELECT a.bulan, SUM(a.total_berobat) total_berobat,SUM(a.total_vaksin) total_vaksin,SUM(a.total_berobat_vaksin) total_berobat_vaksin
                FROM
                (
                SELECT 'SEPTEMBER' AS bulan, count(dx) total_berobat,0 total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                WHERE dx='BEROBAT' and MONTH(tgl)=9
                GROUP BY dx
                UNION ALL
            SELECT 'SEPTEMBER' AS bulan, 0 total_berobat,count(dx) total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='VAKSINASI' and MONTH(tgl)=9
                group by dx
                UNION ALL
                SELECT 'SEPTEMBER' AS bulan, 0 total_berobat,0 total_vaksin,count(dx) total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='BEROBAT & VAKSINASI' and MONTH(tgl)=9
                group by dx
                )a
                UNION ALL
            SELECT a.bulan, SUM(a.total_berobat) total_berobat,SUM(a.total_vaksin) total_vaksin,SUM(a.total_berobat_vaksin) total_berobat_vaksin
                FROM
                (
                SELECT 'OKTOBER' AS bulan, count(dx) total_berobat,0 total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                WHERE dx='BEROBAT' and MONTH(tgl)=10
                GROUP BY dx
                UNION ALL
            SELECT 'OKTOBER' AS bulan, 0 total_berobat,count(dx) total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='VAKSINASI' and MONTH(tgl)=10
                group by dx
                UNION ALL
                SELECT 'OKTOBER' AS bulan, 0 total_berobat,0 total_vaksin,count(dx) total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='BEROBAT & VAKSINASI' and MONTH(tgl)=10
                group by dx
                )a
                UNION ALL
            SELECT a.bulan, SUM(a.total_berobat) total_berobat,SUM(a.total_vaksin) total_vaksin,SUM(a.total_berobat_vaksin) total_berobat_vaksin
                FROM
                (
                SELECT 'NOVEMBER' AS bulan, count(dx) total_berobat,0 total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                WHERE dx='BEROBAT' and MONTH(tgl)=11
                GROUP BY dx
                UNION ALL
                SELECT 'NOVEMBER' AS bulan, 0 total_berobat,count(dx) total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='VAKSINASI' and MONTH(tgl)=11
                group by dx
                UNION ALL
            SELECT 'NOVEMBER' AS bulan, 0 total_berobat,0 total_vaksin,count(dx) total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='BEROBAT & VAKSINASI' and MONTH(tgl)=11
                group by dx
                )a
                UNION ALL
                SELECT a.bulan, SUM(a.total_berobat) total_berobat,SUM(a.total_vaksin) total_vaksin,SUM(a.total_berobat_vaksin) total_berobat_vaksin
                FROM
                (
                SELECT 'DESEMBER' AS bulan, count(dx) total_berobat,0 total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                WHERE dx='BEROBAT' and MONTH(tgl)=12
                GROUP BY dx
                UNION ALL
            SELECT 'DESEMBER' AS bulan, 0 total_berobat,count(dx) total_vaksin,0 total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='VAKSINASI' and MONTH(tgl)=12
                group by dx
                UNION ALL
                SELECT 'DESEMBER' AS bulan, 0 total_berobat,0 total_vaksin,count(dx) total_berobat_vaksin
                FROM spgdt_pbfree
                where dx='BEROBAT & VAKSINASI' and MONTH(tgl)=12
                group by dx
            )a;
        """

        cursor = connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        obj = []
        for row in rows:
            obj.append(dict(zip(columns, row)))
        return JsonResponse({
            'sukses': 'yes',
            'pesan': 'blah',
            'data': obj,
        })


def getgiat(request):
    if request.method == "GET":
        query = """
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'JANUARI' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=1
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'FEBRUARI' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=2
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'MARET' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=3
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'APRIL' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=4
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'MEI' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=5
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'JUNI' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=6
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'JULI' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=7
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'AGUSTUS' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=8
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'SEPTEMBER' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=9
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'OKBTOBER' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=10
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'NOVEMBER' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=11
                GROUP BY ket)a
                UNION ALL
            SELECT a.bulan, SUM(a.total_keterangan) total_keterangan
                FROM
                (SELECT 'DESEMBER' AS bulan, count(ket) total_keterangan
                FROM spgdt_giat
                WHERE MONTH(tgl)=12
                GROUP BY ket)a
                ;
            """

        cursor = connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        obj = []
        for row in rows:
            obj.append(dict(zip(columns, row)))
        return JsonResponse({
            'sukses': 'yes',
            'pesan': 'blah',
            'data': obj,
        })


def gettelp(request):
    if request.method == "GET":
        query = """
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'JANUARI' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=1
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'FEBRUARI' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=2
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'MARET' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=3
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'APRIL' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=4
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'MEI' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=5
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'JUNI' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=6
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'JULI' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=7
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'AGUSTUS' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=8
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'SEPTEMBER' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=9
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'OKTOBER' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=10
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'NOVEMBER' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=11
                    GROUP BY kategori)a
                    UNION ALL
                SELECT a.startcall, SUM(a.total_kategori) total_kategori
                    FROM
                    (SELECT 'DESEMBER' AS startcall, count(kategori) total_kategori
                    FROM spgdt_telp
                    WHERE MONTH(startcall)=12
                    GROUP BY kategori)a;
                    """

        cursor = connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        obj = []
        for row in rows:
            obj.append(dict(zip(columns, row)))
        return JsonResponse({
            'sukses': 'yes',
            'pesan': 'blah',
            'data': obj,
        })


def dash(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    pbfrees = Pbfree.objects.filter(name__icontains=q)
    return render(request, 'base/dash.html', {'pbfrees': pbfrees})


# menggunakan database local dan file di video di kirimkan ke folder project app
def video(request):
    video = Video.objects.all()
    return render(request, 'spgdt/video.html', {"video": video})


# menggunakan url youtube
def videogiat(request):
    video = Video_giat.objects.all()
    return render(request, 'spgdt/video_url.html', {"video": video})


def tab(request):
    telps = Telp.objects.all()
    context = {'telps': telps}
    return render(request, 'spgdt/table.html', context)

# def spgdt(request):
#     telps = Telp.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(telps, 10)

#     try:
#         telps = paginator.page(page)
#     except PageNotAnInteger:
#         telps = paginator.page(1)
#     except EmptyPage:
#         telps = paginator.page(paginator.num_pages)

#     context = {'telps': telps}
#     return render(request, 'spgdt/main.html', context)
