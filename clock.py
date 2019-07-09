from apscheduler.schedulers.blocking import BlockingScheduler
import wingman

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=7)
def scheduled_job():
    wingman()

sched.start()
