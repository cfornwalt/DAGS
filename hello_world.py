from airflow.operators.python_operator import PythonOperator
from airflow import DAG
import airflow.utils.dates


def first_function_execute():
    return 'Hello World'


# passing parameter in DAG
def second_function_execute(**kwargs):
    var = kwargs.get('key', "there!")  # if failed to get the value set 'there!' as default
    return f'Hello {var}'


default_args = {
    "owner": "Airflow",
    "start_date": airflow.utils.dates.days_ago(1)

}
info = {'key': dag_run.conf['key']}


with DAG(
        dag_id='my_first_dag',
        schedule_interval="@once",  # Executed every minute # 0 0 * * * Every day at midnight
        default_args=default_args,
        catchup=False
) as dag:

    python_task_1 = PythonOperator(
        task_id='python_task_1',
        python_callable=first_function_execute
    )

    python_task_2 = PythonOperator(
        task_id='python_task_2',
        python_callable=second_function_execute,
        op_kwargs=info  # to pass arguments
    )



python_task_1 >> python_task_2