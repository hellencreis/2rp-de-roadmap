# -*- encoding: utf-8 -*-

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

#Carregar os dados das tabelas em dataframes
df_pok = spark.table("work_dataeng.pokemon_hellen")
#print df_pok.count(), len(df_pok.columns)

df_gen = spark.table("work_dataeng.generation_hellen")
#print df_gen.count(), len(df_gen.columns)

#Filtrar o dataframe pela data
df_gen = df_gen.filter(df_gen["date_introduced"] < "2002-11-21")

df_pok.show()
df_gen.show()

#Fazer o cache do dataframe
df_gen = df_gen.cache()

#Fazer a união (inner join) entre os dataframes de pokemon e generation
df_pok = df_pok.withColumnRenamed('generation', 'pokemon_generation') #renomear a coluna generation pois é igual no outro dataframe

new_join = df_pok.join(df_gen, on=[df_pok.pokemon_generation == df_gen.generation], how='inner')

columns_to_drop = ['generation'] #retirando uma das colunas idênticas
new_join = new_join.drop(*columns_to_drop)

new_join.show()

#Salvar o dataframe em uma nova tabela no Hive
new_join.write.mode('overwrite').format('orc').saveAsTable('work_dataeng.pokemons_oldschool_hellen')
