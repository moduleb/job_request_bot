from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text="Hello")
