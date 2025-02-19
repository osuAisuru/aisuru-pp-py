from typing import Iterable, List, Union

class ScoreParams:
    """
    A class to describe the state of a score to pass to a `Calculator`.
    Note that all attributes are optional.

    ## Attributes

    `mods`: Optional[int]
        Bit value for mods, defaults to 0 (NM) see [https://github.com/ppy/osu-api/wiki#mods](https://github.com/ppy/osu-api/wiki#mods)
    `acc`: Optional[float]
        Accuracy between 0.0 and 100.0.
        If neither acc nor hitresults are specified, acc defaults to 100.0.
    `n300`: Optional[int]
        Amount of 300s, defaults to value based on acc.
    `n100`: Optional[int]
        Amount of 100s, defaults to value based on acc.
    `n50`: Optional[int]
        Amount of 50s, defaults to value based on acc.
    `nMisses`: Optional[int]
        Amount of misses, defaults to 0.
    `nKatu`: Optional[int]
        Amount of katus. Only important for osu!ctb.
    `combo`: Optional[int]
        The max combo of the score, defaults to full combo.
    `score`: Optional[int]
        The final score. Only important for osu!mania.
    `passedObjects`: Optional[int]
        Amount of hitobjects to be considered. Useful for failed plays.
        Defaults to all objects.
    `clockRate`: Optional[float]
        Customizable clock rate to replace the one dictated by mods.
        Defaults to the mod's clock rate.

    ## Example
    ```py
    # specify through setter
    params = ScoreParams()
    params.acc = 98.76

    # specify through constructor kwargs
    params = ScoreParams(acc = 98.76)
    ```
    """
    def __init__(self, **kwargs) -> None: ...

class CalculateResult:
    """
    A class that contains all difficulty and performance attributes.
    Most attributes are optional based on the map's mode.
    In the following, O/T/C/M will denote for which mode the given attribute will be present.

    ## Attributes

    `mode`: int
        Game mode of the map. (O/T/C/M)
    `stars`: float
        Star rating of the map. (O/T/C/M)
    `pp`: float
        Performance points of the score. (O/T/C/M)
    `ppAcc`: Optional[float]
        Accuracy based portion of the performance points. (O/T/M)
    `ppAim`: Optional[float]
        Aim based portion of the performance points. (O)
    `ppFlashlight`: Optional[float]
        Flashlight based portion of the performance points. (O)
    `ppSpeed`: Optional[float]
        Speed based portion of the performance points. (O)
    `ppStrain`: Optional[float]
        Strain based portion of the performance points. (T/M)
    `nFruits`: Optional[int]
        The amount of fruits in the map. (C)
    `nDroplets`: Optional[int]
        The amount of droplets in the map. (C)
    `nTinyDroplets`: Optional[int]
        The amount of tiny droplets in the map. (C)
    `aimStrain`: Optional[float]
        Aim based portion of the star rating. (O)
    `speedStrain`: Optional[float]
        Speed based portion of the star rating. (O)
    `flashlightRating`: Optional[float]
        Flashlight based portion of the star rating. (O)
    `sliderFactor`: Optional[float]
        Nerf factor for sliders. (O)
    `ar`: float
        Approach rate of the map. (O/T/C/M)
    `cs`: float
        Circle size of the map. (O/T/C/M)
    `hp`: float
        Health drain rate of the map. (O/T/C/M)
    `od`: float
        Overall difficulty of the map. (O/T/C/M)
    `bpm`: float
        Beats per minute of the map. (O/T/C/M)
    `clockRate`: float
        Clock rate used in calculation i.e. 1.5 for DT, 0.75 for HT, 1.0 for NM or one that was specified (O/T/C/M)
    `nCircles`: Optional[int]
        The amount of circles in the map. (O/T/M)
    `nSliders`: Optional[int]
        The amount of sliders in the map. (O/T/M)
    `nSpinners`: Optional[int]
        The amount of spinners in the map. (O/T/C)
    `maxCombo`: Optional[int]
        The max combo of the map. (O/T/C)
    """
    def __init__(self) -> None: ...

class Calculator:
    """
    A class to calculate difficulty and performance attributes.

    ## Arguments

    `path`: str
        The path to the .osu file.

    ## Named arguments

    `ar`: Optional[float]
        Adjusts the map's approach rate.
    `cs`: Optional[float]
        Adjusts the map's circle size.
    `hp`: Optional[float]
        Adjusts the map's drain rate.
    `od`: Optional[float]
        Adjusts the map's overall difficulty.

    ## Methods

    `set_ar(ar)`
        Specify an approach rate to override the map's value.
    `set_cs(cs)`
        Specify a circle size to override the map's value.
    `set_hp(hp)`
        Specify a drain rate to override the map's value.
    `set_od(od)`
        Specify an overall difficulty to override the map's value.
    `calculate(params)`
        Calculate the difficulty and performance attributes for the given score parameters.

    ## Raises

    Throws an Exception if the map could not be parsed or an invalid named argument was given.
    """
    def __init__(self, path: str) -> None: ...

    def calculate(self, params: Union[ScoreParams, Iterable[ScoreParams]]) -> List[CalculateResult]:
        """
        Calculate the difficulty and performance attributes for the given score parameters.

        ## Arguments

        `params`: Either a single `ScoreParams` or multiple `ScoreParams` in an iterable collection.

        ## Returns

        A list of `CalculateResult` consisting of difficulty and performance attributes for each given `ScoreParams`

        ## Example

        ```py
        calculator = Calculator('./maps/1980365.osu')

        params1 = ScoreParams(mods = 8 + 16) # HDHR
        params2 = ScoreParams(
            mods = 24,
            acc = 97.89,
            nMisses = 13,
            combo = 1388,
        )

        # provide params for one score
        result1 = calculator.calculate(params1)

        # provide params for multiple scores
        results = calculator.calculate([params1, params2])
        ```
        """