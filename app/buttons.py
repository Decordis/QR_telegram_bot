from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/instruction'), KeyboardButton(text='/GetQRcode')],
    [KeyboardButton(text='/example'), KeyboardButton(text='/help')]
], input_field_placeholder='Выберите пункт')

main1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/instruction'), KeyboardButton(text='/GetQRcode')],
    [KeyboardButton(text='/example'), KeyboardButton(text='/help')]
], input_field_placeholder='Вставьте ссылку/текст')

# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Upup', url = 'https://www.youtube.com/?app=desktop&hl=ru')]
# ])