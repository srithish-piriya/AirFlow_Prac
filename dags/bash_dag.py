from airflow.sdk import dag,task
from airflow.operators.bash import BashOperator

@dag(dag_id = "bash_dag")
def bash_dag():
    @task.python
    def first_task():
        print("kjjfj")
    @task.python
    def second_task():
        print("kjcnk")
    @task.bash
    def bash_task1():
        return "echo https://airflow.apache.org/"
    bash_task2 = BashOperator(
        task_id ="bash_task2",
        bash_command ="echo https://airflow.apache.org/"
    )

    first = first_task()
    sec = second_task()
    bash_new = bash_task1()
    bash_old = bash_task2

    first >> sec >> bash_new >> bash_old
bash_dag()