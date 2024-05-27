import sys
import time
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chariot_scaffold import version, log
from chariot_scaffold.exceptions import ActionRetry, SDKError
from chariot_scaffold.schema.base import ActionOutputModel, ActionOutputBodyModel
from chariot_scaffold.api_server.action_router import action_router


app = FastAPI(title="千乘SOAR", version=version, description="YYDS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
app.include_router(action_router, tags=["动作"])


def timing(s_time):
    """计时器"""
    e_time = time.perf_counter()
    c_time = e_time - s_time
    cost = "%.5fs" % c_time if c_time < 0 else "%.5fms" % (c_time * 1000)
    return cost


async def sieve_middleware(request: Request, call_next):
    """
    统一拦截所有异常
    """
    s_time = time.perf_counter()

    try:
        response = await call_next(request)
        log.debug(f"{request.client.host}:{request.client.port} | 200 | {timing(s_time)} | {request.method} | {request.url}")
        return response

    except ActionRetry as action_retry:
        log.error(f"{request.client.host}:{request.client.port} | 201 | {timing(s_time)} | {request.method} | {request.url}")
        output = ActionOutputModel(code=201, message=str(action_retry), body={})
        return JSONResponse(content=output.model_dump(), status_code=200)

    except SDKError as sdk_error:
        log.error(f"{request.client.host}:{request.client.port} | 500 | {timing(s_time)} | {request.method} | {request.url}")

        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback)
        log.error("\n" + exc_type.__name__ + " " + str(exc_value))

        output = ActionOutputModel(code=500, message=str(sdk_error), body={})
        return JSONResponse(content=output.model_dump(), status_code=200)

    except Exception as e:
        log.error(f"{request.client.host}:{request.client.port} | 500 | {timing(s_time)} | {request.method} | {request.url}")

        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback)
        log.error("\n" + exc_type.__name__ + " " + str(exc_value))

        output = ActionOutputModel(
            code=500, message="任务运行失败", body=ActionOutputBodyModel(
                status="error", log=str(e), error_trace=f"{exc_type.__name__} {exc_value}"
            )
        )
        return JSONResponse(content=output.model_dump(), status_code=200)


app.middleware('http')(sieve_middleware)


def runserver(workers):
    import uvicorn
    uvicorn.run(
        "chariot_scaffold.api_server.app:app", host="0.0.0.0", port=10001, workers=workers, reload=True,
        log_level="critical"
    )
