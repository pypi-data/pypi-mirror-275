from gdtransform.transform import transformation_builder

from .textclassification import TextClassificationTransformation


@transformation_builder(is_batch=True)
def text_classification(*args, **kwargs):
    model = kwargs['model']
    input_field = kwargs['input_field']
    top_k_scores = int(kwargs['top_k_scores']) if 'top_k_scores' in kwargs and kwargs['top_k_scores'] else 1
    full_output_field = kwargs.get('full_output_field', None)
    label_output_field = kwargs.get('label_output_field', None)
    score_output_field = kwargs.get('score_output_field', None)
    gpu_device = int(kwargs.get('gpu_device')) if 'gpu_device' in kwargs and kwargs['gpu_device'] else None

    text_classifier = TextClassificationTransformation(model, input_field, top_k_scores=top_k_scores,
                                                       full_output_field=full_output_field,
                                                       label_output_field=label_output_field,
                                                       score_output_field=score_output_field,
                                                       gpu_device=gpu_device)

    return text_classifier.transform
