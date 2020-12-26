from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='yes',
                callback_data='yes'
            )
        ],
        [
            InlineKeyboardButton(
                text='reset',
                callback_data='reset'
            )
        ]
    ]
)
