from rest_framework import serializers
from snippet.models import Tags, Snippets


class TagsSerializer(serializers.ModelSerializer):
    tag_details = serializers.HyperlinkedIdentityField(view_name='tag-detail')
    class Meta:
        model = Tags
        fields = ['id','title', 'tag_details']


class SnippetsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=False,required=False)
    author = serializers.SlugRelatedField(
            read_only=True,
            slug_field='username'
        )
    snippet_details = serializers.HyperlinkedIdentityField(view_name='snippet-detail')
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
    class Meta:
        model = Snippets
        fields = ['id', 'title',"message",'tags','author',"created",'snippet_details']
        read_only_fields = ['author']
    def validate(self, attrs):
        #only logged user can update own data only
        if self.instance:
            if  self.context['request'].user.pk != self.instance.author.pk:
                raise serializers.ValidationError({"author": "the user not access for update"})
        else:
            attrs['author'] = self.context['request'].user
        
        return attrs
    def get_validated_data_tag(self,validated_data={}):
        tags_datas ={}
        tags_delete_all=False
        if validated_data.get('tags'):
            tags_datas = validated_data.pop('tags')
        elif "tags" in validated_data: 
            validated_data.pop('tags')
            #if tags exist and it become empty we should delete corresponding tags
            tags_delete_all=True
        return tags_datas,tags_delete_all
    def create(self, validated_data):
        tags_datas,_ = self.get_validated_data_tag(validated_data)
        instance = super(SnippetsSerializer, self).create(validated_data)
        if tags_datas:
            for tags_data in tags_datas:
                tag,created = self.get_or_create_tags(tags_data)
                instance.tags.add(tag)
        return instance
    def update(self, instance, validated_data):
        tags_datas,tags_delete_all = self.get_validated_data_tag(validated_data=validated_data)
        instance = super(SnippetsSerializer, self).update(instance, validated_data)
        if tags_datas:
            for tags_data in tags_datas:
                tag,created = self.get_or_create_tags(tags_data)
                instance.tags.add(tag)
        elif tags_delete_all :
            instance.tags.clear() 
            pass
        return instance
    def get_or_create_tags(self,tags_data={}):
        tag=None
        if tags_data:
            tag,created = Tags.objects.filter(title__iexact=tags_data['title']).get_or_create(
                **tags_data
            )
        return tag,created

    