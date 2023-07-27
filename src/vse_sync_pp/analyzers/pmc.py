### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze pmc log messages"""

from statemachine import StateMachine, State
from .analyzer import ClockClassAnalyzerBase

class TgmClock(StateMachine):
    # states
    freeRunState     = State("FREERUN", initial=True)
    lockedState      = State("LOCKED")
    holdoverInState  = State("HOLDOVER_IN_SPEC")
    holdoverOutState = State("HOLDOVER_OUT_SPEC")

    # state transitions
    sync = freeRunState.to(lockedState)
    ho_good = lockedState.to(holdoverInState)
    sync_rec_ho_good = holdoverInState.to(lockedState)
    ho_bad = holdoverInState.to(holdoverOutState)
    sync_rec_ho_bad = holdoverOutState.to(lockedState)
    freerun_ho_bad = holdoverOutState.to(freeRunState)

class TgmClockClassAnalyzer(ClockClassAnalyzerBase):
    """Analytime Clock Class Transition in T-GM"""
    id_ = 'pmc/gm-settings'
    parser = id_
    # TODO
