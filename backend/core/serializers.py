from rest_framework import serializers
from .models import Student, Result, Fee, Note, ReportCard

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    total_score = serializers.ReadOnlyField()
    class Meta:
        model = Result
        fields = '__all__'

class FeeSerializer(serializers.ModelSerializer):
    outstanding = serializers.ReadOnlyField()
    class Meta:
        model = Fee
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = '__all__'