from rest_framework import serializers

from comment.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    # def get_user(self, obj):
    #     return {
    #         "name":obj.user.first_name,
    #     }


    class Meta:
        model = Comment
        fields = [
             "post","name", "email", "subject", "message","approved"]


class CommentUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
           "post","name", "email", "subject", "message","approved"]