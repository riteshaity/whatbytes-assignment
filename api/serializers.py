from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Mapping, Doctor, Patient

User = get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']

    def validate(self, data):
        if not self.instance and not ('password' in data and 'confirm_password' in data):
            return serializers.ValidationError('Password needed for registration.')

        if 'password' in data and 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('Passwords do not match.')
            if len(data['password']) < 6:
                raise serializers.ValidationError('Passwords is too small, >= 6 chars needed.')
        
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        cp = validated_data.pop('confirm_password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user 


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']

    def validate(self, data):
        if self.instance and 'password' in data and 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('Passwords do not match.')
            if len(data['password']) < 6:
                raise serializers.ValidationError('Passwords is too small, >= 6 chars needed.')
            
        return data
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
            
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MappingSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Mapping
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'assigned_at':{
                'read_only':True,
            },
        }

    def validate(self, data):
        dctr = data.get('doctor')
        ptnt = data.get('patient') 

        doctor_instance = Doctor.objects.filter(pk=dctr.pk)
        patient_instance = Patient.objects.filter(pk=ptnt.pk)

        if not doctor_instance.exists(): 
            raise serializers.ValidationError(
                'Doctor ID does not exists.'
            )
        if not patient_instance.exists():
            raise serializers.ValidationError(
                'Patient ID does not exists.'
            )
        return data 
    
    def create(self, validated_data):
        doctor_in = validated_data.get('doctor')
        patient_in = validated_data.get('patient')

        mapping = Mapping.objects.create(doctor=doctor_in, patient=patient_in)
        
        return mapping
