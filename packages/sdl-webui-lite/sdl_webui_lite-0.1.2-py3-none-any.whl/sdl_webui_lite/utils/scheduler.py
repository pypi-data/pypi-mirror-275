import threading
import queue
import logging

"""
Task Manager
this script is used to schedule task, one can put task into the queue
the scheduler will auto execute tasks inside the queue
once task is executed, user cannot stop the action, but
one can cancel all pending tasks through `cancel_current_task`
"""


class TaskManager:
    def __init__(self):
        self.task_queue = queue.Queue()
        self.worker_thread = threading.Thread(target=self._process_tasks)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.cancel_flag = threading.Event()  # Flag to indicate task cancellation
        self.worker_thread.start()

    def list_all_tasks(self):
        with self.task_queue.mutex:
            self.logger.info(f"Pending task: {[task[0].__name__ for task in list(self.task_queue.queue)]}", )

    def _process_tasks(self):
        while True:
            task, kwargs = self.task_queue.get()
            if not self.cancel_flag.is_set():  # Check if task should be canceled
                self._execute_task(task, kwargs)
            self.task_queue.task_done()

    def _execute_task(self, task, kwargs):
        # Replace this with your task execution logic
        self.logger.info(f"Executing task: {task.__name__}", )
        self.list_all_tasks()
        output = task(**kwargs)
        # Simulating task cancellation by checking the cancel flag
        self.logger.info(f"Task finished: {task.__name__}, output: {output}", )
        if self.cancel_flag.is_set():
            self.logger.info("Task canceled")


    def add_task(self, task, kwargs):
        self.logger.info(f"Adding task: {task.__name__}, {kwargs}")
        self.task_queue.put((task, kwargs))
        self.list_all_tasks()

    def cancel_current_task(self):
        self.logger.info(f"Cancelling pending tasks")
        self.cancel_flag.set()
        while not self.task_queue.empty():
            self.task_queue.get()  # Remove all pending tasks
            self.task_queue.task_done()
        self.cancel_flag.clear()
        # self.list_all_tasks()

    def wait_completion(self):
        self.logger.info("Completing task")
        self.task_queue.join()


# Example usage
if __name__ == "__main__":
    def my_task(arg1, arg2):
        print("Running my_task with arguments:", arg1, arg2)

    task_queue = TaskManager()
    task_queue.add_task(my_task, dict(arg1="Argument 1", arg2="Argument 2"))
    task_queue.add_task(my_task, dict(arg1="Argument 2", arg2="Argument 2"))
    # task_queue.cancel_current_task()  # Cancels the current task
    task_queue.wait_completion()
