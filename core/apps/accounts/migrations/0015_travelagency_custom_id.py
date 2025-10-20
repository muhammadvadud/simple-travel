from django.db import migrations, models
import uuid

def generate_custom_ids(apps, schema_editor):
    TravelAgency = apps.get_model('accounts', 'TravelAgency')
    for agency in TravelAgency.objects.all():
        agency.custom_id = str(uuid.uuid4())
        agency.save(update_fields=["custom_id"])

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_participantmodel_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelagency',
            name='custom_id',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='custom id'),
        ),
        migrations.RunPython(generate_custom_ids),
    ]
