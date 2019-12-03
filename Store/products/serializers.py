from rest_framework import serializers
from . models import Products

class ProductsSerializer(serializers.ModelSerializer):
    # #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, unique=True, blank=True, null=True)
    # productid = serializers.IntegerField(max_length=10, unique=True, blank=True)
    # productname = serializers.CharField(max_length=255, blank=True)
    # vendor = serializers.CharField(max_length=100, blank=True)
    # mrp = serializers.IntegerField(max_length=10, blank=True)
    # batchdate = serializers.DateTimeField(auto_now_add=True)
    # batchnumber = serializers.IntegerField(max_length=1000, blank=True)
    # quantity = serializers.IntegerField(max_length=1000, blank=True)
    # status_approved = serializers.NullBooleanField(blank=True, null=True, default=False)

    class Meta:
        model = Products
        fields = (
            'user_id', 'productid', 'productname', 'vendor', 'mrp', 'batchdate', 'batchnumber', 'quantity', 'status_approved'
        )
        #read_only_fields = 'batchdate')

    def create(self, validated_data):
        return Products.objects.create_Products(**validated_data)
