from bot_config import dp, bot
from aiogram import types
from random import randint

total = 150
turn = 1
text = ''
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'начинаем игру "Отними у младенца леденцы🍭🍭🍭". '
                                                      f'Всего у малыша Lollipops_eater_bot 150 леденцов. '
                                                      f'Можно брать не больше 28 штук. '
                                                      f'Выиграет тот, кто заберет последние сладости')
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'ты любишь сладкое? Напиши: да или нет')

@dp.message_handler(text=['да', 'Да', 'Нет', 'нет'])
async def start_play(message: types.Message):
    global total
    global turn
    total = 150
    if message.text:
        await bot.send_message(message.from_user.id, text=f'Хорошо! {message.from_user.first_name}, '
                                                          f'определим, кто ходит первым 🎲🎲')
        turn = randint(0, 1)  # жеребьевка очередности
        if turn == 1:
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, первый ход у тебя')
            await bot.send_message(message.from_user.id,
                                   text=f'{message.from_user.first_name}, сколько хочешь леденцов?')
        else:
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name},'
                                                              f' первый ход у Lollipops_eater_bot')
            loll = randint(1, 28)
            total -= int(loll)
            await bot.send_message(message.from_user.id, f'Младенец съел {loll}  🍭 и теперь у него осталось: {total}')
            await bot.send_message(message.from_user.id,
                                   text=f'{message.from_user.first_name}. Сколько ты хочешь взять?')
            turn = 1

@dp.message_handler()
async def anything(message: types.Message):
    global total
    global turn
    if turn == 1 and total > 28:
        if message.text.isdigit() and 0 < int(message.text) < 29:
            total -= int(message.text)
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, отнять у младенца {message.text}🍭 - это как? '
                                                         f'У него осталось: {total}')
            turn = 0
        if message.text.isdigit() and int(message.text) >= 29:
            await message.reply(f'{message.from_user.first_name} да ты жадина! Можно взять от 1 до 28 штук')
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}. '
                                                              f'Сколько ты хочешь опять взять?')
    if turn == 0 and total > 28:
        await bot.send_message(message.from_user.id, f'Детеныш рыдает 😭😭😭')
        loll = randint(1, 29)
        total -= int(loll)
        await bot.send_message(message.from_user.id, f'Младенец съел {loll} 🍭 и теперь у него осталось: {total}')
        if total > 28:
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}. '
                                                              f'Сколько ты хочешь опять взять?')
        turn = 1
    if turn == 1 and total <= 28:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, приятно отнимать у младенца последние {total}'
                               f' 🍭? Ты победил!')
    if turn == 0 and total <= 28:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, младенец доел последние {total}'
                               f' 🍭 и победил!')





