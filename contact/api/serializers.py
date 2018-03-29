from rest_framework import serializers
from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'contact_number')

    # validation for duplicate name
    def validate_name(self, value):
        name_matched = Contact.objects.filter(name__iexact=value)

        if self.instance:
            name_matched = name_matched.exclude(pk=self.instance.pk)  # exclude own name from the list of matched names

        if name_matched.exists():
            raise serializers.ValidationError("Name already exists")

        return value

    # validation for duplicate number
    def validate_contact_number(self, value):
        number_matched = Contact.objects.filter(contact_number__iexact=value)

        if self.instance:
            number_matched = number_matched.exclude(pk=self.instance.pk)

        if number_matched.exists():
            raise serializers.ValidationError("Number already exists")

        return value





