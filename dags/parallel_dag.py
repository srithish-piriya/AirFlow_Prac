from airflow.sdk import dag,task

@dag(dag_id = "parallel_dag")
def parallel_dag():
    @task.python
    def task1(**kwargs):
        print("working on task1.....")
        dict1 = {"name":[1,2,3,4,5,6]}
        print(f'fetch{dict1["name"]}')
        ti = kwargs['ti']
        ti.xcom_push(key='result',value=dict1)
    @task.python
    def task2(**kwargs):
        ti = kwargs['ti']
        dict2 = ti.xcom_pull(task_ids="task1",key="result")
        lst2 = dict2["name"]*2
        print(dict2)
        ti.xcom_push(key="result",value={"transformed":lst2})
    @task.python
    def task3():
        print("task 3 is running")
    @task.python
    def task4():
        print("Task 4 is running..")
        print("All tasks are succesfully completed")
    
    first=task1()
    sec = task2()
    third = task3()
    four = task4()

    first>>[sec,third]>>four
parallel_dag()

