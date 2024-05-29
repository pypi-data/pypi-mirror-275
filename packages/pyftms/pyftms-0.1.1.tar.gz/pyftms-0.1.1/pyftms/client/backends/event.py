# Copyright 2024, Sergey Dudanov
# SPDX-License-Identifier: Apache-2.0

from typing import Callable, Literal, NamedTuple, NotRequired, TypedDict

from ...models import (
    IndoorBikeSimulationParameters,
    SpinDownControlCode,
    SpinDownSpeedData,
    SpinDownStatusCode,
    TrainingStatusCode,
)
from ..properties import MovementDirection

FtmsNumbers = int | float
ControlSource = Literal["callback", "user", "safety", "other"]
SimpleControlEvents = Literal["start", "stop", "pause", "reset"]


class SpinDownEventData(TypedDict, total=False):
    """`SpinDownEvent` data."""

    target_speed: SpinDownSpeedData
    """From fitness machine to client. Indicate successfully operation."""
    code: SpinDownControlCode
    """From client to fitness machine. START or IGNORE."""
    status: SpinDownStatusCode
    """From fitness machine to client."""


class SetupEventData(TypedDict, total=False):
    """`SetupEvent` data."""

    indoor_bike_simulation: IndoorBikeSimulationParameters
    """Indoor Bike Simulation Parameters."""
    target_cadence: float
    """
    Targeted cadence.

    Units: `rpm`.
    """
    target_distance: int
    """
    Targeted distance.

    Units: `meters`.
    """
    target_energy: int
    """
    Targeted expended energy.

    Units: `kcals`.
    """
    target_heart_rate: int
    """
    Targeted heart rate.

    Units: `bpm`.
    """
    target_inclination: float
    """
    Targeted inclination.

    Units: `%`.
    """
    target_power: int
    """
    Targeted power.

    Units: `Watts`.
    """
    target_resistance: float | int
    """
    Targeted resistance level.

    Units: `unitless`.
    """
    target_speed: float
    """
    Targeted speed.

    Units: `km/h`.
    """
    target_steps: int
    """
    Targeted number of steps.

    Units: `steps`.
    """
    target_strides: int
    """
    Targeted number of strides.

    Units: `strides`.
    """
    target_time: tuple[int, ...]
    """
    Targeted training time.

    Units: `seconds`.
    """
    wheel_circumference: float
    """
    Wheel circumference.

    Units: `mm`.
    """


class UpdateEventData(TypedDict, total=False):
    cadence_average: float
    """
    Average Cadence.

    Units: `rpm`.
    """
    cadence_instant: float
    """
    Instantaneous Cadence.

    Units: `rpm`.
    """
    distance_total: int
    """
    Total Distance.

    Units: `m`.
    """
    elevation_gain_negative: int
    """
    Negative Elevation Gain.

    Units: `m`.
    """
    elevation_gain_positive: int
    """
    Positive Elevation Gain.

    Units: `m`.
    """
    energy_per_hour: int
    """
    Energy Per Hour.

    Units: `kcal`.
    """
    energy_per_minute: int
    """
    Energy Per Minute.

    Units: `kcal`.
    """
    energy_total: int
    """
    Total Energy.

    Units: `kcal`.
    """
    force_on_belt: int
    """
    Force on Belt.

    Units: `newton`.
    """
    heart_rate: int
    """
    Heart Rate.

    Units: `bpm`.
    """
    inclination: float
    """
    Inclination.

    Units: `%`.
    """
    metabolic_equivalent: float
    """
    Metabolic Equivalent.

    Units: `meta`.
    """
    movement_direction: MovementDirection
    """
    Movement Direction.

    Units: `MovementDirection`.
    """
    pace_average: int | float
    """
    Average Pace.

    Units: `Km/m` or `Seconds(500m)` for `Rower`.
    """
    pace_instant: int | float
    """
    Instantaneous Pace.

    Units: `Km/m` or `Seconds(500m)` for `Rower`.
    """
    power_average: int
    """
    Average Power.

    Units: `Watts`.
    """
    power_instant: int
    """
    Instantaneous Power.

    Units: `Watts`.
    """
    power_output: int
    """
    Power Output.

    Units: `Watts`.
    """
    ramp_angle: float
    """
    Ramp Angle Setting.

    Units: `deg`.
    """
    resistance_level: int | float
    """
    Resistance Level.

    Units: `unitless`.
    """
    speed_average: float
    """
    Average Speed.

    Units: `Km/h`.
    """
    speed_instant: float
    """
    Instantaneous Speed.

    Units: `Km/h`.
    """
    step_rate_average: int
    """
    Average Step Rate.

    Units: `step_per_minute`.
    """
    step_rate_instant: int
    """
    Instantaneous Step Rate.

    Units: `step_per_minute`.
    """
    stride_count: int
    """
    Stride Count.

    Units: `unitless`.
    """
    stroke_count: int
    """
    Stroke Count.

    Units: `unitless`.
    """
    stroke_rate_average: float
    """
    Average Stroke Rate.

    Units: `stroke/m`.
    """
    stroke_rate_instant: float
    """
    Instantaneous Stroke Rate.

    Units: `stroke/m`.
    """
    time_elapsed: int
    """
    Elapsed Time.

    Units: `s`.
    """
    time_remaining: int
    """
    Remaining Time.

    Units: `s`.
    """


class TrainingStatusEventData(TypedDict):
    """`TrainingStatusEvent` data."""

    code: TrainingStatusCode
    string: NotRequired[str]


class TrainingStatusEvent(NamedTuple):
    """Training Status Event."""

    event_id: Literal["training_status"]
    event_data: TrainingStatusEventData


class UpdateEvent(NamedTuple):
    """Update Event."""

    event_id: Literal["update"]
    event_data: UpdateEventData


class SpinDownEvent(NamedTuple):
    """Spin Down Procedure Event."""

    event_id: Literal["spin_down"]
    event_data: SpinDownEventData


class SetupEvent(NamedTuple):
    """Setting Event."""

    event_id: Literal["setup"]
    event_data: SetupEventData
    event_source: ControlSource


class ControlEvent(NamedTuple):
    """Control Event."""

    event_id: SimpleControlEvents
    event_source: ControlSource


FtmsEvents = (
    UpdateEvent | SetupEvent | ControlEvent | TrainingStatusEvent | SpinDownEvent
)
"""Tagged union of FTMS events."""

FtmsCallback = Callable[[FtmsEvents], None]
"""Callback function to receive FTMS events."""
