import json_log_formatter


class JsonFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):

        request = extra.pop("request", None)
        if request:
            extra["ip"] = request.META.get("HTTP_X_FORWARDED_FOR")
            extra["agent"] = request.META.get("HTTP_USER_AGENT")

        sender = extra.pop("sender", None)
        if sender:
            extra["sender"] = sender.__class__.__name__

        return super(JsonFormatter, self).json_record(message, extra, record)
