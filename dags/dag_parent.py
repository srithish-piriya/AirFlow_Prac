from airflow.sdk import dag,task
from airflow.opearators.trigger import TriggerDagRunOperator

@dag(dag_id="dag_parent")
def dag_parent():
    trigger_first_dag = TriggerDagRunOperator(
        task_id="trigger_first_dag",
        trigger_dag_id="first_orc"
    )
    trigger_second_dag = TriggerDagRunOperator(
        task_id="trigger_second_dag", 
        trigger_dag_id="sec_orc"
    )

    trigger_first_dag >> trigger_second_dag



dag_parent()