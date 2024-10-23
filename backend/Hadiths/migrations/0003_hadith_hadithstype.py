# Generated by Django 5.1.2 on 2024-10-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hadiths', '0002_alter_hadith_explantion'),
    ]

    operations = [
        migrations.AddField(
            model_name='hadith',
            name='hadithstype',
            field=models.CharField(choices=[('حسن', 'حسن'), ('صحيح', 'صحيح'), ('ضعيف', 'ضعيف'), ('معلق', 'معلق'), ('منقطع', 'منقطع'), ('معضل', 'معضل'), ('المُرسَل', 'المُرسَل'), ('مرسل الصحابي', 'مرسل الصحابي'), ('المدلس', 'المدلس'), ('الموضوع', 'الموضوع'), ('المتروك', 'المتروك'), ('المنكر', 'المنكر'), ('المطروح', 'المطروح'), ('المضعف', 'المضعف'), ('المجهول', 'المجهول'), ('المدرج', 'المدرج'), ('المقلوب', 'المقلوب'), ('المُضطرِب', 'المُضطرِب'), ('المصحف والمحرف', 'المصحف والمحرف'), ('الشاذ', 'الشاذ'), ('المعلل', 'المعلل'), ('المرفوع', 'المرفوع'), ('الموقوف', 'الموقوف'), ('المقطوع', 'المقطوع'), ('المتواتر', 'المتواتر'), ('خبر الآحاد', 'خبر الآحاد'), ('المُسنَد', 'المُسنَد'), ('المتصل', 'المتصل'), ('المسلسل', 'المسلسل'), ('الاعتبار', 'الاعتبار'), ('حديث الفرد', 'حديث الفرد'), (' المعنعن', ' المعنعن'), (' المؤنن', ' المؤنن'), (' المنقلب', ' المنقلب'), (' العالي', ' العالي'), (' النازل', ' النازل'), (' الغريب', ' الغريب'), (' المبهم', ' المبهم'), (' المدبج', ' المدبج'), (' الناسخ والمنسوخ', ' الناسخ والمنسوخ'), (' المؤتلف والمختلف', ' المؤتلف والمختلف')], default='حسن', max_length=250),
            preserve_default=False,
        ),
    ]
