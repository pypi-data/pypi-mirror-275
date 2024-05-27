# KvCommon-Flask

Library of various [Flask](https://flask.palletsprojects.com/en/3.0.x/) utils that aren't worthy of their own dedicated libs.

This library isn't likely to be useful to anyone else; it's just a convenience to save me from copy/pasting between various projects I work on.


## Packages/Modules

| Package | Description |
|---|---|
|`metrics`|Prometheus Metrics utils & boilerplate
|`traces`|OTLP Traces utils & boilerplate
|`context`|Convenience utils for manipulating Flask config and flask.g context
|`middleware`|Basic middleware class using flask-http-middleware with prometheus metrics
|`responses`|Utils and classes for common HTTP Responses with built-in prometheus metrics
|`scheduler`|Utils for scheduling jobs on cron-like intervals with Flask-APScheduler and metrics + logging
