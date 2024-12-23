# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AzApiSettlement(models.Model):
    id = models.UUIDField(primary_key=True)
    asin = models.CharField(db_column='Asin', blank=True, null=True)  # Field name made lowercase.
    isamazonfulfilled = models.BooleanField(db_column='IsAmazonFulfilled', blank=True, null=True)  # Field name made lowercase.
    input_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    totalfeesestimate = models.DecimalField(db_column='TotalFeesEstimate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    referralfee = models.DecimalField(db_column='ReferralFee', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    referralfee_tax = models.DecimalField(db_column='ReferralFee_tax', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    variableclosingfee = models.DecimalField(db_column='VariableClosingFee', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    variableclosingfee_tax = models.DecimalField(db_column='VariableClosingFee_tax', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    closing_fee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    closing_fee_tax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fullfillment_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fullfillment_cost_tax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fbaweighthandling = models.DecimalField(db_column='FBAWeightHandling', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fbaweighthandling_tax = models.DecimalField(db_column='FBAWeightHandling_tax', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fbapickandpack = models.DecimalField(db_column='FBAPickAndPack', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fbapickandpack_tax = models.DecimalField(db_column='FBAPickAndPack_tax', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    final_settlement = models.DecimalField(db_column='final settlement', max_digits=20, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_tax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    last_updated_date = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'az_api_settlement'


class CompetitorScrappingData(models.Model):
    id = models.UUIDField(primary_key=True)
    portal = models.CharField(blank=True, null=True)
    asin_fsn = models.CharField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    product_ratings = models.CharField(blank=True, null=True)
    rating_count = models.CharField(blank=True, null=True)
    rating_1 = models.CharField(blank=True, null=True)
    reviews_1 = models.CharField(blank=True, null=True)
    rating_2 = models.CharField(blank=True, null=True)
    reviews_2 = models.CharField(blank=True, null=True)
    rating_3 = models.CharField(blank=True, null=True)
    reviews_3 = models.CharField(blank=True, null=True)
    rating_4 = models.CharField(blank=True, null=True)
    reviews_4 = models.CharField(blank=True, null=True)
    rating_5 = models.CharField(blank=True, null=True)
    reviews_5 = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competitor_scrapping_data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FkMappingSheet(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    warehouse_name_fk = models.TextField(blank=True, null=True)
    state_fk = models.TextField(blank=True, null=True)
    zone_fk = models.TextField(blank=True, null=True)
    state_az = models.TextField(blank=True, null=True)
    zone_az = models.TextField(blank=True, null=True)
    wh_id = models.TextField(blank=True, null=True)
    field_st = models.TextField(db_column='__st', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    zoone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fk_mapping_sheet'


class GetAfnInventoryData(models.Model):
    id = models.UUIDField(primary_key=True)
    seller_sku = models.CharField(blank=True, null=True)
    fulfillment_channel_sku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    condition_type = models.CharField(blank=True, null=True)
    warehouse_condition_code = models.CharField(blank=True, null=True)
    quantity_available = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_afn_inventory_data'


class GetAmazonFulfilledShipmentsDataGeneral(models.Model):
    id = models.UUIDField(primary_key=True)
    amazon_order_id = models.CharField(blank=True, null=True)
    merchant_order_id = models.CharField(blank=True, null=True)
    shipment_id = models.CharField(blank=True, null=True)
    shipment_item_id = models.CharField(blank=True, null=True)
    amazon_order_item_id = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    merchant_order_item_id = models.CharField(blank=True, null=True)
    purchase_date = models.CharField(blank=True, null=True)
    payments_date = models.CharField(blank=True, null=True)
    shipment_date = models.CharField(blank=True, null=True)
    reporting_date = models.CharField(blank=True, null=True)
    buyer_email = models.CharField(blank=True, null=True)
    buyer_name = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    buyer_phone_number = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    quantity_shipped = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    item_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_tax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    shipping_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    shipping_tax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    gift_wrap_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    gift_wrap_tax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_service_level = models.CharField(blank=True, null=True)
    recipient_name = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_address_1 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_address_2 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_address_3 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_city = models.CharField(blank=True, null=True)
    ship_state = models.CharField(blank=True, null=True)
    ship_postal_code = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_country = models.CharField(blank=True, null=True)
    ship_phone_number = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bill_address_1 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bill_address_2 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bill_address_3 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bill_city = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bill_state = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bill_postal_code = models.CharField(blank=True, null=True)
    bill_country = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_promotion_discount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_promotion_discount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    carrier = models.CharField(blank=True, null=True)
    tracking_number = models.CharField(blank=True, null=True)
    estimated_arrival_date = models.CharField(blank=True, null=True)
    fulfillment_center_id = models.CharField(blank=True, null=True)
    fulfillment_channel = models.CharField(blank=True, null=True)
    sales_channel = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_amazon_fulfilled_shipments_data_general'


class GetFbaEstimatedFbaFeesTxtData(models.Model):
    id = models.UUIDField(primary_key=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    amazon_store = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    product_group = models.CharField(blank=True, null=True)
    brand = models.CharField(blank=True, null=True)
    fulfilled_by = models.CharField(blank=True, null=True)
    your_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    longest_side = models.CharField(blank=True, null=True)
    median_side = models.CharField(blank=True, null=True)
    shortest_side = models.CharField(blank=True, null=True)
    length_and_girth = models.CharField(blank=True, null=True)
    unit_of_dimension = models.CharField(blank=True, null=True)
    item_package_weight = models.CharField(blank=True, null=True)
    unit_of_weight = models.CharField(blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    estimated_fee_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_referral_fee_per_unit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_fixed_closing_fee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_pick_pack_fee_per_unit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_weight_handling_fee_per_unit = models.CharField(blank=True, null=True)
    estimated_delivery_services_fee_per_unit = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_estimated_fba_fees_txt_data'


class GetFbaFulfillmentCustomerReturnsData(models.Model):
    id = models.UUIDField(primary_key=True)
    return_date = models.CharField(blank=True, null=True)
    order_id = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fulfillment_center_id = models.CharField(blank=True, null=True)
    detailed_disposition = models.CharField(blank=True, null=True)
    reason = models.CharField(blank=True, null=True)
    license_plate_number = models.CharField(blank=True, null=True)
    customer_comments = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_fulfillment_customer_returns_data'


class GetFbaFulfillmentCustomerShipmentSalesData(models.Model):
    id = models.UUIDField(primary_key=True)
    shipment_date = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    fulfillment_center_id = models.CharField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    amazon_order_id = models.CharField(blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    item_price_per_unit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    shipping_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    gift_wrap_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ship_city = models.CharField(blank=True, null=True)
    ship_state = models.CharField(blank=True, null=True)
    ship_postal_code = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_fulfillment_customer_shipment_sales_data'


class GetFbaFulfillmentRemovalOrderDetailData(models.Model):
    id = models.UUIDField(primary_key=True)
    request_date = models.CharField(blank=True, null=True)
    order_id = models.CharField(blank=True, null=True)
    order_source = models.CharField(blank=True, null=True)
    order_type = models.CharField(blank=True, null=True)
    service_speed = models.CharField(blank=True, null=True)
    order_status = models.CharField(blank=True, null=True)
    last_updated_date = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    disposition = models.CharField(blank=True, null=True)
    requested_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    cancelled_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    disposed_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    shipped_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    in_process_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    removal_fee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_fulfillment_removal_order_detail_data'


class GetFbaFulfillmentRemovalShipmentDetailData(models.Model):
    id = models.UUIDField(primary_key=True)
    request_date = models.CharField(blank=True, null=True)
    order_id = models.CharField(blank=True, null=True)
    shipment_date = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    disposition = models.CharField(blank=True, null=True)
    shipped_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    carrier = models.CharField(blank=True, null=True)
    tracking_number = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    shipment_status = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    removal_order_type = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_fulfillment_removal_shipment_detail_data'


class GetFbaInventoryPlanningData(models.Model):
    id = models.UUIDField(primary_key=True)
    snapshot_date = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    product_name = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    condition = models.CharField(blank=True, null=True)
    available = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pending_removal_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_0_to_90_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_91_to_180_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_181_to_270_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_271_to_365_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_365_plus_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    qty_to_be_charged_ltsf_5_mo = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    projected_ltsf_5_mo = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    qty_to_be_charged_ltsf_12_mo = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_ltsf_next_charge = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    units_shipped_t7 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    units_shipped_t30 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    units_shipped_t60 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    units_shipped_t90 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    alert = models.CharField(blank=True, null=True)
    your_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    lowest_price_new_plus_shipping = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    lowest_price_used = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    recommended_action = models.CharField(blank=True, null=True)
    healthy_inventory_level = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    recommended_sales_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    recommended_sale_duration_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    recommended_removal_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_cost_savings_of_recommended_actions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sell_through = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    volume_unit_measurement = models.CharField(blank=True, null=True)
    storage_type = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    storage_volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    marketplace = models.CharField(blank=True, null=True)
    product_group = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_rank = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    days_of_supply = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_excess_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    weeks_of_cover_t30 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    weeks_of_cover_t90 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    featuredoffer_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_shipped_last_7_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_shipped_last_30_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_shipped_last_60_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales_shipped_last_90_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_0_to_30_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_31_to_60_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_61_to_90_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_91_to_150_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_151_to_180_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_181_to_330_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inv_age_331_to_365_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_storage_cost_next_month = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inbound_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inbound_working = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inbound_shipped = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inbound_received = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    reserved_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unfulfillable_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_inventory_planning_data'


class GetFbaMyiUnsuppressedInventoryData(models.Model):
    id = models.UUIDField(primary_key=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    condition = models.CharField(blank=True, null=True)
    your_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    mfn_listing_exists = models.CharField(blank=True, null=True)
    mfn_fulfillable_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_listing_exists = models.CharField(blank=True, null=True)
    afn_warehouse_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_fulfillable_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_unsellable_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_reserved_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_total_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    per_unit_volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_inbound_working_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_inbound_shipped_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_inbound_receiving_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_researching_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_reserved_future_supply = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    afn_future_supply_buyable = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_myi_unsuppressed_inventory_data'


class GetFbaRecommendedRemovalData(models.Model):
    id = models.UUIDField(primary_key=True)
    snapshot_date = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    condition = models.CharField(blank=True, null=True)
    sellable_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sellable_271_365_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sellable_365_days = models.DecimalField(db_column='sellable_365+_days', max_digits=20, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sellable_removal_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unsellable_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unsellable_0_7_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unsellable_8_60_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unsellable_61_90_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sellable_121_150_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sellable_151_270_days = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_recommended_removal_data'


class GetFbaReimbursementsData(models.Model):
    id = models.UUIDField(primary_key=True)
    approval_date = models.CharField(blank=True, null=True)
    reimbursement_id = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    case_id = models.CharField(blank=True, null=True)
    amazon_order_id = models.CharField(blank=True, null=True)
    reason = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    condition = models.CharField(blank=True, null=True)
    currency_unit = models.CharField(blank=True, null=True)
    amount_per_unit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity_reimbursed_cash = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity_reimbursed_inventory = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity_reimbursed_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    original_reimbursement_id = models.CharField(blank=True, null=True)
    original_reimbursement_type = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_reimbursements_data'


class GetFbaStorageFeeChargesData(models.Model):
    id = models.UUIDField(primary_key=True)
    asin = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    fulfillment_center = models.CharField(blank=True, null=True)
    country_code = models.CharField(blank=True, null=True)
    longest_side = models.CharField(blank=True, null=True)
    median_side = models.CharField(blank=True, null=True)
    shortest_side = models.CharField(blank=True, null=True)
    measurement_units = models.CharField(blank=True, null=True)
    weight = models.CharField(blank=True, null=True)
    weight_units = models.CharField(blank=True, null=True)
    item_volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    volume_units = models.CharField(blank=True, null=True)
    average_quantity_on_hand = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    average_quantity_pending_removal = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estimated_total_item_volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    month_of_charge = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    storage_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    estimated_monthly_storage_fee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    average_quantity_customer_orders = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_fba_storage_fee_charges_data'


class GetFlatFileAllOrdersDataByLastUpdateGeneral(models.Model):
    id = models.UUIDField(primary_key=True)  # The composite primary key (id, updated_date) found, that is not supported. The first column is selected.
    amazon_order_id = models.CharField(blank=True, null=True)
    merchant_order_id = models.CharField(blank=True, null=True)
    purchase_date = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)
    order_status = models.CharField(blank=True, null=True)
    fulfillment_channel = models.CharField(blank=True, null=True)
    sales_channel = models.CharField(blank=True, null=True)
    order_channel = models.CharField(blank=True, null=True)
    ship_service_level = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    sku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    item_status = models.CharField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    item_price = models.FloatField(blank=True, null=True)
    item_tax = models.FloatField(blank=True, null=True)
    shipping_price = models.FloatField(blank=True, null=True)
    shipping_tax = models.FloatField(blank=True, null=True)
    gift_wrap_price = models.FloatField(blank=True, null=True)
    gift_wrap_tax = models.FloatField(blank=True, null=True)
    item_promotion_discount = models.FloatField(blank=True, null=True)
    ship_promotion_discount = models.FloatField(blank=True, null=True)
    ship_city = models.CharField(blank=True, null=True)
    ship_state = models.CharField(blank=True, null=True)
    ship_postal_code = models.CharField(blank=True, null=True)
    ship_country = models.CharField(blank=True, null=True)
    promotion_ids = models.CharField(blank=True, null=True)
    is_business_order = models.BooleanField(blank=True, null=True)
    purchase_order_number = models.CharField(blank=True, null=True)
    price_designation = models.CharField(blank=True, null=True)
    fulfilled_by = models.CharField(blank=True, null=True)
    is_iba = models.BooleanField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'get_flat_file_all_orders_data_by_last_update_general'
        unique_together = (('id', 'updated_date'),)


# class GetFlatFileAllOrdersDataByOrderDateGeneral(models.Model):
#     id = models.UUIDField(primary_key=True)  # The composite primary key (id, updated_date) found, that is not supported. The first column is selected.
#     amazon_order_id = models.CharField(blank=True, null=True)
#     merchant_order_id = models.CharField(blank=True, null=True)
#     purchase_date = models.DateTimeField(blank=True, null=True)
#     last_updated_date = models.DateTimeField(blank=True, null=True)
#     order_status = models.CharField(blank=True, null=True)
#     fulfillment_channel = models.CharField(blank=True, null=True)
#     sales_channel = models.CharField(blank=True, null=True)
#     order_channel = models.CharField(blank=True, null=True)
#     ship_service_level = models.CharField(blank=True, null=True)
#     product_name = models.CharField(blank=True, null=True)
#     sku = models.CharField(blank=True, null=True)
#     asin = models.CharField(blank=True, null=True)
#     item_status = models.CharField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     currency = models.CharField(blank=True, null=True)
#     item_price = models.FloatField(blank=True, null=True)
#     item_tax = models.FloatField(blank=True, null=True)
#     shipping_price = models.FloatField(blank=True, null=True)
#     shipping_tax = models.FloatField(blank=True, null=True)
#     gift_wrap_price = models.FloatField(blank=True, null=True)
#     gift_wrap_tax = models.FloatField(blank=True, null=True)
#     item_promotion_discount = models.FloatField(blank=True, null=True)
#     ship_promotion_discount = models.FloatField(blank=True, null=True)
#     ship_city = models.CharField(blank=True, null=True)
#     ship_state = models.CharField(blank=True, null=True)
#     ship_postal_code = models.CharField(blank=True, null=True)
#     ship_country = models.CharField(blank=True, null=True)
#     promotion_ids = models.CharField(blank=True, null=True)
#     is_business_order = models.BooleanField(blank=True, null=True)
#     purchase_order_number = models.CharField(blank=True, null=True)
#     price_designation = models.CharField(blank=True, null=True)
#     fulfilled_by = models.CharField(blank=True, null=True)
#     is_iba = models.BooleanField(blank=True, null=True)
#     account_name = models.CharField(blank=True, null=True)
#     updated_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'get_flat_file_all_orders_data_by_order_date_general'
#         unique_together = (('id', 'updated_date'),)


class GetFlatFileReturnsDataByReturnDate(models.Model):
    id = models.UUIDField(primary_key=True)  # The composite primary key (id, updated_date) found, that is not supported. The first column is selected.
    order_id = models.CharField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    return_request_date = models.DateTimeField(blank=True, null=True)
    return_request_status = models.CharField(blank=True, null=True)
    amazon_rma_id = models.CharField(blank=True, null=True)
    merchant_rma_id = models.CharField(blank=True, null=True)
    label_type = models.CharField(blank=True, null=True)
    label_cost = models.FloatField(blank=True, null=True)
    currency_code = models.CharField(blank=True, null=True)
    return_carrier = models.CharField(blank=True, null=True)
    tracking_id = models.CharField(blank=True, null=True)
    label_to_be_paid_by = models.CharField(blank=True, null=True)
    a_to_z_claim = models.CharField(blank=True, null=True)
    is_prime = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    merchant_sku = models.CharField(blank=True, null=True)
    item_name = models.CharField(blank=True, null=True)
    return_quantity = models.IntegerField(blank=True, null=True)
    return_reason = models.CharField(blank=True, null=True)
    in_policy = models.CharField(blank=True, null=True)
    return_type = models.CharField(blank=True, null=True)
    resolution = models.CharField(blank=True, null=True)
    invoice_number = models.CharField(blank=True, null=True)
    return_delivery_date = models.DateTimeField(blank=True, null=True)
    order_amount = models.FloatField(blank=True, null=True)
    order_quantity = models.FloatField(blank=True, null=True)
    safet_action_reason = models.CharField(blank=True, null=True)
    safet_claim_id = models.CharField(blank=True, null=True)
    safet_claim_state = models.CharField(blank=True, null=True)
    safet_claim_creation_time = models.CharField(blank=True, null=True)
    safet_claim_reimbursement_amount = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'get_flat_file_returns_data_by_return_date'
        unique_together = (('id', 'updated_date'),)


class GetLedgerDetailViewData(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    msku = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    event_type = models.CharField(blank=True, null=True)
    reference_id = models.CharField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fulfillment_center = models.CharField(blank=True, null=True)
    disposition = models.CharField(blank=True, null=True)
    reason = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    reconciled_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unreconciled_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    date_and_time = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_ledger_detail_view_data'


class GetLedgerSummaryViewData(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    msku = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    disposition = models.CharField(blank=True, null=True)
    starting_warehouse_balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    in_transit_between_warehouses = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    receipts = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    customer_shipments = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    customer_returns = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    vendor_returns = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    warehouse_transfer_in_out = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    found = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    lost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    damaged = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    disposed = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    other_events = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ending_warehouse_balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unknown_events = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    location = models.CharField(blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_ledger_summary_view_data'


class GetMerchantListingsAllData(models.Model):
    id = models.UUIDField(primary_key=True)
    item_name = models.CharField(blank=True, null=True)
    item_description = models.CharField(blank=True, null=True)
    listing_id = models.CharField(blank=True, null=True)
    seller_sku = models.CharField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    open_date = models.CharField(blank=True, null=True)
    image_url = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_is_marketplace = models.CharField(blank=True, null=True)
    product_id_type = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    zshop_shipping_fee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_note = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_condition = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    zshop_category1 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    zshop_browse_path = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    zshop_storefront_feature = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    asin1 = models.CharField(blank=True, null=True)
    asin2 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    asin3 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    will_ship_internationally = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    expedited_shipping = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    zshop_boldface = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    product_id = models.CharField(blank=True, null=True)
    bid_for_featured_placement = models.CharField(blank=True, null=True)
    add_delete = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pending_quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fulfillment_channel = models.CharField(blank=True, null=True)
    optional_payment_type_exclusion = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    merchant_shipping_group = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    maximum_retail_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_merchant_listings_all_data'


class GetReservedInventoryData(models.Model):
    id = models.UUIDField(primary_key=True)
    sku = models.CharField(blank=True, null=True)
    fnsku = models.CharField(blank=True, null=True)
    asin = models.CharField(blank=True, null=True)
    product_name = models.CharField(blank=True, null=True)
    reserved_qty = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    reserved_customerorders = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    reserved_fc_transfers = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    reserved_fc_processing = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'get_reserved_inventory_data'


class SbAdsReport(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsalespercentage = models.DecimalField(db_column='newToBrandSalesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costtype = models.CharField(db_column='costType', blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.DecimalField(db_column='viewClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasespromoted = models.DecimalField(db_column='purchasesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewrate = models.DecimalField(db_column='newToBrandDetailPageViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasespercentage = models.DecimalField(db_column='newToBrandPurchasesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salespromoted = models.DecimalField(db_column='salesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adid = models.DecimalField(db_column='adId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesrate = models.DecimalField(db_column='newToBrandPurchasesRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviews = models.DecimalField(db_column='video5SecondViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandecpdetailpageview = models.DecimalField(db_column='newToBrandECPDetailPageView', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobranddetailpageviewsclicks = models.DecimalField(db_column='newToBrandDetailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewableimpressions = models.DecimalField(db_column='viewableImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.DecimalField(db_column='eCPAddToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviews = models.DecimalField(db_column='newToBrandDetailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviewrate = models.DecimalField(db_column='video5SecondViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldpercentage = models.DecimalField(db_column='newToBrandUnitsSoldPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_ads_report'


class SbPurchasedProduct(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandunitssold14d = models.DecimalField(db_column='newToBrandUnitsSold14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignpricetypecode = models.CharField(db_column='campaignPriceTypeCode', blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldpercentage14d = models.DecimalField(db_column='newToBrandUnitsSoldPercentage14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases14d = models.DecimalField(db_column='newToBrandPurchases14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    orders14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobrandsales14d = models.DecimalField(db_column='newToBrandSales14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ordersclicks14d = models.DecimalField(db_column='ordersClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', blank=True, null=True)  # Field name made lowercase.
    productcategory = models.CharField(db_column='productCategory', blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasespercentage14d = models.DecimalField(db_column='newToBrandPurchasesPercentage14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    unitssold14d = models.DecimalField(db_column='unitsSold14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks14d = models.DecimalField(db_column='salesClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsalespercentage14d = models.DecimalField(db_column='newToBrandSalesPercentage14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributiontype = models.CharField(db_column='attributionType', blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    purchasedasin = models.CharField(db_column='purchasedAsin', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_purchased_product'


class SbTraffic(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    invalidclickthroughs = models.DecimalField(db_column='invalidClickThroughs', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    invalidimpressions = models.DecimalField(db_column='invalidImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grossimpressions = models.DecimalField(db_column='grossImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    invalidclickthroughrate = models.DecimalField(db_column='invalidClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    grossclickthroughs = models.DecimalField(db_column='grossClickThroughs', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    invalidimpressionrate = models.DecimalField(db_column='invalidImpressionRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_traffic'


class SdAdvertisedProduct(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promotedsku = models.CharField(db_column='promotedSku', blank=True, null=True)  # Field name made lowercase.
    addtocartviews = models.DecimalField(db_column='addToCartViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobranddetailpageviewclicks = models.DecimalField(db_column='newToBrandDetailPageViewClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.CharField(db_column='viewClickThroughRate', blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewrate = models.DecimalField(db_column='newToBrandDetailPageViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewviews = models.DecimalField(db_column='newToBrandDetailPageViewViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    leadformopens = models.DecimalField(db_column='leadFormOpens', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adid = models.DecimalField(db_column='adId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    leads = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressionsviews = models.DecimalField(db_column='impressionsViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandecpdetailpageview = models.CharField(db_column='newToBrandECPDetailPageView', blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cumulativereach = models.DecimalField(db_column='cumulativeReach', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchrate = models.DecimalField(db_column='brandedSearchRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressionsfrequencyaverage = models.DecimalField(db_column='impressionsFrequencyAverage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    linkouts = models.DecimalField(db_column='linkOuts', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesviews = models.DecimalField(db_column='brandedSearchesViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promotedasin = models.CharField(db_column='promotedAsin', blank=True, null=True)  # Field name made lowercase.
    bidoptimization = models.CharField(db_column='bidOptimization', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    salespromotedclicks = models.DecimalField(db_column='salesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpbrandsearch = models.CharField(db_column='eCPBrandSearch', blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasespromotedclicks = models.DecimalField(db_column='purchasesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.CharField(db_column='eCPAddToCart', blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviews = models.DecimalField(db_column='newToBrandDetailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sd_advertised_product'


class SdTraffic(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    invalidclickthroughs = models.DecimalField(db_column='invalidClickThroughs', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    invalidimpressions = models.DecimalField(db_column='invalidImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grossimpressions = models.DecimalField(db_column='grossImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    invalidclickthroughrate = models.DecimalField(db_column='invalidClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    grossclickthroughs = models.DecimalField(db_column='grossClickThroughs', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    invalidimpressionrate = models.DecimalField(db_column='invalidImpressionRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sd_traffic'


class SpAdvertisedProduct(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    attributedsalessamesku1d = models.DecimalField(db_column='attributedSalesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    roasclicks14d = models.DecimalField(db_column='roasClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks1d = models.DecimalField(db_column='unitsSoldClicks1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku14d = models.DecimalField(db_column='attributedSalesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    attributedsalessamesku30d = models.DecimalField(db_column='attributedSalesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesroyalties14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRoyalties14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku1d = models.DecimalField(db_column='unitsSoldSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    advertisedsku = models.CharField(db_column='advertisedSku', blank=True, null=True)  # Field name made lowercase.
    salesothersku7d = models.DecimalField(db_column='salesOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku7d = models.DecimalField(db_column='purchasesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku30d = models.DecimalField(db_column='unitsSoldSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    costperclick = models.DecimalField(db_column='costPerClick', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clickthroughrate = models.DecimalField(db_column='clickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesread14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRead14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    acosclicks14d = models.DecimalField(db_column='acosClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks30d = models.DecimalField(db_column='unitsSoldClicks30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    portfolioid = models.DecimalField(db_column='portfolioId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adid = models.DecimalField(db_column='adId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    roasclicks7d = models.DecimalField(db_column='roasClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku14d = models.DecimalField(db_column='unitsSoldSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks7d = models.DecimalField(db_column='unitsSoldClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku7d = models.DecimalField(db_column='attributedSalesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku14d = models.DecimalField(db_column='purchasesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldothersku7d = models.DecimalField(db_column='unitsSoldOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    spend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku1d = models.DecimalField(db_column='purchasesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    advertisedasin = models.CharField(db_column='advertisedAsin', blank=True, null=True)  # Field name made lowercase.
    purchases1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku7d = models.DecimalField(db_column='unitsSoldSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    acosclicks7d = models.DecimalField(db_column='acosClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku30d = models.DecimalField(db_column='purchasesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchases30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_advertised_product'


class SpPurchasedProduct(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    keywordid = models.DecimalField(db_column='keywordId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesothersku7d = models.DecimalField(db_column='purchasesOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks1d = models.DecimalField(db_column='unitsSoldClicks1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    matchtype = models.CharField(db_column='matchType', blank=True, null=True)  # Field name made lowercase.
    unitssoldothersku14d = models.DecimalField(db_column='unitsSoldOtherSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldothersku30d = models.DecimalField(db_column='unitsSoldOtherSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesothersku14d = models.DecimalField(db_column='salesOtherSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesroyalties14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRoyalties14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesothersku30d = models.DecimalField(db_column='salesOtherSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldothersku7d = models.DecimalField(db_column='unitsSoldOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesothersku1d = models.DecimalField(db_column='salesOtherSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    advertisedsku = models.CharField(db_column='advertisedSku', blank=True, null=True)  # Field name made lowercase.
    advertisedasin = models.CharField(db_column='advertisedAsin', blank=True, null=True)  # Field name made lowercase.
    keywordtype = models.CharField(db_column='keywordType', blank=True, null=True)  # Field name made lowercase.
    purchases1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasesothersku1d = models.DecimalField(db_column='purchasesOtherSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(blank=True, null=True)
    salesothersku7d = models.DecimalField(db_column='salesOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldothersku1d = models.DecimalField(db_column='unitsSoldOtherSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    kindleeditionnormalizedpagesread14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRead14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldclicks30d = models.DecimalField(db_column='unitsSoldClicks30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesothersku30d = models.DecimalField(db_column='purchasesOtherSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    portfolioid = models.DecimalField(db_column='portfolioId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    purchases30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasesothersku14d = models.DecimalField(db_column='purchasesOtherSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    purchasedasin = models.CharField(db_column='purchasedAsin', blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks7d = models.DecimalField(db_column='unitsSoldClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_purchased_product'


class SpTraffic(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    invalidclickthroughs = models.DecimalField(db_column='invalidClickThroughs', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    invalidimpressions = models.DecimalField(db_column='invalidImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grossimpressions = models.DecimalField(db_column='grossImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    invalidclickthroughrate = models.DecimalField(db_column='invalidClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    grossclickthroughs = models.DecimalField(db_column='grossClickThroughs', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    invalidimpressionrate = models.DecimalField(db_column='invalidImpressionRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_traffic'


class SponsoredBrandCampaign(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsalespercentage = models.DecimalField(db_column='newToBrandSalesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    qualifiedborrowsfromclicks = models.DecimalField(db_column='qualifiedBorrowsFromClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtolistfromclicks = models.DecimalField(db_column='addToListFromClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    costtype = models.CharField(db_column='costType', blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.DecimalField(db_column='viewClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    royaltyqualifiedborrowsfromclicks = models.DecimalField(db_column='royaltyQualifiedBorrowsFromClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasespromoted = models.DecimalField(db_column='purchasesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewrate = models.DecimalField(db_column='newToBrandDetailPageViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasespercentage = models.DecimalField(db_column='newToBrandPurchasesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qualifiedborrows = models.DecimalField(db_column='qualifiedBorrows', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salespromoted = models.DecimalField(db_column='salesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesrate = models.DecimalField(db_column='newToBrandPurchasesRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviews = models.DecimalField(db_column='video5SecondViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    topofsearchimpressionshare = models.DecimalField(db_column='topOfSearchImpressionShare', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    royaltyqualifiedborrows = models.DecimalField(db_column='royaltyQualifiedBorrows', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandecpdetailpageview = models.DecimalField(db_column='newToBrandECPDetailPageView', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtolist = models.DecimalField(db_column='addToList', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobranddetailpageviewsclicks = models.DecimalField(db_column='newToBrandDetailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewableimpressions = models.DecimalField(db_column='viewableImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.DecimalField(db_column='eCPAddToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviews = models.DecimalField(db_column='newToBrandDetailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviewrate = models.DecimalField(db_column='video5SecondViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldpercentage = models.DecimalField(db_column='newToBrandUnitsSoldPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_brand_campaign'


class SponsoredBrandsPlacement(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    placementclassification = models.CharField(db_column='placementClassification', blank=True, null=True)  # Field name made lowercase.
    newtobrandsalespercentage = models.DecimalField(db_column='newToBrandSalesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costtype = models.CharField(db_column='costType', blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.DecimalField(db_column='viewClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasespromoted = models.DecimalField(db_column='purchasesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewrate = models.DecimalField(db_column='newToBrandDetailPageViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasespercentage = models.DecimalField(db_column='newToBrandPurchasesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salespromoted = models.DecimalField(db_column='salesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesrate = models.DecimalField(db_column='newToBrandPurchasesRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviews = models.DecimalField(db_column='video5SecondViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandecpdetailpageview = models.DecimalField(db_column='newToBrandECPDetailPageView', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobranddetailpageviewsclicks = models.DecimalField(db_column='newToBrandDetailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewableimpressions = models.DecimalField(db_column='viewableImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.DecimalField(db_column='eCPAddToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviews = models.DecimalField(db_column='newToBrandDetailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviewrate = models.DecimalField(db_column='video5SecondViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldpercentage = models.DecimalField(db_column='newToBrandUnitsSoldPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_brands_placement'


class SponsoredBrandsSearchTerm(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordid = models.DecimalField(db_column='keywordId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviews = models.DecimalField(db_column='video5SecondViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    matchtype = models.CharField(db_column='matchType', blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    keywordbid = models.DecimalField(db_column='keywordBid', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    searchterm = models.CharField(db_column='searchTerm', blank=True, null=True)  # Field name made lowercase.
    costtype = models.CharField(db_column='costType', blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.DecimalField(db_column='viewClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    viewableimpressions = models.DecimalField(db_column='viewableImpressions', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordtext = models.CharField(db_column='keywordText', blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    video5secondviewrate = models.DecimalField(db_column='video5SecondViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_brands_search_term'


class SponsoredBrandsTargeting(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    matchtype = models.CharField(db_column='matchType', blank=True, null=True)  # Field name made lowercase.
    newtobrandsalespercentage = models.DecimalField(db_column='newToBrandSalesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costtype = models.CharField(db_column='costType', blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    targetingtype = models.CharField(db_column='targetingType', blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasespromoted = models.DecimalField(db_column='purchasesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewrate = models.DecimalField(db_column='newToBrandDetailPageViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasespercentage = models.DecimalField(db_column='newToBrandPurchasesPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordtext = models.CharField(db_column='keywordText', blank=True, null=True)  # Field name made lowercase.
    salespromoted = models.DecimalField(db_column='salesPromoted', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesrate = models.DecimalField(db_column='newToBrandPurchasesRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordid = models.DecimalField(db_column='keywordId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    topofsearchimpressionshare = models.DecimalField(db_column='topOfSearchImpressionShare', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandecpdetailpageview = models.DecimalField(db_column='newToBrandECPDetailPageView', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordbid = models.DecimalField(db_column='keywordBid', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    adkeywordstatus = models.CharField(db_column='adKeywordStatus', blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordtype = models.CharField(db_column='keywordType', blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    targetingid = models.DecimalField(db_column='targetingId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewsclicks = models.DecimalField(db_column='newToBrandDetailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targetingexpression = models.CharField(db_column='targetingExpression', blank=True, null=True)  # Field name made lowercase.
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targetingtext = models.CharField(db_column='targetingText', blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.DecimalField(db_column='eCPAddToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviews = models.DecimalField(db_column='newToBrandDetailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldpercentage = models.DecimalField(db_column='newToBrandUnitsSoldPercentage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_brands_targeting'


class SponsoredDisplayCampaign(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartviews = models.DecimalField(db_column='addToCartViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    newtobranddetailpageviewclicks = models.DecimalField(db_column='newToBrandDetailPageViewClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    costtype = models.CharField(db_column='costType', blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.CharField(db_column='viewClickThroughRate', blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewrate = models.DecimalField(db_column='newToBrandDetailPageViewRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviewviews = models.DecimalField(db_column='newToBrandDetailPageViewViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    leadformopens = models.DecimalField(db_column='leadFormOpens', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    leads = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressionsviews = models.DecimalField(db_column='impressionsViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandecpdetailpageview = models.CharField(db_column='newToBrandECPDetailPageView', blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cumulativereach = models.DecimalField(db_column='cumulativeReach', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchrate = models.DecimalField(db_column='brandedSearchRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressionsfrequencyaverage = models.DecimalField(db_column='impressionsFrequencyAverage', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    linkouts = models.DecimalField(db_column='linkOuts', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesviews = models.DecimalField(db_column='brandedSearchesViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    salespromotedclicks = models.DecimalField(db_column='salesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpbrandsearch = models.CharField(db_column='eCPBrandSearch', blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasespromotedclicks = models.DecimalField(db_column='purchasesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.CharField(db_column='eCPAddToCart', blank=True, null=True)  # Field name made lowercase.
    newtobranddetailpageviews = models.DecimalField(db_column='newToBrandDetailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_display_campaign'


class SponsoredDisplayMatchedTarget(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartviews = models.DecimalField(db_column='addToCartViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    brandedsearchrate = models.DecimalField(db_column='brandedSearchRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    linkouts = models.DecimalField(db_column='linkOuts', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesviews = models.DecimalField(db_column='brandedSearchesViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewclickthroughrate = models.DecimalField(db_column='viewClickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    salespromotedclicks = models.DecimalField(db_column='salesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpbrandsearch = models.CharField(db_column='eCPBrandSearch', blank=True, null=True)  # Field name made lowercase.
    leadformopens = models.DecimalField(db_column='leadFormOpens', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    purchasespromotedclicks = models.DecimalField(db_column='purchasesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    leads = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ecpaddtocart = models.CharField(db_column='eCPAddToCart', blank=True, null=True)  # Field name made lowercase.
    matchedtargetasin = models.CharField(db_column='matchedTargetAsin', blank=True, null=True)  # Field name made lowercase.
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressionsviews = models.DecimalField(db_column='impressionsViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_display_matched_target'


class SponsoredDisplayTargeting(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    newtobrandsalesclicks = models.DecimalField(db_column='newToBrandSalesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    viewabilityrate = models.DecimalField(db_column='viewabilityRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasesclicks = models.DecimalField(db_column='purchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    detailpageviews = models.DecimalField(db_column='detailPageViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssold = models.DecimalField(db_column='unitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartviews = models.DecimalField(db_column='addToCartViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    viewclickthroughrate = models.CharField(db_column='viewClickThroughRate', blank=True, null=True)  # Field name made lowercase.
    purchases = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    leadformopens = models.DecimalField(db_column='leadFormOpens', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    leads = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videocompleteviews = models.DecimalField(db_column='videoCompleteViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressionsviews = models.DecimalField(db_column='impressionsViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesclicks = models.DecimalField(db_column='salesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videofirstquartileviews = models.DecimalField(db_column='videoFirstQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks = models.DecimalField(db_column='unitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearches = models.DecimalField(db_column='brandedSearches', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchases = models.DecimalField(db_column='newToBrandPurchases', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesclicks = models.DecimalField(db_column='brandedSearchesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandsales = models.DecimalField(db_column='newToBrandSales', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchrate = models.DecimalField(db_column='brandedSearchRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    linkouts = models.DecimalField(db_column='linkOuts', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandpurchasesclicks = models.DecimalField(db_column='newToBrandPurchasesClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brandedsearchesviews = models.DecimalField(db_column='brandedSearchesViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartclicks = models.DecimalField(db_column='addToCartClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videounmutes = models.DecimalField(db_column='videoUnmutes', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocart = models.DecimalField(db_column='addToCart', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    videothirdquartileviews = models.DecimalField(db_column='videoThirdQuartileViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    addtocartrate = models.DecimalField(db_column='addToCartRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    salespromotedclicks = models.DecimalField(db_column='salesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targetingid = models.DecimalField(db_column='targetingId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpbrandsearch = models.CharField(db_column='eCPBrandSearch', blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssold = models.DecimalField(db_column='newToBrandUnitsSold', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    targetingexpression = models.CharField(db_column='targetingExpression', blank=True, null=True)  # Field name made lowercase.
    detailpageviewsclicks = models.DecimalField(db_column='detailPageViewsClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targetingtext = models.CharField(db_column='targetingText', blank=True, null=True)  # Field name made lowercase.
    purchasespromotedclicks = models.DecimalField(db_column='purchasesPromotedClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ecpaddtocart = models.CharField(db_column='eCPAddToCart', blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    videomidpointviews = models.DecimalField(db_column='videoMidpointViews', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newtobrandunitssoldclicks = models.DecimalField(db_column='newToBrandUnitsSoldClicks', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_display_targeting'


class SponsoredProductsCampaign(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    attributedsalessamesku1d = models.DecimalField(db_column='attributedSalesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbiddingstrategy = models.CharField(db_column='campaignBiddingStrategy', blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks1d = models.DecimalField(db_column='unitsSoldClicks1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku7d = models.DecimalField(db_column='attributedSalesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    topofsearchimpressionshare = models.DecimalField(db_column='topOfSearchImpressionShare', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku14d = models.DecimalField(db_column='attributedSalesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignrulebasedbudgetamount = models.CharField(db_column='campaignRuleBasedBudgetAmount', blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku30d = models.DecimalField(db_column='attributedSalesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesroyalties14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRoyalties14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku14d = models.DecimalField(db_column='purchasesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    spend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku1d = models.DecimalField(db_column='purchasesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku1d = models.DecimalField(db_column='unitsSoldSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    purchases1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku7d = models.DecimalField(db_column='purchasesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku7d = models.DecimalField(db_column='unitsSoldSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku30d = models.DecimalField(db_column='unitsSoldSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costperclick = models.DecimalField(db_column='costPerClick', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    clickthroughrate = models.DecimalField(db_column='clickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    kindleeditionnormalizedpagesread14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRead14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignapplicablebudgetrulename = models.CharField(db_column='campaignApplicableBudgetRuleName', blank=True, null=True)  # Field name made lowercase.
    purchasessamesku30d = models.DecimalField(db_column='purchasesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldclicks30d = models.DecimalField(db_column='unitsSoldClicks30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    purchases30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignapplicablebudgetruleid = models.CharField(db_column='campaignApplicableBudgetRuleId', blank=True, null=True)  # Field name made lowercase.
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku14d = models.DecimalField(db_column='unitsSoldSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks7d = models.DecimalField(db_column='unitsSoldClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_products_campaign'


class SponsoredProductsCampaignPlacement(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    attributedsalessamesku1d = models.DecimalField(db_column='attributedSalesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbiddingstrategy = models.CharField(db_column='campaignBiddingStrategy', blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks1d = models.DecimalField(db_column='unitsSoldClicks1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku7d = models.DecimalField(db_column='attributedSalesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    placementclassification = models.CharField(db_column='placementClassification', blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku14d = models.DecimalField(db_column='attributedSalesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    attributedsalessamesku30d = models.DecimalField(db_column='attributedSalesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesroyalties14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRoyalties14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku14d = models.DecimalField(db_column='purchasesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    spend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku1d = models.DecimalField(db_column='purchasesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku1d = models.DecimalField(db_column='unitsSoldSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku7d = models.DecimalField(db_column='purchasesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku7d = models.DecimalField(db_column='unitsSoldSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku30d = models.DecimalField(db_column='unitsSoldSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costperclick = models.DecimalField(db_column='costPerClick', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    clickthroughrate = models.DecimalField(db_column='clickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    kindleeditionnormalizedpagesread14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRead14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku30d = models.DecimalField(db_column='purchasesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldclicks30d = models.DecimalField(db_column='unitsSoldClicks30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku14d = models.DecimalField(db_column='unitsSoldSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks7d = models.DecimalField(db_column='unitsSoldClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_products_campaign_placement'


class SponsoredProductsSearchTerm(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    attributedsalessamesku1d = models.DecimalField(db_column='attributedSalesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    roasclicks14d = models.DecimalField(db_column='roasClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks1d = models.DecimalField(db_column='unitsSoldClicks1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    matchtype = models.CharField(db_column='matchType', blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku14d = models.DecimalField(db_column='attributedSalesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    attributedsalessamesku30d = models.DecimalField(db_column='attributedSalesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesroyalties14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRoyalties14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    searchterm = models.CharField(db_column='searchTerm', blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku1d = models.DecimalField(db_column='unitsSoldSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(blank=True, null=True)
    salesothersku7d = models.DecimalField(db_column='salesOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku7d = models.DecimalField(db_column='purchasesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku30d = models.DecimalField(db_column='unitsSoldSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    costperclick = models.DecimalField(db_column='costPerClick', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clickthroughrate = models.DecimalField(db_column='clickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesread14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRead14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    acosclicks14d = models.DecimalField(db_column='acosClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks30d = models.DecimalField(db_column='unitsSoldClicks30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    portfolioid = models.DecimalField(db_column='portfolioId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    roasclicks7d = models.DecimalField(db_column='roasClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku14d = models.DecimalField(db_column='unitsSoldSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks7d = models.DecimalField(db_column='unitsSoldClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordid = models.DecimalField(db_column='keywordId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku7d = models.DecimalField(db_column='attributedSalesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordbid = models.DecimalField(db_column='keywordBid', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targeting = models.CharField(blank=True, null=True)
    purchasessamesku14d = models.DecimalField(db_column='purchasesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldothersku7d = models.DecimalField(db_column='unitsSoldOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku1d = models.DecimalField(db_column='purchasesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    adkeywordstatus = models.CharField(db_column='adKeywordStatus', blank=True, null=True)  # Field name made lowercase.
    keywordtype = models.CharField(db_column='keywordType', blank=True, null=True)  # Field name made lowercase.
    purchases1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku7d = models.DecimalField(db_column='unitsSoldSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    acosclicks7d = models.DecimalField(db_column='acosClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku30d = models.DecimalField(db_column='purchasesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchases30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_products_search_term'


class SponsoredProductsTargeting(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.CharField(blank=True, null=True)
    attributedsalessamesku1d = models.DecimalField(db_column='attributedSalesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    roasclicks14d = models.DecimalField(db_column='roasClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks1d = models.DecimalField(db_column='unitsSoldClicks1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    matchtype = models.CharField(db_column='matchType', blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku14d = models.DecimalField(db_column='attributedSalesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    attributedsalessamesku30d = models.DecimalField(db_column='attributedSalesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesroyalties14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRoyalties14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku1d = models.DecimalField(db_column='unitsSoldSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='campaignStatus', blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(blank=True, null=True)
    salesothersku7d = models.DecimalField(db_column='salesOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku7d = models.DecimalField(db_column='purchasesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetamount = models.DecimalField(db_column='campaignBudgetAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases7d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku30d = models.DecimalField(db_column='unitsSoldSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    costperclick = models.DecimalField(db_column='costPerClick', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks14d = models.DecimalField(db_column='unitsSoldClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adgroupname = models.CharField(db_column='adGroupName', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.DecimalField(db_column='campaignId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clickthroughrate = models.DecimalField(db_column='clickThroughRate', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kindleeditionnormalizedpagesread14d = models.DecimalField(db_column='kindleEditionNormalizedPagesRead14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    acosclicks14d = models.DecimalField(db_column='acosClicks14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks30d = models.DecimalField(db_column='unitsSoldClicks30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    portfolioid = models.DecimalField(db_column='portfolioId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgetcurrencycode = models.CharField(db_column='campaignBudgetCurrencyCode', blank=True, null=True)  # Field name made lowercase.
    roasclicks7d = models.DecimalField(db_column='roasClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldsamesku14d = models.DecimalField(db_column='unitsSoldSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldclicks7d = models.DecimalField(db_column='unitsSoldClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordid = models.DecimalField(db_column='keywordId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    attributedsalessamesku7d = models.DecimalField(db_column='attributedSalesSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    topofsearchimpressionshare = models.DecimalField(db_column='topOfSearchImpressionShare', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    adgroupid = models.DecimalField(db_column='adGroupId', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    keywordbid = models.DecimalField(db_column='keywordBid', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targeting = models.CharField(blank=True, null=True)
    purchasessamesku14d = models.DecimalField(db_column='purchasesSameSku14d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitssoldothersku7d = models.DecimalField(db_column='unitsSoldOtherSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasessamesku1d = models.DecimalField(db_column='purchasesSameSku1d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    campaignbudgettype = models.CharField(db_column='campaignBudgetType', blank=True, null=True)  # Field name made lowercase.
    keywordtype = models.CharField(db_column='keywordType', blank=True, null=True)  # Field name made lowercase.
    purchases1d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitssoldsamesku7d = models.DecimalField(db_column='unitsSoldSameSku7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sales14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    acosclicks7d = models.DecimalField(db_column='acosClicks7d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impressions = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchasessamesku30d = models.DecimalField(db_column='purchasesSameSku30d', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchases14d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    purchases30d = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    clicks = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    campaignname = models.CharField(db_column='campaignName', blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_products_targeting'


class TweetsTweet(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=250)
    photo = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tweets_tweet'
