import asyncio
import random
from typing import Optional, Callable
from aiogram import Bot
from aiogram.types import Message

from bot.data import MOTIVATION_MESSAGES, REMINDER_INTERVALS


class WorkoutTimer:
    """Mashq taymeri va eslatmalar"""

    def __init__(self, bot: Bot, chat_id: int):
        self.bot = bot
        self.chat_id = chat_id
        self._timer_task: Optional[asyncio.Task] = None
        self._reminder_task: Optional[asyncio.Task] = None
        self._paused = False
        self._cancelled = False
        self._remaining_time = 0

    async def start_timer(
        self,
        seconds: int,
        on_complete: Optional[Callable] = None,
        message: Optional[Message] = None
    ):
        """Taymerni boshlash"""
        self._cancelled = False
        self._paused = False
        self._remaining_time = seconds

        self._timer_task = asyncio.create_task(
            self._run_timer(seconds, on_complete, message)
        )

    async def _run_timer(
        self,
        seconds: int,
        on_complete: Optional[Callable],
        message: Optional[Message]
    ):
        """Taymer ishlashi"""
        try:
            start_time = asyncio.get_event_loop().time()
            elapsed = 0

            while elapsed < seconds and not self._cancelled:
                if self._paused:
                    await asyncio.sleep(0.5)
                    continue

                await asyncio.sleep(1)
                elapsed = int(asyncio.get_event_loop().time() - start_time)
                self._remaining_time = seconds - elapsed

                # Har 10 sekundda yangilash (katta taymerlar uchun)
                if seconds > 30 and elapsed % 10 == 0 and message:
                    remaining = seconds - elapsed
                    if remaining > 0:
                        try:
                            await message.edit_text(
                                f"⏱ Qoldi: {remaining} soniya\n\n"
                                f"{'█' * (remaining * 10 // seconds)}{'░' * (10 - remaining * 10 // seconds)}"
                            )
                        except:
                            pass

            if not self._cancelled and on_complete:
                await on_complete()

        except asyncio.CancelledError:
            pass

    async def start_countdown(
        self,
        seconds: int,
        message: Message,
        prefix: str = ""
    ) -> bool:
        """Countdown timer bilan xabarni yangilash"""
        self._cancelled = False
        self._paused = False

        for remaining in range(seconds, 0, -1):
            if self._cancelled:
                return False

            while self._paused:
                await asyncio.sleep(0.5)
                if self._cancelled:
                    return False

            progress = "█" * ((seconds - remaining) * 10 // seconds) + "░" * (remaining * 10 // seconds)

            try:
                await message.edit_text(
                    f"{prefix}\n\n"
                    f"⏱ **{remaining}** soniya qoldi\n"
                    f"[{progress}]",
                    parse_mode="Markdown"
                )
            except:
                pass

            await asyncio.sleep(1)

        return True

    def pause(self):
        """Pauzaga olish"""
        self._paused = True

    def resume(self):
        """Davom ettirish"""
        self._paused = False

    def cancel(self):
        """Bekor qilish"""
        self._cancelled = True
        if self._timer_task:
            self._timer_task.cancel()
        if self._reminder_task:
            self._reminder_task.cancel()

    @property
    def is_paused(self) -> bool:
        return self._paused

    @property
    def remaining(self) -> int:
        return self._remaining_time


class ReminderManager:
    """Eslatmalar menejeri - asabga teguvchi xabarlar"""

    def __init__(self, bot: Bot, chat_id: int):
        self.bot = bot
        self.chat_id = chat_id
        self._task: Optional[asyncio.Task] = None
        self._active = False

    async def start_reminders(self, interval: int = 30):
        """Eslatmalarni boshlash"""
        self._active = True
        self._task = asyncio.create_task(self._send_reminders(interval))

    async def _send_reminders(self, interval: int):
        """Eslatmalar yuborish"""
        reminder_count = 0
        current_interval = interval

        while self._active:
            await asyncio.sleep(current_interval)

            if not self._active:
                break

            reminder_count += 1
            message = random.choice(MOTIVATION_MESSAGES)

            # Har safar tezroq va jahldorroq
            if reminder_count > 2:
                message = f"😤😤😤 {message.upper()}"
            elif reminder_count > 4:
                message = f"🔥🔥🔥 HOZIROQ MASHQ QIL! {message.upper()} 🔥🔥🔥"

            try:
                await self.bot.send_message(
                    self.chat_id,
                    message,
                    parse_mode="Markdown"
                )
            except:
                pass

            # Intervallarni qisqartirish
            if reminder_count > 3:
                current_interval = max(15, interval // 2)

    def stop(self):
        """To'xtatish"""
        self._active = False
        if self._task:
            self._task.cancel()
