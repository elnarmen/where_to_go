from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from .models import Place, Image


class ImageStackedInline(SortableStackedInline):
    model = Image
    fields = ['image', 'get_image_preview',]
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, obj):
        return format_html('<img src={} height="200"', obj.image.url)


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageStackedInline,
    ]


admin.site.register(Image)