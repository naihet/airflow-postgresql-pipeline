from notifier import send_discord
import pendulum

def task_failure_alert(context):

    dag_id = context["dag"].dag_id
    task_id = context["task_instance"].task_id
    run_id = context["run_id"]
    # execution_date = context["logical_date"] # For GMT+0
    thai_time = (
        context["logical_date"]
        .in_timezone("Asia/Bangkok")
        .strftime("%Y-%m-%d %H:%M:%S")
    )
    message = f"""
❌ ETL Pipeline Failed

DAG: {dag_id}
Task: {task_id}
Run ID: {run_id}
Execution: {thai_time}
"""

    send_discord(message)


def dag_success_alert(context):

    dag_id = context["dag"].dag_id
    run_id = context["run_id"]
    # execution_date = context["logical_date"] # For GMT+0
    thai_time = (
        context["logical_date"]
        .in_timezone("Asia/Bangkok")
        .strftime("%Y-%m-%d %H:%M:%S")
    )
    message = f"""
✅ ETL Pipeline Completed

DAG: {dag_id}
Run ID: {run_id}
Execution: {thai_time}
"""

    send_discord(message)