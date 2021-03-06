# Generated by Django 2.2 on 2020-03-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0018_auto_20200311_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectaccount',
            name='account_number',
            field=models.CharField(max_length=7, null=True, verbose_name='口座番号(7桁)'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='bank_code',
            field=models.CharField(max_length=4, null=True, verbose_name='銀行コード(4桁)'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='branch_code',
            field=models.CharField(max_length=3, null=True, verbose_name='支店コード(3桁)'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='dob_day',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], max_length=2, null=True, verbose_name='誕生日（日）'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='dob_month',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2, null=True, verbose_name='誕生日（月）'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='dob_year',
            field=models.CharField(choices=[('1920', '1920'), ('1921', '1921'), ('1922', '1922'), ('1923', '1923'), ('1924', '1924'), ('1925', '1925'), ('1926', '1926'), ('1927', '1927'), ('1928', '1928'), ('1929', '1929'), ('1930', '1930'), ('1931', '1931'), ('1932', '1932'), ('1933', '1933'), ('1934', '1934'), ('1935', '1935'), ('1936', '1936'), ('1937', '1937'), ('1938', '1938'), ('1939', '1939'), ('1940', '1940'), ('1941', '1941'), ('1942', '1942'), ('1943', '1943'), ('1944', '1944'), ('1945', '1945'), ('1946', '1946'), ('1947', '1947'), ('1948', '1948'), ('1949', '1949'), ('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('2000', '2001'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010')], max_length=4, null=True, verbose_name='誕生日（年）'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='kana_line2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='建物・部屋番号・その他（カナ）'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='kanji_line2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='建物・部屋番号・その他（漢字）'),
        ),
    ]
