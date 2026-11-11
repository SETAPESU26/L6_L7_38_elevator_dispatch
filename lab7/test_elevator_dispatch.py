
import pytest
from hypothesis import given, strategies as st

from elevator_dispatch import (
    parse_request,
    total_travel,
    load_percent,
)


# Fuzz tests for unexpected inputs

@given(st.text() | st.none())
def test_parse_request_no_crash(s):
    try:
        parse_request(s)
    except ValueError:
        pass


@given(st.text() | st.none())
def test_total_travel_no_crash(s):
    try:
        total_travel(s)
    except ValueError:
        pass


@given(st.text() | st.none())
def test_load_percent_no_crash(s):
    try:
        load_percent(s)
    except ValueError:
        pass


# Property-based tests for valid inputs

@given(st.integers(), st.integers())
def test_parse_request_valid_input(start, end):
    assert parse_request(f"{start}->{end}") == (start, end)


@given(st.lists(st.integers(), min_size=1))
def test_total_travel_valid_input(floors):
    csv = ",".join(map(str, floors))

    expected = sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )

    assert total_travel(csv) == expected


@given(
    st.integers(min_value=0),
    st.integers(min_value=1),
)
def test_load_percent_valid_input(load, capacity):
    assert load_percent(
        f"{load} of {capacity}"
    ) == load * 100 // capacity


def test_load_percent_rejects_zero_capacity():
    with pytest.raises(ValueError):
        load_percent("10 of 0")
