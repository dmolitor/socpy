from request import soccer_req
from response import coalesce_results, soccer_enrich, soccer_resp
from utils import map_dict, recycle_args

def soccer_engine(job_title, job_desc = None, industry = None, n_results = 10, **kwargs):
    request = soccer_req(
        job_title = job_title,
        job_desc = job_desc,
        industry = industry,
        n_results = n_results
    )
    response = soccer_resp(request)
    enriched = soccer_enrich(
        resp = response,
        **kwargs
    )
    return enriched

def soccer(job_title, job_desc = None, industry = None, n_results = 10, **kwargs):
    fun_args = recycle_args(
        job_title = job_title, 
        job_desc = job_desc,
        industry = industry,
        n_results = n_results,
        **kwargs
    )
    tst = map_dict(fun = soccer_engine, **fun_args)
    return coalesce_results(tst)
