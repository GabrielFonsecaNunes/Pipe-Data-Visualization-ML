import pandas as pd
import numpy as np
from numpy import random
from datetime import datetime, timedelta

def get_target_dates() -> list:
    """
    Returns:
        target_dts: É uma lista com as datas dos ultimos 3 meses 
    para avaliação
    """
    target_dts = [datetime.strftime(
        datetime.now() - timedelta(days=n*31), '%Y%m') for n in range(1, 4)]
    return target_dts


def get_scoring_dates() -> list:
    """
    Returns:
        scoring_dates: É uma lista com as datas dos ultimos 3 meses 
    para escoragem 
    """
    scoring_dts = [datetime.strftime(
        datetime.now() - timedelta(days=n*31), '%Y%m') for n in range(0, 3)]
    return scoring_dts

def get_eval_df() -> pd.DataFrame():
    """
    Returns:
        eval_df: Dataframe sintetico com score dos modelos
    """
    nr_cod_modelo = [str(cod).zfill(8) for cod in range(51) for decil in range(10) for n_data in range(len(get_target_dates()))]
    nm_modelo = [f"Propensao xpto {cod}" for cod in range(51) for decil in range(10) for n_data in range(len(get_target_dates()))]
    tp_model = ["COMPRADO" if cod % 2 == 0 else "VENDIDO" for cod in range(51) for decil in range(10) for n_data in range(len(get_target_dates()))]
    decil = [decil for cod in range(51) for n_data in range(len(get_target_dates())) for decil in range(1, 11)]

    ks = list()
    conversao = list()

    for cod in range(51):
        for date in get_scoring_dates():
            seed = random.randint(low= 29, high= 70, size = 1)
            ks.extend(list(map(lambda x : round(x, 3), sorted(np.random.normal(loc = seed, scale = 10, size= 10), reverse= True))))
            conversao.extend(list(map(lambda x : round(x, 3), sorted(random.uniform(low = 0.005, high= 0.1, size=10), reverse= True))))
    
    eval_df = pd.DataFrame(
        data = {
            'nr_cod_modelo': nr_cod_modelo,
            'nm_modelo': nm_modelo,
            'tp_model': tp_model,
            'decil': decil,
            'ks': ks,
            'conversao': conversao,
            'data_scoragens': [date for cod in range(51) for date in get_scoring_dates() for decil in range(1, 11)],
            'data_target': [date for cod in range(51) for date in get_target_dates() for decil in range(1, 11)]
        }
    )

    return eval_df