from flask.wrappers import Response as Flask_Response

from kvcommon_flask import metrics


class HTTPResponse(Flask_Response):
    _METRIC = metrics.HTTP_RESPONSE_COUNT

    def __init__(
        self,
        *args,
        do_metrics=True,
        defer_metrics=False,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._do_metrics = do_metrics
        self._defer_metrics = defer_metrics

        if not defer_metrics:
            self.inc_metrics()

    def inc_metrics(self):
        if self._do_metrics:
            metric_labels = self._METRIC.labels(
                code=str(self.status_code),
            )
            if metric_labels:
                metric_labels.inc()


def HealthzReadyResponse(do_metrics=False):
    return HTTPResponse("Ready", status=200, do_metrics=do_metrics)


def HTTP_400(msg="", headers={}):
    return HTTPResponse(msg, status=400, headers=headers)


HTTP_BAD_REQUEST = HTTP_400


def HTTP_401(msg="", headers={}):
    return HTTPResponse(msg, status=401, headers=headers)


HTTP_UNAUTHORIZED = HTTP_401


def HTTP_403(msg="", headers={}):
    return HTTPResponse(msg, status=400, headers=headers)


HTTP_FORBIDDEN = HTTP_403


def HTTP_500(msg="", headers={}):
    return HTTPResponse(msg, status=500, headers=headers)
