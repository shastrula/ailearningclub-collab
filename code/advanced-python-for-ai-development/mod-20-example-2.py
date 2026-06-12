import skl2onnx
from skl2onnx.common.data_types import FloatTensorType

initial_type = [('float_input', FloatTensorType([None, 10]))]
onnx_model = skl2onnx.convert_sklearn(
    sklearn_model,
    initial_types=initial_type
)

# Deploy ONNX everywhere
import onnxruntime as rt
sess = rt.InferenceSession('model.onnx')