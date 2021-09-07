from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from .models import Post, Category
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(request, "The wrong file has been uploaded")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")  # o/p ['categories\r', 'coding\r', 'food']

            for x in csv_data:
                fields = x.split(",")
                created = Category.objects.update_or_create(name=fields[0])
            url = reverse("admin:index")
            return HttpResponseRedirect(url)
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
