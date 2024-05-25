# Copyright (C) 2022 Rainer Garus
#
# This file is part of the ooresults Python package, a software to
# compute results of orienteering events.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import copy
from datetime import datetime
from datetime import timezone

import pytest

from ooresults.handler import handicap
from ooresults.repo.result_type import SplitTime
from ooresults.repo.result_type import SpStatus
from ooresults.repo.result_type import PersonRaceResult
from ooresults.repo.result_type import ResultStatus
from ooresults.repo.class_params import ClassParams


def t(a: datetime, b: datetime) -> int:
    diff = b.replace(microsecond=0) - a.replace(microsecond=0)
    return int(diff.total_seconds())


def test_compute_result_status_ok():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(s1, c1), status=SpStatus.OK
            ),
            SplitTime(
                control_code="102", punch_time=c2, time=t(s1, c2), status=SpStatus.OK
            ),
            SplitTime(
                control_code="103", punch_time=c3, time=t(s1, c3), status=SpStatus.OK
            ),
        ],
    )


def test_compute_result_status_mispunched():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103", "104"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.MISSING_PUNCH,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(s1, c1), status=SpStatus.OK
            ),
            SplitTime(
                control_code="102", punch_time=None, time=None, status=SpStatus.MISSING
            ),
            SplitTime(
                control_code="103", punch_time=c3, time=t(s1, c3), status=SpStatus.OK
            ),
            SplitTime(
                control_code="104", punch_time=None, time=None, status=SpStatus.MISSING
            ),
        ],
    )


def test_compute_result_status_ok_with_additionals():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    c4 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)
    c5 = datetime(2015, 1, 1, 12, 39, 9, tzinfo=timezone.utc)
    c6 = datetime(2015, 1, 1, 12, 39, 11, tzinfo=timezone.utc)
    c7 = datetime(2015, 1, 1, 12, 39, 13, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="105", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="101", punch_time=c3, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c4, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c5, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="101", punch_time=c6, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="104", punch_time=c7, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="105",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="101",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="102",
                punch_time=c4,
                time=t(s1, c4),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="103",
                punch_time=c5,
                time=t(s1, c5),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="101",
                punch_time=c6,
                time=t(s1, c6),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="104",
                punch_time=c7,
                time=t(s1, c7),
                status=SpStatus.ADDITIONAL,
            ),
        ],
    )


def test_compute_result_with_unknown_punch_times():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = SplitTime.NO_TIME
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = SplitTime.NO_TIME
    c4 = SplitTime.NO_TIME
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="104", punch_time=c3, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c4, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=None,
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="104",
                punch_time=c3,
                time=None,
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="103",
                punch_time=c4,
                time=None,
                status=SpStatus.OK,
            ),
        ],
    )


def test_compute_result_and_delete_additional_splittime_without_punch_times():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    c4 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)
    c5 = datetime(2015, 1, 1, 12, 39, 9, tzinfo=timezone.utc)
    c6 = datetime(2015, 1, 1, 12, 39, 11, tzinfo=timezone.utc)
    c7 = datetime(2015, 1, 1, 12, 39, 13, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="105", status=SpStatus.ADDITIONAL),
            SplitTime(control_code="101", punch_time=c3, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c4, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c5, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="101", punch_time=c6, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="104", punch_time=c7, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="101",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="102",
                punch_time=c4,
                time=t(s1, c4),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="103",
                punch_time=c5,
                time=t(s1, c5),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="101",
                punch_time=c6,
                time=t(s1, c6),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="104",
                punch_time=c7,
                time=t(s1, c7),
                status=SpStatus.ADDITIONAL,
            ),
        ],
    )


def test_compute_result_and_contain_additional_splittime_with_si_punch_time_but_without_punch_time():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    c4 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)
    c5 = datetime(2015, 1, 1, 12, 39, 9, tzinfo=timezone.utc)
    c6 = datetime(2015, 1, 1, 12, 39, 11, tzinfo=timezone.utc)
    c7 = datetime(2015, 1, 1, 12, 39, 13, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="105", si_punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="101", punch_time=c3, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c4, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c5, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="101", punch_time=c6, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="104", punch_time=c7, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="105",
                si_punch_time=c2,
                time=None,
                status=None,
            ),
            SplitTime(
                control_code="101",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="102",
                punch_time=c4,
                time=t(s1, c4),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="103",
                punch_time=c5,
                time=t(s1, c5),
                status=SpStatus.OK,
            ),
            SplitTime(
                control_code="101",
                punch_time=c6,
                time=t(s1, c6),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="104",
                punch_time=c7,
                time=t(s1, c7),
                status=SpStatus.ADDITIONAL,
            ),
        ],
    )


