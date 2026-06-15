from rest_framework import serializers

from library.models.users import User

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", 'username', 'email', 'role', 'age']

    def to_representation(self, instance: User):
        data = super().to_representation(instance)
        if self.context.get('include_related'):
            memberships = instance.membership_records.all()
            top_reviews = sorted(instance.reviews.all(), key=lambda review: review.rating or 0, reverse=True)
            new_data = {
                "libraries": [
                    {
                        "id": member.id,
                        "name": member.library.name
                    } for member in memberships
                ],
                "posts_count": instance.posts.count(),
                "reviews_count": instance.reviews.count(),
                "top_reviews": [
                    {
                        "id": tr.id,
                        "content": tr.content,
                        "rating": tr.rating
                    } for tr in top_reviews
                ]
            }
            data.update(new_data)
        return data
