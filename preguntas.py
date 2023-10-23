"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return len(tbl0)


def pregunta_02():
    return len(tbl0.columns)


def pregunta_03():
    contar = tbl0['_c1'].value_counts().sort_index()
    return contar.rename('_c1')


def pregunta_04():
    return tbl0.groupby('_c1')['_c2'].mean()


def pregunta_05():
    return tbl0.groupby('_c1')['_c2'].max()


def pregunta_06():
    return sorted(tbl1['_c4'].str.upper().unique())


def pregunta_07():
    return tbl0.groupby('_c1')['_c2'].sum()


def pregunta_08():
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0


def pregunta_09():
    df = pd.read_csv('tbl0.tsv', sep='\t')
    df['year'] = df['_c3'].str[:4]
    return df


def pregunta_10():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    result = tbl0.groupby('_c1')['_c2'].agg(list).reset_index()
    result['_c2'] = result['_c2'].apply(lambda x: sorted(x))
    result['_c2'] = result['_c2'].apply(lambda x: ':'.join(map(str, x)))
    result.set_index('_c1', inplace=True)
    return result


def pregunta_11():
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl1 = tbl1.sort_values(by='_c4')
    result = tbl1.groupby('_c0')['_c4'].agg(','.join).reset_index()
    return result


def pregunta_12():
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
    tbl2 = tbl2.sort_values(by=['_c5a', '_c5b'])
    tbl2['_c5'] = tbl2['_c5a'].astype(str) + ':' + tbl2['_c5b'].astype(str)
    result = tbl2.groupby('_c0')['_c5'].agg(','.join).reset_index()
    return result


def pregunta_13():
    merged = pd.merge(tbl0, tbl2, on='_c0')
    result = merged.groupby('_c1')['_c5b'].sum()
    return result