def test_compute_result_first_leg_voided():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard", voided_legs=[("S", "101")])

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()) - int((c1 - s1).total_seconds()),
        status=ResultStatus.OK,
        last_leg_voided=False,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
                leg_voided=True,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="103",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.OK,
                leg_voided=False,
            ),
        ],
    )


def test_compute_result_last_leg_voided():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard", voided_legs=[("103", "F")])

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()) - int((f1 - c3).total_seconds()),
        status=ResultStatus.OK,
        last_leg_voided=True,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="103",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.OK,
                leg_voided=False,
            ),
        ],
    )


def test_compute_result_several_legs_voided():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype="standard", voided_legs=[("101", "102"), ("102", "103")]
    )

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()) - int((c3 - c1).total_seconds()),
        status=ResultStatus.OK,
        last_leg_voided=False,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.OK,
                leg_voided=True,
            ),
            SplitTime(
                control_code="103",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.OK,
                leg_voided=True,
            ),
        ],
    )


def test_compute_result_legs_voided_with_unknown_punch_times_can_not_always_be_substracted_1():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = SplitTime.NO_TIME
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype="standard", voided_legs=[("101", "102"), ("102", "103")]
    )

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()) - (5 - 3),
        status=ResultStatus.OK,
        last_leg_voided=False,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=None,
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.OK,
                leg_voided=True,
            ),
            SplitTime(
                control_code="103",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.OK,
                leg_voided=True,
            ),
        ],
    )


def test_compute_result_legs_voided_with_unknown_punch_times_can_not_always_be_substracted_2():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = SplitTime.NO_TIME
    c3 = SplitTime.NO_TIME
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype="standard", voided_legs=[("101", "102"), ("102", "103")]
    )

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        last_leg_voided=False,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=None,
                status=SpStatus.OK,
                leg_voided=True,
            ),
            SplitTime(
                control_code="103",
                punch_time=c3,
                time=None,
                status=SpStatus.OK,
                leg_voided=True,
            ),
        ],
    )


def test_compute_result_legs_voided_with_unknown_punch_times_are_substracted_if_possible():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = SplitTime.NO_TIME
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype="standard", voided_legs=[("101", "102"), ("102", "103")]
    )

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()) - (6 - 2),
        status=ResultStatus.OK,
        last_leg_voided=False,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=2,
                status=SpStatus.OK,
                leg_voided=False,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=None,
                status=SpStatus.OK,
                leg_voided=True,
            ),
            SplitTime(
                control_code="103",
                punch_time=c3,
                time=6,
                status=SpStatus.OK,
                leg_voided=True,
            ),
        ],
    )


