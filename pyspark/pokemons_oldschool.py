%pyspark
spark.version
print(type(spark))
print(type(sc))
print(type(sqlContext))
print(type(z))

%pyspark
#Carregar os dados das tabelas em dataframes
df_pok = spark.table("work_dataeng.pokemon_hellen")
#print df_pok.count(), len(df_pok.columns)

df_gen = spark.table("work_dataeng.generation_hellen")
#print df_gen.count(), len(df_gen.columns)

#df_gen = spark.where(func.col("date_introduced") < "2002-11-21")
df_gen = df_gen.filter(df_gen["date_introduced"] < "2002-11-21")

df_pok.show()
df_gen.show()

df_gen = df_gen.cache() #fazer o cache do dataframe

%pyspark
#Fazer a união (inner join) entre os dataframes de pokemon e generation
df_pok = df_pok.withColumnRenamed('generation', 'pokemon_generation') #renomear a coluna generation pois é igual no outro dataframe

new_join = df_pok.join(df_gen, on=[df_pok.pokemon_generation == df_gen.generation], how='inner')

columns_to_drop = ['generation'] #retirando uma das colunas idênticas
new_join = new_join.drop(*columns_to_drop)

new_join.show()

%pyspark
#Salvar o dataframe em uma nova tabela no Hive
new_join.createOrReplaceTempView("new_join")

spark.sql("drop table if exists work_dataeng.pokemons_oldschool_hellen")

spark.sql("create table work_dataeng.pokemons_oldschool_hellen as select * from new_join")
