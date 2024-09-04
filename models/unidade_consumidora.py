from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.tipos_consumidor import TipoConsumidorDB


class UnidadeConsumidoraDB(Model):
    id = AutoField(column_name='unidade_consumidora_id')
    nome = CharField(column_name='unidade_consumidora_nome')
    tipo = ForeignKeyField(
        TipoConsumidorDB,
        column_name='unidade_consumidora_tipo_id',
        backref='unidades_consumidoras'
    )

    class Meta:
        database = database
        table_name = 'unidades_consumidoras'
