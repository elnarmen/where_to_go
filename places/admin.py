from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe


from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'get_image_preview']
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, obj):
        width = 150,
        height = 150
        return format_html(
            "{}",
            mark_safe(
                f'<img src="{obj.image.url}" width="{width}" height={height} />'
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass