from datetime import datetime
from typing import Any

from apscheduler.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.base import BaseTrigger

from nestipy.common import Injectable


class _Undefined(object):
    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

    def __repr__(self):
        return '<undefined>'


undefined = _Undefined()


@Injectable()
class SchedulerRegistry:
    _scheduler = AsyncIOScheduler = AsyncIOScheduler()

    def get_scheduler(self) -> AsyncIOScheduler:
        return self._scheduler

    def get_cron_job(self, _id: str) -> Job | None:
        return self._scheduler.get_job(_id)

    def remove_cron_job(self, _id: str):
        return self._scheduler.remove_job(_id)

    def get_cron_jobs(self) -> list[Job]:
        return self._scheduler.get_jobs()

    def add_cron_job(
            self,
            func: Any,
            trigger: str | BaseTrigger = None,
            args: list | tuple = None,
            kwargs: dict = None,
            id: str = None,
            name: str = None,
            misfire_grace_time: int = undefined,
            coalesce: bool = undefined,
            max_instances: int = undefined,
            next_run_time: datetime = undefined,
            jobstore: str = 'default',
            executor: str = 'default',
            replace_existing: bool = False,
            **trigger_args: Any
    ):
        return self._scheduler.add_job(
            func, trigger, args, kwargs, id, name, misfire_grace_time, coalesce,
            max_instances, next_run_time, jobstore, executor, replace_existing,
            **trigger_args
        )
