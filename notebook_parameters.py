from dataclasses import dataclass

@dataclass(frozen=True, kw_only=True)
class SampleDecisionSystemParameters:
    '''Класс с параметрами генерации ЭИС'''
    i_max: int # число строк в результирующей ТР
    input_var_lens: list[int] # Количество значений каждой входной переменной
    output_var_lens: list[int] # Количество значений каждой выходной переменной
    attribute_connections: list[list[int]] # Связи атрибутов решения с атрибутами условия
    connected_probabilities: list[float] # Вероятности расположения связанных атрибутов на той или иной позиции
@dataclass(frozen=True, kw_only=True)
class NotebookParameters(SampleDecisionSystemParameters):
    '''Класс для передачи параметров в Jupyter Notebook генератора ЭИС'''
    output_file_path: str # Путь для сохранения результирующей таблицы решений