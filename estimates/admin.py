from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from estimates.models import Estimates

# Register your models here.

class EstimateAdmin(admin.ModelAdmin):
    readonly_fields = ('estimate_number',)

    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if obj:
            return self.readonly_fields + ('other_fields',) #add other fields to make it readonly
        return self.readonly_fields
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.estimate_number:
            obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Estimates, EstimateAdmin)