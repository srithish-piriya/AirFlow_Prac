from airflow.sdk import dag,task

@dag(dag_id ="first_orc")
def first_orc():
    @task.python
    def first_task():
        print("Hello Word")
    @task.python
    def second_task():
        print("kjdn")
    @task.python
    def third_task():
        print("kjjhbjdn")
     
    #defing task dependendencies 
    first = first_task()
    sec = second_task()
    third = third_task()
    first >> sec >> third

first_orc()