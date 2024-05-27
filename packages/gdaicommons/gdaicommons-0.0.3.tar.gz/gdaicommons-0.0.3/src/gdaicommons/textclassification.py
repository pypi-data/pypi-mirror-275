from typing import Any, Dict, List, Optional, Tuple

from transformers import pipeline


class TextClassificationTransformation:

    def __init__(self, model: str, input_field: str,
                 top_k_scores: Optional[int] = 1,
                 full_output_field: Optional[str] = None,
                 label_output_field: Optional[str] = None, score_output_field: Optional[str] = None,
                 gpu_device: Optional[int] = None):
        self._model = model
        self._input_field = input_field
        self._top_k_scores = top_k_scores if top_k_scores else 1
        self._full_output_field = full_output_field
        self._label_output_field = label_output_field
        self._score_output_field = score_output_field
        self._gpu_device = gpu_device
        self._pipeline = pipeline(model=self._model, device=self._gpu_device,
                                  top_k=top_k_scores if top_k_scores else 1)

    def transform(self, data_list: List[Dict[str, Any]]):
        indexed_inputs = self._get_indexed_inputs(data_list)
        model_inputs = [d for _, d in indexed_inputs]
        model_outputs = self._pipeline(model_inputs)
        if self._top_k_scores > 1:
            self._set_all_scores(data_list, indexed_inputs, model_outputs)
        else:
            self._set_label_score(data_list, indexed_inputs, model_outputs)

    def _get_indexed_inputs(self, data_list: List[Dict[str, Any]]) -> List[Tuple[int, str]]:
        indexed_inputs = []
        for idx, data in enumerate(data_list):
            if self._input_field in data and data[self._input_field] is not None:
                indexed_inputs.append((idx, data[self._input_field],))

        return indexed_inputs

    def _set_all_scores(self, data_list: List[Dict[str, Any]], indexed_inputs: List[Tuple[int, str]],
                        model_outputs: List[List[Dict]]):
        for idx, (data_index, _) in enumerate(indexed_inputs):
            model_output = model_outputs[idx]
            data_list[data_index][self._full_output_field] = model_output

    def _set_label_score(self, data_list: List[Dict[str, Any]], indexed_inputs: List[Tuple[int, str]],
                         model_outputs: List[List[Dict]]):
        for idx, (data_index, _) in enumerate(indexed_inputs):
            model_output = model_outputs[idx]
            data_list[data_index][self._label_output_field] = model_output[0]['label']
            if self._score_output_field:
                data_list[data_index][self._score_output_field] = model_output[0]['score']
