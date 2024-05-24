# Copyright (C) Okahu Inc 2023-2024. All rights reserved

import logging
from opentelemetry import context as context_api
from opentelemetry.context import attach, set_value
from opentelemetry.instrumentation.utils import (
    _SUPPRESS_INSTRUMENTATION_KEY,
)
from okahu_apptrace.wrap_common import WORKFLOW_TYPE_MAP, with_tracer_wrapper

logger = logging.getLogger(__name__)


@with_tracer_wrapper
def wrap(tracer, to_wrap, wrapped, instance, args, kwargs):
    if context_api.get_value(_SUPPRESS_INSTRUMENTATION_KEY):
        return wrapped(*args, **kwargs)
    name = "haystack_pipeline"
    attach(set_value("workflow_name", name))
    with tracer.start_as_current_span(f"{name}.workflow") as span:
        workflow_name = span.resource.attributes.get("service.name")
        set_workflow_attributes(span, workflow_name)
        
        response = wrapped(*args, **kwargs)

    return response

def set_workflow_attributes(span, workflow_name):
    span.set_attribute("workflow_name",workflow_name)
    span.set_attribute("workflow_type", WORKFLOW_TYPE_MAP["haystack"])
