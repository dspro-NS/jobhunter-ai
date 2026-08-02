from collectors.greenhouse import get_jobs as greenhouse_jobs
from collectors.workday import get_jobs as workday_jobs
from collectors.lever import get_jobs as lever_jobs
from collectors.ashby import get_jobs as ashby_jobs


COLLECTORS = {
    "greenhouse": greenhouse_jobs,
    "workday": workday_jobs,
    "lever": lever_jobs,
    "ashby": ashby_jobs,
}