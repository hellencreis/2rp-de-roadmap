from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator

usuario = "2rp-hellen"
default_args = {
    "owner": usuario,
    "start_date": datetime(2021, 12, 22),
    "depend_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "run_as_user": usuario,
    "proxy_user": usuario
}

with DAG (dag_id='de_hellen_dev', schedule_interval='0 0 * * *', start_date=datetime(2021, 12, 22), default_args=default_args, catchup=False) as DAG:

    t_dummy_op = DummyOperator(
        task_id="t_dummy_op",
        DAG=DAG
    )
   
    t_kinit = BashOperator(
        task_id="t_kinit",
        bash_command=f'kinit -kt /home/{usuario}/{usuario}.keytab {usuario}'
    )

    t_executar = BashOperator(
        task_id="t_executar",
        bash_command=f'bash /home/{usuario}/shell-script/executar.sh'
    )
    
    t_pokemon = TwoRPSparkSubmitOperator(
        task_id="t_pokemon",
        name="spark_job_pokemon",
        conn_id="spark_conn",
        application=f'/home/{usuario}/pokemon-script/pokemon.py',
        conf={'spark.yarn.queue':'root.users.{usuario}','spark.driver.memory':'20g'},
        keytab=f'/home/{usuario}/{usuario}.keytab',
        principal=usuario,
        proxy_user=None,
        verbose=True
    )

t_dummy_op >> t_kinit >> t_executar >> t_pokemon
