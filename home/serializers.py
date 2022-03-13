from rest_framework import serializers


class contactForm(serializers.Serializer):
    names = serializers.CharField(max_length=100)
    emailAddress = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=100)

class call(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)