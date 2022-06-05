# a wrapper for interfacing with the sw proxy

from asgiref.sync import sync_to_async
import asyncio
import itertools
import pythoncom

from SolidProxy.bootstrap import GetOrStartSWInst
from core.models import SWModel

_HEARTBEAT_INTERVAL_S = 10
_POLL_INTERVAL_S = 1

pythoncom.CoInitialize()
_sw_inst = None

async def _delayedCounter(delay_s: float, count_start:int = 0):
    for i in itertools.count(count_start):
        yield i
        await asyncio.sleep(delay_s)

async def heartbeat():
    async for i in _delayedCounter(_HEARTBEAT_INTERVAL_S):
        print(f"SWP_Wrapper Heartbeat {i}")


@sync_to_async
def _get_known_models():
    return set(list(SWModel.objects.values_list('title', flat=True)))

@sync_to_async
def _rm_known_model(t: str) -> None:
    SWModel.objects.filter(title=t).delete()

@sync_to_async
def _add_known_model(t: str) -> None:
    m = SWModel(title=t)
    m.save()

async def pollOpenFiles():
    """Poll and maintain a list of opened files,
        in reality we probably want to interface with some events/callbacks
        but that requires a level of thought that I'm not ready for
    """
    global _sw_inst

    async for i in _delayedCounter(_POLL_INTERVAL_S):
        open_docs = _sw_inst.GetDocuments()
        open_doc_titles = set(map(lambda x: x.GetTitle(), open_docs))

        known_docs_titles = await _get_known_models()

        new_docs = open_doc_titles - known_docs_titles
        closed_docs = known_docs_titles - open_doc_titles

        # if new_docs or closed_docs:
        if new_docs or closed_docs:
            print(f"File Change Detected - NEW: {new_docs}, CLOSE: {closed_docs}")

        for c in closed_docs:
            await _rm_known_model(c)

        for c in new_docs:
            await _add_known_model(c)

async def main_aio():
    print("A Main")
    asyncio.get_event_loop().create_task(heartbeat())
    asyncio.get_event_loop().create_task(pollOpenFiles())

def main():
    """Interface for working with the SolidWorks proxy"""
    print("Wrapper main!")

    global _sw_inst

    # need to call this within the thread scope
    pythoncom.CoInitialize()
    _sw_inst = GetOrStartSWInst()

    if _sw_inst is None:
        raise RuntimeError(f"Could not connect to SolidWorks Instance")

    loop = asyncio.new_event_loop()
    loop.create_task(main_aio())
    loop.run_forever()