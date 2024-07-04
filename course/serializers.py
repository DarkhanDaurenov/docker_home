from rest_framework.serializers import ModelSerializer, SerializerMethodField
from course.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='уроки')
    lesson_count = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, obj):
        return obj.уроки.count()



