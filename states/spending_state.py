from aiogram.dispatcher.filters.state import State,StatesGroup


class SpendingState(StatesGroup):
    """State of add spending"""

    EnterSpending = State()
    Approval = State()
