from django.contrib import admin
from .models import Brand, CommonProblem, Customer, TVRepair

# የደንበኛውን ሰንጠረዥ እይታ ማሳመሪያ
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'visit_count', 'star_rating') # እነዚህን በሰንጠረዥ ያሳያል
    search_fields = ('name', 'phone_number') # በስም እና በስልክ መፈለጊያ ሳጥን ይጨምራል

# የቲቪ ጥገና ሰንጠረዥ እይታ ማሳመሪያ
@admin.register(TVRepair)
class TVRepairAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_number', 'get_customer_name', 'get_customer_phone', 'warranty_status', 'status', 'created_at')
    list_filter = ('status', 'warranty_status', 'brand') # በቀኝ በኩል በማጣሪያ (Filter) ለመለየት
    search_fields = ('model_number', 'customer__name', 'customer__phone_number') # መፈለጊያ

    # የደንበኛውን ስም ከሌላ ሰንጠረዥ መሳቢያ
    def get_customer_name(self, obj):
        return obj.customer.name
    get_customer_name.short_description = 'Customer Name'

    # የደንበኛውን ስልክ ከሌላ ሰንጠረዥ መሳቢያ
    def get_customer_phone(self, obj):
        return obj.customer.phone_number
    get_customer_phone.short_description = 'Phone Number'

# ሌሎቹን መመዝገብ
admin.site.register(Brand)
admin.site.register(CommonProblem)