from rest_framework import serializers

from .models import Group, Element


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="group-detail")

    class Meta:
        model = Group
        fields = (
            'url',
            'name',
            'description',
            'parent',
            'icon',
            'child_group_count',
            'child_element_count'
        )


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="element-detail")
    verified = serializers.NullBooleanField(read_only=True)

    class Meta:
        model = Element
        fields = (
            'url',
            'parent',
            'name',
            'description',
            'icon',
            'creation_name',
            'verified'
        )


class GroupDetailSerializer(serializers.HyperlinkedModelSerializer):
    child_groups = GroupSerializer(many=True, read_only=True)
    elements = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="group-detail")

    class Meta:
        model = Group
        fields = (
            'url',
            'name',
            'description',
            'parent',
            'icon',
            'child_group_count',
            'child_element_count',
            'child_groups',
            'elements'
        )

    def get_elements(self, obj):
        elements = Element.objects.filter(parent=obj, verified=True)
        return ElementSerializer(elements, many=True, read_only=True).data

