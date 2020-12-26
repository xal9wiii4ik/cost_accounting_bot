from aiogram.dispatcher.filters.state import State,StatesGroup


class SpendingState(StatesGroup):
    """Класс состояний добавление расходов"""

    EnterSpending = State()
    Approval = State()
