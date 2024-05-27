import os
from typing import Literal

import pandas as pd
import pyreadr


Games = Literal["maismilionaria", "megasena", "lotofacil", "quina", "lotomania", "duplasena", "diadesorte"]
Types = Literal["numbers", "winners"]

class InvalidGameError(ValueError):
    """Raised when an invalid game is provided."""
    def __init__(self, game: str):
        super().__init__(f"Invalid game: {game}. Must be one of {', '.join(Games.__args__)}.")

class InvalidTypeError(ValueError):
    """Raised when an invalid type is provided."""
    def __init__(self, type: str):
        super().__init__(f"Invalid type: {type}. Must be one of {', '.join(Types.__args__)}.")

def get_data(
    game: Games, 
    type: Types, 
) -> pd.DataFrame:
    """
    Loads data for the specified lottery game and data type.

    This function fetches the data from a specified lottery game and data type, either 'numbers' or 'winners',
    directly from the LotteryBrasilDATA repository on GitHub.

    Parameters
    ----------
    game : Games
        The name of the lottery game whose data we want to load.
        Allowed values are:
        - 'maismilionaria' for the Mais Milionária game
        - 'megasena' for the Mega-Sena game
        - 'lotofacil' for the Lotofácil game
        - 'quina' for the Quina game
        - 'lotomania' for the Lotomania game
        - 'duplasena' for the Dupla Sena game
        - 'diadesorte' for the Dia de Sorte game
    type : Types
        The type of data to be loaded.
        Allowed values are:
        - 'numbers' for the drawn numbers data
        - 'winners' for the winners data

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the data loaded.

    Raises
    ------
    InvalidGameError
        If the provided `game` is not valid.
    InvalidTypeError
        If the provided `type` is not valid.
    ValueError
        If there is an issue loading the RDS file from the URL.
    
    Examples
    --------
    Load drawn numbers data for the Mega-Sena game:

    >>> df = get_data('megasena', 'numbers')
    >>> print(df.head())

    Load winners data for the Lotofácil game:

    >>> df = get_data('lotofacil', 'winners')
    >>> print(df.head())
    """
    valid_games = {"maismilionaria", "megasena", "lotofacil", "quina", "lotomania", "duplasena", "diadesorte"}
    valid_types = {"numbers", "winners"}

    if game not in valid_games:
        raise InvalidGameError(game)

    if type not in valid_types:
        raise InvalidTypeError(type)
    
    match type:
        case 'numbers':
            type_str = 'dezenas'
        case 'winners':
            type_str = 'ganhadores'

    url = f"https://github.com/tomasbp2/LotteryBrasilDATA/blob/main/{game}/{type_str}.rds?raw=true"

    try:
        module_dir = os.path.dirname(os.path.abspath(__file__))
        dst_dir = os.path.join(module_dir, "..", "dataset", game)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        dst_path = os.path.join(dst_dir, f"{type_str}.rds")
        pyreadr.download_file(url, dst_path)
        result = pyreadr.read_r(dst_path)
        df = result[None]
        
    except Exception as e:
        raise ValueError(f"Error while importing data: {e}")
    
    return df