def test_compute_result_status_last_three_stations_missing():
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 11, tzinfo=timezone.utc)
    c4 = datetime(2015, 1, 1, 12, 39, 13, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101", "102", "103", "104", "105"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="106", punch_time=c3, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="107", punch_time=c4, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype="standard")

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.DID_NOT_FINISH,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(s1, c1), status=SpStatus.OK
            ),
            SplitTime(
                control_code="102", punch_time=c2, time=t(s1, c2), status=SpStatus.OK
            ),
            SplitTime(
                control_code="103", punch_time=None, time=None, status=SpStatus.MISSING
            ),
            SplitTime(
                control_code="104", punch_time=None, time=None, status=SpStatus.MISSING
            ),
            SplitTime(
                control_code="105", punch_time=None, time=None, status=SpStatus.MISSING
            ),
            SplitTime(
                control_code="106",
                punch_time=c3,
                time=t(s1, c3),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="107",
                punch_time=c4,
                time=t(s1, c4),
                status=SpStatus.ADDITIONAL,
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_given_result_status_is_disqualified_when_compute_result_then_result_status_is_disqualified(
    otype,
):
    time_limit = 60 if otype == "score" else None
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.DISQUALIFIED,
        punched_start_time=None,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params)
    if otype == "score":
        extensions = {
            "score_controls": 3,
            "score_overtime": None,
            "score": None,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=None,
        punched_start_time=None,
        finish_time=f1,
        punched_finish_time=f1,
        time=None,
        status=ResultStatus.DISQUALIFIED,
        extensions=extensions,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, time=None, status=SpStatus.OK),
            SplitTime(control_code="102", punch_time=c2, time=None, status=SpStatus.OK),
            SplitTime(control_code="103", punch_time=c3, time=None, status=SpStatus.OK),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_given_no_controls_and_status_ok_when_compute_result_then_result_is_not_changed(
    otype,
):
    time_limit = 60 if otype == "score" else None
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = []
    result = PersonRaceResult(
        status=ResultStatus.OK,
        punched_start_time=None,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, time=None, status=SpStatus.OK),
            SplitTime(
                control_code="102", punch_time=None, time=None, status=SpStatus.OK
            ),
            SplitTime(
                control_code="103", punch_time=None, time=None, status=SpStatus.MISSING
            ),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    new_result = copy.deepcopy(result)
    new_result.compute_result(controls=controls, class_params=class_params)
    assert new_result is not result
    assert new_result == result


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_given_no_controls_and_status_mp_when_compute_result_then_result_is_not_changed(
    otype,
):
    time_limit = 60 if otype == "score" else None
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = []
    result = PersonRaceResult(
        status=ResultStatus.MISSING_PUNCH,
        punched_start_time=None,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, time=None, status=SpStatus.OK),
            SplitTime(control_code="102", punch_time=c2, time=None, status=SpStatus.OK),
            SplitTime(control_code="103", punch_time=c3, time=None, status=SpStatus.OK),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    new_result = copy.deepcopy(result)
    new_result.compute_result(controls=controls, class_params=class_params)
    assert new_result is not result
    assert new_result == result


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_compute_result_status_no_start_time(otype):
    time_limit = 60 if otype == "score" else None
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=None,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params)
    if otype == "score":
        extensions = {
            "score_controls": 3,
            "score_overtime": None,
            "score": None,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=None,
        punched_start_time=None,
        finish_time=f1,
        punched_finish_time=f1,
        time=None,
        status=ResultStatus.MISSING_PUNCH,
        extensions=extensions,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, time=None, status=SpStatus.OK),
            SplitTime(control_code="102", punch_time=c2, time=None, status=SpStatus.OK),
            SplitTime(control_code="103", punch_time=c3, time=None, status=SpStatus.OK),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_compute_result_status_no_finish_time(otype):
    time_limit = 60 if otype == "score" else None
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    c3 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)

    controls = ["101", "102", "103"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=None,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="103", punch_time=c3, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params)
    if otype == "score":
        extensions = {
            "score_controls": 3,
            "score_overtime": None,
            "score": None,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=None,
        punched_finish_time=None,
        time=None,
        status=ResultStatus.DID_NOT_FINISH,
        extensions=extensions,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(s1, c1), status=SpStatus.OK
            ),
            SplitTime(
                control_code="102", punch_time=c2, time=t(s1, c2), status=SpStatus.OK
            ),
            SplitTime(
                control_code="103", punch_time=c3, time=t(s1, c3), status=SpStatus.OK
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_given_no_punches_and_old_status_is_dns_when_compute_result_then_new_status_is_dns(
    otype,
):
    time_limit = 60 if otype == "score" else None

    controls = ["101", "102"]
    result = PersonRaceResult(
        status=ResultStatus.DID_NOT_START,
        punched_start_time=None,
        punched_finish_time=None,
        time=None,
        split_times=[],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params)
    if otype == "score":
        extensions = {
            "score_controls": 0,
            "score_overtime": None,
            "score": None,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=None,
        punched_start_time=None,
        finish_time=None,
        punched_finish_time=None,
        time=None,
        status=ResultStatus.DID_NOT_START,
        extensions=extensions,
        split_times=[
            SplitTime(
                control_code="101", punch_time=None, time=None, status=SpStatus.MISSING
            ),
            SplitTime(
                control_code="102", punch_time=None, time=None, status=SpStatus.MISSING
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_given_no_punches_and_old_status_is_inactive_when_compute_result_then_new_status_is_inactive(
    otype,
):
    time_limit = 60 if otype == "score" else None

    controls = []
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=None,
        punched_finish_time=None,
        time=None,
        split_times=[],
    )
    class_params = ClassParams(
        otype=otype,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params)
    if otype == "score":
        extensions = {
            "score_controls": 0,
            "score_overtime": None,
            "score": None,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=None,
        punched_start_time=None,
        finish_time=None,
        punched_finish_time=None,
        time=None,
        status=ResultStatus.INACTIVE,
        extensions=extensions,
        split_times=[],
    )


@pytest.mark.parametrize("otype", ["standard", "net"])
def test_given_no_controls_but_punches_when_compute_result_then_status_is_finished(
    otype,
):
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    c2 = datetime(2015, 1, 1, 12, 39, 3, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 5, tzinfo=timezone.utc)

    controls = []
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
            SplitTime(control_code="102", punch_time=c2, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype=otype)

    result.compute_result(controls=controls, class_params=class_params)
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.FINISHED,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=c1,
                time=t(s1, c1),
                status=SpStatus.ADDITIONAL,
            ),
            SplitTime(
                control_code="102",
                punch_time=c2,
                time=t(s1, c2),
                status=SpStatus.ADDITIONAL,
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net"])
@pytest.mark.parametrize(
    "female, year_of_birth", [(True, 2000), (True, 1981), (False, 1941)]
)
def test_compute_handicap_ok(otype, female, year_of_birth):
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(otype=otype, apply_handicap_rule=True)

    result.compute_result(
        controls=controls,
        class_params=class_params,
        year=year_of_birth,
        gender="F" if female else "M",
    )

    h = handicap.Handicap()
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        extensions={
            "running_time": int((f1 - s1).total_seconds()),
            "factor": h.factor(female=female, year=f1.year - year_of_birth),
        },
        time=int(result.extensions["running_time"] * result.extensions["factor"]),
        status=ResultStatus.OK,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(s1, c1), status=SpStatus.OK
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net"])
@pytest.mark.parametrize(
    "female, year_of_birth", [(True, 2000), (True, 1981), (False, 1941)]
)
def test_compute_handicap_mp(otype, female, year_of_birth):
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 7, tzinfo=timezone.utc)

    controls = ["101"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[],
    )
    class_params = ClassParams(otype=otype, apply_handicap_rule=True)

    result.compute_result(
        controls=controls,
        class_params=class_params,
        year=year_of_birth,
        gender="F" if female else "M",
    )

    h = handicap.Handicap()
    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int(result.extensions["running_time"] * result.extensions["factor"]),
        status=ResultStatus.MISSING_PUNCH,
        extensions={
            "running_time": int((f1 - s1).total_seconds()),
            "factor": h.factor(female=female, year=f1.year - year_of_birth),
        },
        split_times=[
            SplitTime(
                control_code="101", punch_time=None, time=None, status=SpStatus.MISSING
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_compute_result_use_personal_start_time_if_using_start_control_is_no(otype):
    time_limit = 60 if otype == "score" else None
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    p1 = datetime(2015, 1, 1, 12, 38, 50, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        using_start_control="no",
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params, start_time=p1)
    if otype == "score":
        extensions = {
            "score_controls": 1,
            "score_overtime": 0,
            "score": 1,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=p1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - p1).total_seconds()),
        status=ResultStatus.OK,
        extensions=extensions,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(p1, c1), status=SpStatus.OK
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_compute_result_use_mass_time_if_no_personal_start_time_and_using_start_control_is_no(
    otype,
):
    time_limit = 60 if otype == "score" else None
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    p1 = datetime(2015, 1, 1, 12, 38, 50, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        using_start_control="no",
        mass_start=p1,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params)
    if otype == "score":
        extensions = {
            "score_controls": 1,
            "score_overtime": 0,
            "score": 1,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=p1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - p1).total_seconds()),
        status=ResultStatus.OK,
        extensions=extensions,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(p1, c1), status=SpStatus.OK
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_compute_result_use_punched_time_if_using_start_control_is_yes(otype):
    time_limit = 60 if otype == "score" else None
    s1 = datetime(2015, 1, 1, 12, 38, 59, tzinfo=timezone.utc)
    p1 = datetime(2015, 1, 1, 12, 38, 50, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=s1,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        using_start_control="yes",
        mass_start=p1,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params, start_time=p1)
    if otype == "score":
        extensions = {
            "score_controls": 1,
            "score_overtime": 0,
            "score": 1,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=s1,
        punched_start_time=s1,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - s1).total_seconds()),
        status=ResultStatus.OK,
        extensions=extensions,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(s1, c1), status=SpStatus.OK
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
def test_compute_result_use_personal_start_time_if_using_start_control_is_if_punched_and_no_punch_time(
    otype,
):
    time_limit = 60 if otype == "score" else None
    p1 = datetime(2015, 1, 1, 12, 38, 50, tzinfo=timezone.utc)
    c1 = datetime(2015, 1, 1, 12, 39, 1, tzinfo=timezone.utc)
    f1 = datetime(2015, 1, 1, 12, 39, 15, tzinfo=timezone.utc)

    controls = ["101"]
    result = PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=None,
        punched_finish_time=f1,
        time=None,
        split_times=[
            SplitTime(control_code="101", punch_time=c1, status=SpStatus.ADDITIONAL),
        ],
    )
    class_params = ClassParams(
        otype=otype,
        using_start_control="if_punched",
        mass_start=p1,
        time_limit=time_limit,
    )

    result.compute_result(controls=controls, class_params=class_params, start_time=p1)
    if otype == "score":
        extensions = {
            "score_controls": 1,
            "score_overtime": 0,
            "score": 1,
        }
    else:
        extensions = {}

    assert result == PersonRaceResult(
        start_time=p1,
        punched_start_time=None,
        finish_time=f1,
        punched_finish_time=f1,
        time=int((f1 - p1).total_seconds()),
        status=ResultStatus.OK,
        extensions=extensions,
        split_times=[
            SplitTime(
                control_code="101", punch_time=c1, time=t(p1, c1), status=SpStatus.OK
            ),
        ],
    )
