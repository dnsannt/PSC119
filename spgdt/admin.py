from importlib import resources
from django.contrib import admin
from .models import Telp, Pbfree, Giat, Video, Video_giat
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from embed_video.admin import AdminVideoMixin  # import library


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):  # view admin video in django
    pass


admin.site.register(Video_giat, AdminVideo)
admin.site.register(Video)


@admin.register(Pbfree)
class Pbfree_Resources(ImportExportModelAdmin):
    class Meta:
        model = Pbfree

    def __str__(self):
        return self.nama


@admin.register(Telp)
class Telp_Resources(ImportExportModelAdmin):
    class Meta:
        model = Telp

    def __str__(self):
        return self.nama


@admin.register(Giat)
class Giat_Resources(ImportExportModelAdmin):
    class Meta:
        model = Giat

    def __str__(self):
        return self.ket
