#!/usr/bin/env python
# coding:utf-8

from datetime import timedelta, datetime
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago

"""--- 定义默认参数 ---"""
# 这些参数会传递给每个operator
# 您可以在operator初始化期间基于每个任务重写它们
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["3205577372@qq.com"],  # 告警通知邮箱地址
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


""" --- 实例化一个DAG --- """
# 我们需要一个 DAG 对象来嵌套我们的任务。
# 在这里，我们传递一个定义 dag_id 的字符串，该字符串用作 DAG 的唯一标识符。
# 我们还传递了刚刚定义的默认参数字典，
# 并为 DAG 定义了调度间隔时间（schedule_interval ）为1天 。
with DAG(
    "001-整点tasks",
    default_args=default_args,
    description="WSL2-每天每小时需要执行的tasks",
    schedule_interval="0 * * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=3),
    tags=["每小时任务", "every-hours"],
    params={"args1": "args2"},
) as dag:
    # 实例化Operator对象时会生成任务。
    # 从Operator实例化的对象称为任务。 第一个参数task_id充当任务的唯一标识符。

    t1 = SSHOperator(
        task_id="datetime_1",
        ssh_conn_id="wsl2",
        command="adate +'%Y-%m-%d %H:%M:%S' >> /home/lucas/tmp/everyday.log",
    )

    # t2 = SSHOperator(
    #     task_id="start_synctime",
    #     ssh_conn_id="wsl2",
    #     command="synctime1",
    # )

    t3 = SSHOperator(
        task_id="datetime_2",
        ssh_conn_id="wsl2",
        command="date +'%Y-%m-%d %H:%M:%S' >> /home/lucas/tmp/everyday.log",
    )

    t4 = SSHOperator(
        task_id="freeMem",
        ssh_conn_id="wsl2",
        command="sudo /home/lucas/myshell/free-mem.sh >> /home/lucas/tmp/everyday.log",
    )

    # t5 = SSHOperator(
    #     task_id="docker_ps",
    #     ssh_conn_id="wsl2",
    #     command="sudo docker ps -a --format 'table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}' >> /home/lucas/tmp/everyday.log",
    # )

    # 设置任务依赖
    t1 >> t3 >> t4

if __name__ == "__main__":
    dag.cli()
