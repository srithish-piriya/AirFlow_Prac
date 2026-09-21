from airflow.sdk import dag,task


@dag(dag_id="xcom_auto")
def xcom_dag():
    @task.python
    def task1():
        print("fetching data.....")
        fetched_data = {"data":[1,2,3,4,5]}
        return fetched_data
    @task.python
    def task2(data:dict):
        print("Transform Data.....")
        trans_data = data["data"]*2
        print(trans_data)
        return {"data": trans_data}
    @task.python
    def task3(data:dict):
        print("storing data.....")
        strd_data = data
        return strd_data

    first = task1()
    second = task2(first)
    third = task3(second)
xcom_dag()