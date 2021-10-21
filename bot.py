import config
import logging

from filters import IsAdminFilter
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsAdminFilter)


# echo
@dp.message_handlers()
async def echo(message: types.Message):
    await message.answer(message.text)

#
# # remove new user joined messages
# @dp.message_handler(content_types=["new_chat_members"])
# async def on_user_joined(message: types.Message):
#     await message.delete()
#
#
# # ban command (admins only)
# @dp.message_handlers(is_admin=True, commands=["ban"], commands_prefix="!/")
# async def cmd_ban(message: types.Message):
#     if not message.reply_to_message:
#         await message.reply("Нецензурная лексика запрещена правилами Группы")
#         return
#     await message.bot.delete_message(chat_id=config.GROUP_ID, message_id=message.message_id)
#     await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message)
#     await message.reply_to_message.reply("Пользователь забанен!")
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #   print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# run long_polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)