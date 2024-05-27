import json
from enum import Enum
from typing import Any, Dict

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


class EventAfter(Enum):
    RECEIVE = "receive"
    SETTLE = "settle"
    SWAP = "swap"


class EventCollector:
    _receive_events: Dict[str, Any] = {}
    _settle_events: Dict[str, Any] = {}
    _swap_events: Dict[str, Any] = {}

    def __init__(self, encoder: type[json.JSONEncoder] = DjangoJSONEncoder):
        self.encoder = encoder
        self.clear()

    def add(self, name: str, params: Dict[str, Any], after: EventAfter):
        if after == EventAfter.RECEIVE:
            self._receive_events[name] = params
        if after == EventAfter.SETTLE:
            self._settle_events[name] = params
        if after == EventAfter.SWAP:
            self._swap_events[name] = params

    def clear(self):
        self._receive_events = {}
        self._settle_events = {}
        self._swap_events = {}

    def _get_event_calls(self):
        calls = []

        for name, data in self._receive_events.items():
            calls.append((name, data, EventAfter.RECEIVE.value))
        for name, data in self._settle_events.items():
            calls.append((name, data, EventAfter.SETTLE.value))
        for name, data in self._swap_events.items():
            calls.append((name, data, EventAfter.SWAP.value))

        return calls

    def _apply_manual_header(
        self,
        response: HttpResponse,
        header: str,
        data: Any,
        merge=False,
    ):
        if not merge or header not in response.headers:
            response.headers[header] = json.dumps(data, cls=self.encoder)
            return
        header_data = json.loads(response.headers[header])
        header_data = {
            **header_data,
            **data,
        }
        response.headers[header] = json.dumps(header_data, cls=self.encoder)

    def _apply_manual(self, response: HttpResponse, merge=False):
        self._apply_manual_header(response, "HX-Trigger", self._receive_events, merge)
        self._apply_manual_header(
            response, "HX-Trigger-After-Settle", self._settle_events, merge
        )
        self._apply_manual_header(
            response, "HX-Trigger-After-Swap", self._swap_events, merge
        )

    def _apply_htmx(self, response: HttpResponse):
        try:
            from django_htmx.http import trigger_client_event

            calls = self._get_event_calls()
            for name, data, after in calls:
                trigger_client_event(
                    response, name, data, after=after, encoder=self.encoder
                )
        except ImportError:
            self._apply_manual(response)

    def apply(self, response: HttpResponse, use_django_htmx=True, manual_merge=False):
        if not use_django_htmx:
            return self._apply_manual(response, manual_merge)
        self._apply_htmx(response)
