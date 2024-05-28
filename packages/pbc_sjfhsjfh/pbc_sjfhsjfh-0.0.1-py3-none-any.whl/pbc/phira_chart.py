from __future__ import annotations

from typing import Generic, List, Literal, Optional, Tuple, TypeVar

from .utils.fraction import Fraction

T = TypeVar("T")


class PhiraKeyFrame(Generic[T]):
    def __init__(self, time: float, value: T, tween: int):
        """
        The tween function is actually a function and here we use the id of the function.

        Args:
            time (float): time
            value (T): value
            tween (int): tween function id, see [here](https://github.com/TeamFlos/phira/blob/98fcaccda75db867232fe65bbacbae56a2b5d928/prpr/src/core/tween.rs#L100)
        """
        self.time = time
        self.value = value


class PhiraAnim(Generic[T]):
    def __init__(
        self,
        time: float = 0.,
        keyframes: List[PhiraKeyFrame[T]] = [],
        cursor: int = 0,
        next: Optional[PhiraAnim[T]] = None,
    ):
        self.time = time
        self.keyframes = keyframes
        self.cursor = cursor
        self.next = next
        """
        Used for multi layer animations
        
        a1 + a2 => a1.next = a2
        
        a1 + a2 + a3 + ... => a1.next = a2, a2.next = a3, a3.next = ...
        """

    @classmethod
    def fixed(cls, value: T) -> PhiraAnim[T]:
        return cls(keyframes=[PhiraKeyFrame(0., value, 0)])


class PhiraBpmList:
    """
    See https://github.com/TeamFlos/phira/blob/main/prpr/src/core.rs
    """
    class BpmItem:
        def __init__(self, beats: float, time: float, bpm: float):
            self.beats = beats
            self.time = time
            self.bpm = bpm

    def __init__(self, bpms: List[Tuple[float, float]]):
        elements: List[PhiraBpmList.BpmItem] = []
        time = 0.
        last_beats = 0.
        last_bpm: Optional[float] = None
        for beats, bpm in bpms:
            if last_bpm is not None:
                time += (beats - last_beats) * 60. / last_bpm
            elements.append(PhiraBpmList.BpmItem(beats, time, bpm))
            last_beats = beats
            last_bpm = bpm
        self.elements = elements
        self.cursor: int = 0

    def beats_to_time(self, beats: float | Fraction) -> float:
        if isinstance(beats, Fraction):
            beats = beats.to_float()
        while self.cursor < len(self.elements) - 1 and self.elements[self.cursor].beats <= beats:
            self.cursor += 1
        while self.cursor > 0 and self.elements[self.cursor].beats > beats:
            self.cursor -= 1
        item = self.elements[self.cursor]
        return item.time + (beats - item.beats) * (60. / item.bpm)

    def time_to_beats(self, time: float) -> float:
        while self.cursor < len(self.elements) - 1 and self.elements[self.cursor].time <= time:
            self.cursor += 1
        while self.cursor > 0 and self.elements[self.cursor].time > time:
            self.cursor -= 1
        item = self.elements[self.cursor]
        return item.beats + (time - item.time) / (60. / item.bpm)


class PhiraChartSettings:
    def __init__(self, pe_alpha_extension: bool = False, hold_partial_cover: bool = False):
        self.pe_alpha_extension = pe_alpha_extension
        self.hold_partial_cover = hold_partial_cover


class PhiraChart:

    def __init__(
        self,
        offset: float,
        lines: List[PhiraLine],
        bpm_list: PhiraBpmList,
        settings: PhiraChartSettings = PhiraChartSettings(),
    ):
        self.offset = offset
        self.lines = lines
        self.bpm_list = bpm_list
        self.settings = settings


class PhiraObject:
    def __init__(
        self,
        alpha: PhiraAnim[float] = PhiraAnim(),
        scale: Tuple[PhiraAnim[float], PhiraAnim[float]] = (
            PhiraAnim(), PhiraAnim()),
        rotation: PhiraAnim[float] = PhiraAnim(),
        translation: Tuple[PhiraAnim[float], PhiraAnim[float]] = (
            PhiraAnim(), PhiraAnim()),
    ):
        self.alpha = alpha
        self.scale = scale
        self.rotation = rotation
        """in degrees"""
        self.translation = translation


class PhiraControlObject:
    """
    这啥啊
    """

    def __init__(
        self,
        alpha: PhiraAnim[float] = PhiraAnim(),
        size: PhiraAnim[float] = PhiraAnim(),
        pos: PhiraAnim[float] = PhiraAnim(),
        y: PhiraAnim[float] = PhiraAnim(),
    ):
        self.alpha = alpha
        self.size = size
        self.pos = pos
        self.y = y


class PhiraLine:
    """
    See https://github.com/TeamFlos/phira/blob/main/prpr/src/core/line.rs
    """

    def __init__(
        self,
        notes: List[PhiraNote],
        object: PhiraObject = PhiraObject(),
        height: PhiraAnim[float] = PhiraAnim(),
        kind: Literal["normal"] = "normal",
        z_index: int = 0,
        parent: Optional[int] = None,
        attach_ui: Optional[None] = None,
        ctrl_obj: PhiraControlObject = PhiraControlObject(),
        incline: PhiraAnim[float] = PhiraAnim(),
        color: PhiraAnim[Tuple[float, float, float, float]] = PhiraAnim(),
        show_below: bool = True,
    ):
        self.notes = notes
        self.object = object
        self.height = height
        self.kind = kind
        self.z_index = z_index
        self.parent = parent
        self.attach_ui = attach_ui
        self.ctrl_obj = ctrl_obj
        """Not sure what this is for, from RPE only"""
        self.incline = incline
        self.color = color
        self.show_below = show_below
        self.cache = None
        """This is calculated from notes, see
        
        https://github.com/TeamFlos/phira/blob/98fcaccda75db867232fe65bbacbae56a2b5d928/prpr/src/parse/pgr.rs#L204
        
        https://github.com/TeamFlos/phira/blob/98fcaccda75db867232fe65bbacbae56a2b5d928/prpr/src/parse/pec.rs#L160
        
        https://github.com/TeamFlos/phira/blob/98fcaccda75db867232fe65bbacbae56a2b5d928/prpr/src/parse/rpe.rs#L368
        """


class PhiraNote:
    """
    See https://github.com/TeamFlos/phira/blob/main/prpr/src/core/note.rs
    """

    def __init__(
        self,
        kind: Literal["tap", "drag", "hold", "flick"],
        time: float,
        height: float,
        multiple_hint: bool = False,
        object: PhiraObject = PhiraObject(),
        speed: float = 1.,
        above: bool = True,
        fake: bool = False,
        judge: Literal["NotJudged"] = "NotJudged",
    ):
        self.object = object
        self.kind = kind
        self.time = time
        self.height = height
        self.speed = speed
        self.above = above
        self.multiple_hint = multiple_hint
        self.fake = fake
        self.judge = judge
        """Not sure what this is for, from RPE only"""
