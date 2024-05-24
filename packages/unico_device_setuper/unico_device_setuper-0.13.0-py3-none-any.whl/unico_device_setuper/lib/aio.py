import asyncio
import itertools
import typing


async def iter_unordered[T](
    futures: typing.Iterable[typing.Coroutine[typing.Any, typing.Any, T]], max_concurrency: int
):
    pending: set[asyncio.Task[T]] = set()
    fut_todo = iter(futures)

    while True:
        pending.update(
            asyncio.create_task(fut)
            for fut in itertools.islice(fut_todo, max_concurrency - len(pending))
        )
        if len(pending) == 0:
            break
        done, pending = await asyncio.wait(pending, return_when='FIRST_COMPLETED')
        for t in done:
            yield t.result()


async def gather_unordered[T](
    futures: typing.Iterable[typing.Coroutine[typing.Any, typing.Any, T]], max_concurrency: int
):
    return [t async for t in iter_unordered(futures, max_concurrency)]
