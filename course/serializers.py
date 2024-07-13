from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from course.models import Course, Lesson, CourseSubscription
from course.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    video_url = serializers.URLField(validators=[UrlValidator(field='video_url')])

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'photo', 'video_url', 'course', 'owner']


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='уроки')
    lesson_count = SerializerMethodField(read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, obj):
        return obj.уроки.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return CourseSubscription.objects.filter(user=user, course=obj).exists()


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = ['course']



