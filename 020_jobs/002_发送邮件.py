# !/usr/bin/env python
# coding=utf-8
"""
Author: lpp
CreatDate: 2022/1/24 16:54
Description:
"""

from airflow.operators.email import EmailOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import timedelta, datetime


default_args = {
    "owner": "lucas",  # dag拥有者，用于权限管控
    "depends_on_past": False,  # 是否依赖上游任务
    "email": ["3205577372@qq.com"],  # 告警通知邮箱地址
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 3,
    "retry_delay": timedelta(seconds=15),
}


with DAG(
    "002-发送email",
    default_args=default_args,
    description="send email to xxx",
    schedule_interval="0 * * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=3),
    tags=["email"],
    params={"args1": "args2"},
) as dag:
    t1 = SSHOperator(
        task_id="datetime_1",
        ssh_conn_id="wsl2",
        command="date +'%Y-%m-%d %H:%M:%S' >> /home/lucas/tmp/everyday.log",
    )

    email_task = EmailOperator(
        task_id="send_email",
        to="3205577372@qq.com",
        subject="服务出现错误!",
        html_content="""<h2>Airflow Email Test.</h2>""",
        dag=dag,
    )

    t3 = SSHOperator(
        task_id="datetime_2",
        ssh_conn_id="wsl2",
        command="date +'%Y-%m-%d %H:%M:%S' >> /home/lucas/tmp/everyday.log",
    )

    # 设置任务依赖
    t1 >> email_task >> t3


if __name__ == "__main__":
    dag.cli()
