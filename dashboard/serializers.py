import pdfkit
from rest_framework import serializers

from utils.reume_make import resumemaker
from .models import Resume
import os

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


def get_pdf_path(filename):
    return os.path.join('media/pdf_files/', filename)


class ResumeCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, max_length=255)
    last_name = serializers.CharField(write_only=True, max_length=255)
    birth_year = serializers.IntegerField(write_only=True)
    address = serializers.CharField(write_only=True)

    class Meta:
        model = Resume
        fields = ['id', 'user', 'name', 'skills', 'pdf_file', 'first_name', 'last_name', 'birth_year', 'address']

    def create(self, validated_data):

        pdf_file_name = resumemaker(validated_data)
        validated_data["pdf_file"] = pdf_file_name

        return super(ResumeCreateSerializer, self).create(validated_data)


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'user', 'name', 'pdf_file']
