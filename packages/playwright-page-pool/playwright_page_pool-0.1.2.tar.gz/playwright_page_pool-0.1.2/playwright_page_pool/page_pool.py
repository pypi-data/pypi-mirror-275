import asyncio
import contextlib
import multiprocessing
from types import TracebackType
from typing import Awaitable, Callable, Optional, Tuple

from playwright.async_api import BrowserContext, Page


class PagePool:
    """Manages a pool of Playwright browser pages within a given browser context.

    This class provides functionality to manage a pool of pages, \
    allowing for either reuse of pages or creation of new pages on demand. \
    It supports asynchronous operations and can be used as a context manager.

    Attributes
    ----------
        context (BrowserContext): The Playwright browser context associated with the page pool.
        max_pages (Union[int, None]): The maximum number of pages \
            that can be opened at once. Defaults to the number of CPU cores.
        page_initiator (Optional[Callable[[Page], Awaitable[None]]]): \
            An optional asynchronous callable that is called each time a new page is created.
        reuse_pages (bool): \
            Determines whether pages should be reused. If False, a new page is created for each acquisition.

    Methods
    -------
        acquire: Acquires a page from the pool.
        close_all: Closes all pages in the pool.

    Usage:
        async def run_example(pool: PagePool):
            async with pool.acquire() as page:
                await page.goto("https://example.com")
                print(await page.title())

        async def main(*args, **kwargs):
            async with PagePool(context=your_browser_context, reuse_pages=True) as pool:
                run_examples = [run_example(pool) for _ in range(10)]
                await asyncio.gather(*run_examples) # 10 tasks are executed concurrently

    """

    def __init__(
        self,
        context: BrowserContext,
        max_pages: Optional[int] = None,
        page_initiator: Optional[Callable[[Page], Awaitable[None]]] = None,
        reuse_pages: bool = False,
    ) -> None:
        self.context = context
        self.max_pages = max_pages if max_pages is not None else multiprocessing.cpu_count()
        self.page_initiator = page_initiator
        self.pages: list[Tuple[Page, asyncio.Event]] = []
        self.lock = asyncio.Semaphore(self.max_pages)
        self.reuse_pages = reuse_pages
        self.acquire = self._acquire_by_reuse if reuse_pages else self._acquire_by_opening_page

    async def close_all(self) -> None:
        if self.reuse_pages:
            await asyncio.gather(*(page.close() for page, _ in self.pages))
            self.pages.clear()

    @contextlib.asynccontextmanager
    async def _acquire_by_reuse(self):
        await self.lock.acquire()
        try:
            # Try to find an available page
            for page, event in self.pages:
                if event.is_set():
                    event.clear()
                    yield page
                    event.set()
                    return

            # No available page, create a new one if under max_pages limit
            if len(self.pages) < self.max_pages:
                page = await self.context.new_page()
                if self.page_initiator:
                    await self.page_initiator(page)
                event = asyncio.Event()
                self.pages.append((page, event))
                yield page
                event.set()
            else:
                # Wait for an available page
                page, event = self.pages[0]
                await event.wait()
                event.clear()
                yield page
                event.set()
        finally:
            self.lock.release()

    @contextlib.asynccontextmanager
    async def _acquire_by_opening_page(self):
        await self.lock.acquire()
        try:
            # Create a new page
            page = await self.context.new_page()
            if self.page_initiator:
                await self.page_initiator(page)
            yield page
        finally:
            # Close the page after use
            await page.close()
            self.lock.release()

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        await self.close_all()
