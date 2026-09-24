from airflow.sdk import dag,task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag(dag_id="dag_parent")
def dag_parent():
    trigger_first_dag = TriggerDagRunOperator(
        task_id="trigger_first_dag",
        trigger_dag_id="first_orc"
        #waitfor_completion=True    
    )
    trigger_second_dag = TriggerDagRunOperator(
        task_id="trigger_second_dag", 
        trigger_dag_id="sec_orc"
        #waitfor_completion=True not mandatory waits for triggered dag completion
    )

    trigger_first_dag >> trigger_second_dag



dag_parent()