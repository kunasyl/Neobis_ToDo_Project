from datetime import datetime, timedelta


class ToDoServices:
    @staticmethod
    def validate_deadline(deadline_date):
        return deadline_date - datetime.now() > timedelta(seconds=0)
