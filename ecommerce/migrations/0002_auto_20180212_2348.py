# Generated by Django 2.0.1 on 2018-02-12 23:48

from django.db import migrations

def add_cat_type_user(apps, schema_editor):
    
    Cat_type_user = apps.get_model('ecommerce', 'Cat_type_user')

    Cat_type_user.objects.create(
        type_user="Buyer"
    )

    Cat_type_user.objects.create(
        type_user="Seller"
    )

    Cat_type_user.objects.create(
        type_user="Administrator"
    )

def add_cat_category(apps, schema_editor):

    Cat_category = apps.get_model('ecommerce', 'Cat_category')

    Cat_category.objects.create(
        category="Cerámica"
    )

    Cat_category.objects.create(
        category="Madera"
    )

    Cat_category.objects.create(
        category="Fibras vegetales"
    )

    Cat_category.objects.create(
        category="Marmol, piedra o vidrio"
    )

    Cat_category.objects.create(
        category="Metal"
    )

    Cat_category.objects.create(
        category="Piel y cuero"
    )

    Cat_category.objects.create(
        category="Textil"
    )

    Cat_category.objects.create(
        category="Joyería"
    )

    Cat_category.objects.create(
        category="Instrumentos musicales"
    )

    Cat_category.objects.create(
        category="Otro"
    )

def add_cat_skill(apps, schema_editor):

    Cat_skill = apps.get_model('ecommerce', 'Cat_skill')

    Cat_skill.objects.create(
        skill="Cerámica"
    )

    Cat_skill.objects.create(
        skill="Madera"
    )

    Cat_skill.objects.create(
        skill="Fibras vegetales"
    )

    Cat_skill.objects.create(
        skill="Marmol, piedra o vidrio"
    )

    Cat_skill.objects.create(
        skill="Metal"
    )

    Cat_skill.objects.create(
        skill="Piel y cuero"
    )

    Cat_skill.objects.create(
        skill="Textil"
    )

    Cat_skill.objects.create(
        skill="Joyería"
    )

    Cat_skill.objects.create(
        skill="Instrumentos musicales"
    )

    Cat_skill.objects.create(
        skill="Otro"
    )

def add_cat_attribute(apps, schema_editor):

    Cat_attribute = apps.get_model('ecommerce', 'Cat_attribute')

    Cat_attribute.objects.create(
        attribute="Peso"
    )

    Cat_attribute.objects.create(
        attribute="Tamaño"
    )

    Cat_attribute.objects.create(
        attribute="Color"
    )

def add_cat_pay_type(apps, schema_editor):

    Cat_pay_type = apps.get_model('ecommerce', 'Cat_pay_type')

    Cat_pay_type.objects.create(
        pay_type="PayPal"
    )

    Cat_pay_type.objects.create(
        pay_type="PayU"
    )

    Cat_pay_type.objects.create(
        pay_type="Terjeta de crédito o débito"
    )

def add_cat_status_order(apps, schema_editor):

    Cat_status_order = apps.get_model('ecommerce', 'Cat_status_order')

    Cat_status_order.objects.create(
        status="PENDING_PAY",
        description="En espera de pago"
    )

    Cat_status_order.objects.create(
        status="PAYED",
        description="Pagado"
    )

    Cat_status_order.objects.create(
        status="PENDING_SEND",
        description="En proceso de envío"
    )

    Cat_status_order.objects.create(
        status="SENT",
        description="Enviado"
    )

    Cat_status_order.objects.create(
        status="DELIVERED",
        description="Entregado"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_cat_type_user),
        migrations.RunPython(add_cat_category),
        migrations.RunPython(add_cat_attribute),
        migrations.RunPython(add_cat_skill),
        migrations.RunPython(add_cat_pay_type),
        migrations.RunPython(add_cat_status_order),
    ]
