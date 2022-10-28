from dataclasses import field
from rest_framework import serializers
from spgdt.models import Pbfree, Telp, Giat


class PbfreeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pbfree
        fields = (
            'id',
            'nama',
            'jk',
            'td',
            'usia',
            'dx',
            'alamat',
            'nohp',
            'tgl',
        )
        datatables_always_serialize = ('id',)


class SpgdtSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Telp
        fields = (
            'id',
            'nama',
            'notelp',
            'lokasi',
            'kategori',
            'subkategori',
            'detailkategori',
            'keterangan',
            'status',
            'startcall',
        )
        datatables_always_serialize = ('id',)


class GiatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Giat
        fields = (
            'id',
            'ket',
            'giat',
            'lokasi',
            'tgl',
        )
        datatables_always_serialize = ('id',)
