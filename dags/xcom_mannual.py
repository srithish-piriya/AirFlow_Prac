from airflow.sdk import dag,task

@dag(dag_id="xcom_mannual")
def xcom_mannual():
    @task.python
    def task1(**kwargs):
        print("Fetching data........")
        ti = kwargs["ti"]
        fetched_data = {"fetched_data":[1,2,3,4,5]}
        print(f"fetched data {fetched_data }")
        ti.xcom_push(key='return_result',value=fetched_data)
    @task.python
    def task2(**kwargs):
        print("transforming data....")
        ti = kwargs["ti"]
        data = ti.xcom_pull(task_ids= "task1",key="return_result")
        trans_data = data["fetched_data"]*2
        print(f"transformed data is {trans_data}")
        ti.xcom_push(key="return_result",value={"trans_data":trans_data})
    @task.python
    def task3(**kwargs):
        ti = kwargs["ti"]
        print("loading data......")
        load_data=ti.xcom_pull(task_ids= "task2",key="return_result")
        print(f"loaded data is {load_data}")
        ti.xcom_push(key="return_result",value=load_data)


    first = task1()
    second=task2()
    third = task3()


    first >> second>>third
xcom_mannual()